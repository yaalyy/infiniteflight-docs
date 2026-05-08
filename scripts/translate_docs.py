#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Iterable
from urllib.parse import quote, unquote


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / "zh-docs"
CODEX_BIN = Path("/Applications/Codex.app/Contents/Resources/codex")
SKIP_DIRS = {".git", "zh-docs", "_site", "node_modules"}
TEXT_EXTENSIONS = {".md"}
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
CODE_FENCE_RE = re.compile(r"^(```|~~~)")


TRANSLATION_PROMPT = """You are translating Infinite Flight documentation from English to Simplified Chinese.

Rules:
- Return only the translated Markdown content.
- Preserve YAML frontmatter keys exactly as-is. Translate frontmatter values like title, meta, and description when natural.
- Preserve Markdown structure, headings, lists, tables, blockquotes, code fences, HTML, shortcode syntax like @[vimeo](...), and blank lines.
- Preserve relative links and image paths exactly as they appear in the source. Do not rewrite URLs or file paths.
- Preserve technical terms when appropriate, especially aviation, ATC, API, HTTP, JSON, GPS, ILS, VOR, VNAV, SID, STAR, NOTAM, pushback, taxi, radar, and similar professional terminology.
- Keep product names like Infinite Flight in English.
- Translate natural-language labels such as Tip, Warning, Important, Notes, and table descriptions into clear Simplified Chinese when they appear as prose.
- Do not add explanations, comments, or surrounding backticks.

Translate the following file to Simplified Chinese:
FILE: {path}
"""


def list_markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        rel_parts = path.relative_to(root).parts
        if any(part in SKIP_DIRS for part in rel_parts):
            continue
        files.append(path)
    return sorted(files)


def run_codex(prompt: str, content: str, model: str) -> str:
    with tempfile.NamedTemporaryFile("w+", suffix=".txt", delete=False) as output_file:
        output_path = Path(output_file.name)

    cmd = [
        str(CODEX_BIN),
        "exec",
        "--skip-git-repo-check",
        "--color",
        "never",
        "-m",
        model,
        "-o",
        str(output_path),
        prompt,
    ]

    try:
        result = subprocess.run(
            cmd,
            input=content,
            text=True,
            capture_output=True,
            cwd=str(ROOT),
            check=False,
        )
        if result.returncode != 0:
            raise RuntimeError(
                "codex exec failed\n"
                f"returncode={result.returncode}\n"
                f"stdout={result.stdout[-4000:]}\n"
                f"stderr={result.stderr[-4000:]}"
            )
        translated = output_path.read_text(encoding="utf-8")
        if not translated.strip():
            raise RuntimeError("codex exec returned empty output")
        return translated
    finally:
        try:
            output_path.unlink(missing_ok=True)
        except OSError:
            pass


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return text
    return parts[2]


def extract_headings(text: str) -> list[str]:
    text = strip_frontmatter(text)
    headings: list[str] = []
    in_code_fence = False

    for line in text.splitlines():
        if CODE_FENCE_RE.match(line.strip()):
            in_code_fence = not in_code_fence
            continue
        if in_code_fence:
            continue
        match = HEADING_RE.match(line)
        if not match:
            continue
        heading = match.group(2).strip()
        heading = re.sub(r"\s+#+\s*$", "", heading).strip()
        if heading:
            headings.append(heading)

    return headings


