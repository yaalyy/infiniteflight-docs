---
title: Infinite Flight 中文文档
permalink: /
---

# Infinite Flight 中文文档

这是中文文档站点的导航页。点击下方各个 guide 可以展开查看 section 和具体页面。

{% assign sorted_pages = site.pages | sort: "path" %}
{% assign guides = "getting-started-guide|flying-guide|atc-guide|atc-manual|developer-reference|get-help|scenario-editor-manual|scenery-editor-manual|legal" | split: "|" %}

<p>
  快速跳转:
  {% for guide in guides %}
    {% capture guide_index_path %}{{ guide }}/index.md{% endcapture %}
    {% assign guide_index = sorted_pages | where: "path", guide_index_path | first %}
    {% assign guide_title = guide_index.title %}
    {% if guide_title == nil %}
      {% case guide %}
        {% when "legal" %}
          {% assign guide_title = "法律" %}
        {% else %}
          {% assign guide_title = guide %}
      {% endcase %}
    {% endif %}
    <a href="#{{ guide }}">{{ guide_title }}</a>{% unless forloop.last %} | {% endunless %}
  {% endfor %}
</p>

{% for guide in guides %}
  {% capture guide_index_path %}{{ guide }}/index.md{% endcapture %}
  {% assign guide_index = sorted_pages | where: "path", guide_index_path | first %}
  {% assign guide_title = guide_index.title %}
  {% if guide_title == nil %}
    {% case guide %}
      {% when "legal" %}
        {% assign guide_title = "法律" %}
      {% else %}
        {% assign guide_title = guide %}
    {% endcase %}
  {% endif %}

  <div id="{{ guide }}"></div>
  <details>
    <summary>
      {% if guide_index %}
        <a href="{{ guide_index.url | relative_url }}">{{ guide_title }}</a>
      {% else %}
        {{ guide_title }}
      {% endif %}
    </summary>

    {% capture ordering_path %}{{ guide }}/_ordering.md{% endcapture %}
    {% assign ordering_page = sorted_pages | where: "path", ordering_path | first %}

    {% if ordering_page and ordering_page.ordering %}
      {% for raw_section in ordering_page.ordering %}
        {% unless raw_section == "meta" %}
          {% assign section_path = raw_section %}
          {% if guide == "atc-guide" and raw_section == "radar" %}
            {% assign section_path = "_radar" %}
          {% endif %}

          {% capture section_prefix %}{{ guide }}/{{ section_path }}/{% endcapture %}
          {% assign section_pages = sorted_pages | where_exp: "item", "item.path contains section_prefix" | sort: "order" %}

          {% if section_pages.size > 0 %}
            {% assign section_label = section_path | remove_first: "_" | replace: "-", " " | replace: ".-", ". " %}
            <h3>{{ section_label }}</h3>
            <ul>
              {% for doc in section_pages %}
                {% assign filename = doc.path | split: "/" | last %}
                {% unless filename == "index.md" or filename == "_meta.md" or filename == "_ordering.md" %}
                  <li><a href="{{ doc.url | relative_url }}">{{ doc.title | default: filename }}</a></li>
                {% endunless %}
              {% endfor %}
            </ul>
          {% endif %}
        {% endunless %}
      {% endfor %}
    {% else %}
      {% capture root_prefix %}{{ guide }}/{% endcapture %}
      {% assign direct_pages = sorted_pages | where_exp: "item", "item.path contains root_prefix" | sort: "order" %}
      <ul>
        {% for doc in direct_pages %}
          {% assign filename = doc.path | split: "/" | last %}
          {% assign parts = doc.path | split: "/" %}
          {% if parts.size == 2 and filename != "index.md" and filename != "_meta.md" and filename != "_ordering.md" %}
            <li><a href="{{ doc.url | relative_url }}">{{ doc.title | default: filename }}</a></li>
          {% endif %}
        {% endfor %}
      </ul>
    {% endif %}
  </details>
{% endfor %}

## 其他页面

- [翻译说明与仓库约定](./README.html)