def github_like_slug(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^\w\u4e00-\u9fff\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    return text.strip("-")


def legacy_anchor_variants(heading: str) -> list[str]:
    normalized = re.sub(r"\s+", " ", heading.strip())
    hyphenated = re.sub(r"\s+", "-", normalized.lower())
    compact = github_like_slug(normalized)
    candidates = [
        normalized,
        normalized.lower(),
        hyphenated,
        compact,
        quote(normalized, safe=""),
        quote(normalized.lower(), safe=""),
        quote(hyphenated, safe=""),
        quote(compact, safe=""),
        unquote(normalized),
        unquote(hyphenated),
        unquote(compact),
    ]

    if re.fullmatch(r"[\d.]+", normalized):
        candidates.extend([normalized, quote(normalized, safe="")])

    seen: set[str] = set()
    variants: list[str] = []
    for candidate in candidates:
        candidate = candidate.strip()
        if not candidate or candidate in seen:
            continue
        seen.add(candidate)
        variants.append(candidate)
    return variants


def add_legacy_heading_anchors(source_text: str, translated_text: str) -> str:
    source_headings = extract_headings(source_text)
    translated_headings = extract_headings(translated_text)
    if not source_headings or len(source_headings) != len(translated_headings):
        return translated_text

    output_lines: list[str] = []
    heading_index = 0
    in_code_fence = False

    for line in translated_text.splitlines():
        stripped = line.strip()
        if CODE_FENCE_RE.match(stripped):
            in_code_fence = not in_code_fence
            output_lines.append(line)
            continue

        if not in_code_fence and HEADING_RE.match(line):
            source_heading = source_headings[heading_index]
            anchors = legacy_anchor_variants(source_heading)
            for anchor in anchors:
                output_lines.append(f'<a id="{anchor}"></a>')
            heading_index += 1

        output_lines.append(line)

    trailing_newline = "\n" if translated_text.endswith("\n") else ""
    return "\n".join(output_lines) + trailing_newline


def resolve_guide_link_target(guide_path: str) -> Path | None:
    normalized = guide_path.strip("/")
    if not normalized.startswith("guide/"):
        return None

    doc_path = normalized[len("guide/") :]
    path_variants = [doc_path]
    dotted_variant = re.sub(r"(^|/)(\d+[a-z]?)-", r"\1\2.-", doc_path)
    if dotted_variant not in path_variants:
        path_variants.append(dotted_variant)

    candidates: list[Path] = []
    for variant in path_variants:
        candidates.extend(
            [
                OUTPUT_ROOT / f"{variant}.md",
                OUTPUT_ROOT / variant / "index.md",
                OUTPUT_ROOT / variant,
            ]
        )
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return None


def rewrite_guide_links(rel_path: Path, text: str) -> str:
    current_file = OUTPUT_ROOT / rel_path
    pieces: list[str] = []
    cursor = 0

    while True:
        marker = text.find("](/guide/", cursor)
        if marker == -1:
            pieces.append(text[cursor:])
            break

        target_start = marker + 2
        pieces.append(text[cursor:target_start])

        idx = target_start
        depth = 0
        while idx < len(text):
            char = text[idx]
            if char == "(":
                depth += 1
            elif char == ")":
                if depth == 0:
                    break
                depth -= 1
            idx += 1

        if idx >= len(text):
            pieces.append(text[target_start:])
            break

        target = text[target_start:idx]
        path_part, hash_part = (target.split("#", 1) + [""])[:2]
        resolved = resolve_guide_link_target(path_part)
        if resolved is None:
            rewritten_target = target
        else:
            relative_link = Path(os.path.relpath(resolved, current_file.parent)).as_posix()
            rewritten_target = f"{relative_link}#{hash_part}" if hash_part else relative_link

        pieces.append(rewritten_target)
        pieces.append(")")
        cursor = idx + 1

    return "".join(pieces)


def maybe_rewrite_root_relative_assets(rel_path: Path, text: str) -> str:
    depth = len(rel_path.parts) - 1
    prefix = "../" * (depth + 1)

    def repl(match: re.Match[str]) -> str:
        target = match.group("target")
        if "://" in target or target.startswith("mailto:") or target.startswith("#") or target.startswith("/"):
            return match.group(0)
        if target.startswith("_images/"):
            return match.group(0).replace(target, f"{prefix}{target}")
        return match.group(0)

    return re.sub(
        r"(?P<full>!?\[[^\]]*\]\((?P<target>[^)\s]+)(?P<suffix>[^)]*)\))",
        repl,
        text,
    )


def translate_file(src: Path, model: str, retries: int = 2) -> tuple[Path, str]:
    rel_path = src.relative_to(ROOT)
    dest = OUTPUT_ROOT / rel_path
    dest.parent.mkdir(parents=True, exist_ok=True)
    source_text = src.read_text(encoding="utf-8")
    prompt = TRANSLATION_PROMPT.format(path=rel_path.as_posix())

    last_error: Exception | None = None
    for attempt in range(1, retries + 2):
        try:
            translated = run_codex(prompt, source_text, model=model)
            translated = add_legacy_heading_anchors(source_text, translated)
            translated = rewrite_guide_links(rel_path, translated)
            translated = maybe_rewrite_root_relative_assets(rel_path, translated)
            dest.write_text(translated, encoding="utf-8")
            return rel_path, "ok"
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            time.sleep(min(5 * attempt, 15))

    assert last_error is not None
    return rel_path, f"error: {last_error}"


def write_index(files: Iterable[Path]) -> None:
    index_path = OUTPUT_ROOT / "README-zh-index.md"
    lines = [
        "# Infinite Flight 中文翻译文档索引",
        "",
        "以下文件为从英文文档翻译得到的简体中文版，目录结构与原仓库保持一致。",
        "",
    ]
    for rel_path in files:
        lines.append(f"- `{rel_path.as_posix()}`")
    lines.append("")
    index_path.write_text("\n".join(lines), encoding="utf-8")


def postprocess_existing_translation(src: Path) -> tuple[Path, str]:
    rel_path = src.relative_to(ROOT)
    dest = OUTPUT_ROOT / rel_path
    if not src.is_file() or not dest.is_file():
        return rel_path, "skip"

    source_text = src.read_text(encoding="utf-8")
    translated_text = dest.read_text(encoding="utf-8")
    fixed_text = add_legacy_heading_anchors(source_text, translated_text)
    fixed_text = rewrite_guide_links(rel_path, fixed_text)
    fixed_text = maybe_rewrite_root_relative_assets(rel_path, fixed_text)
    dest.write_text(fixed_text, encoding="utf-8")
    return rel_path, "ok"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="gpt-5.4-mini")
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--postprocess-only", action="store_true")
    args = parser.parse_args()

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    files = list_markdown_files(ROOT)
    if args.limit > 0:
        files = files[: args.limit]

    print(f"Found {len(files)} markdown files to translate.", flush=True)
    completed: list[Path] = []
    failures: list[tuple[Path, str]] = []

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        task = postprocess_existing_translation if args.postprocess_only else translate_file
        futures = {executor.submit(task, path, args.model) if not args.postprocess_only else executor.submit(task, path): path for path in files}
        for idx, future in enumerate(as_completed(futures), start=1):
            rel_path, status = future.result()
            if status == "ok":
                completed.append(rel_path)
                label = "FIXED" if args.postprocess_only else "OK"
                print(f"[{idx}/{len(files)}] {label} {rel_path.as_posix()}", flush=True)
            else:
                failures.append((rel_path, status))
                print(f"[{idx}/{len(files)}] FAIL {rel_path.as_posix()} :: {status}", flush=True)

    write_index(sorted(completed))

    if failures:
        print("", flush=True)
        print("Failures:", flush=True)
        for rel_path, status in failures:
            print(f"- {rel_path.as_posix()}: {status}", flush=True)
        return 1

    print("", flush=True)
    action = "post-processing" if args.postprocess_only else "translation"
    print(f"Completed {action} for {len(completed)} files into {OUTPUT_ROOT}.", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
