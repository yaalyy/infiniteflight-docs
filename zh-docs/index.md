---
title: Infinite Flight 中文文档
permalink: /
---

# Infinite Flight 中文文档

这是中文文档站点的导航页。点击下方各个 guide 可以展开查看 section 和具体页面。

{% assign sorted_pages = site.pages | sort: "path" %}

<p>
  快速跳转:
  {% for guide in site.data.navigation.guides %}
    <a href="#{{ guide.slug }}">{{ guide.title }}</a>{% unless forloop.last %} | {% endunless %}
  {% endfor %}
</p>

{% for guide in site.data.navigation.guides %}
  {% capture guide_index_path %}{{ guide.slug }}/index.md{% endcapture %}
  {% assign guide_index = sorted_pages | where: "path", guide_index_path | first %}

  <div id="{{ guide.slug }}"></div>
  <details>
    <summary>
      {% if guide_index %}
        <a href="{{ guide_index.url | relative_url }}">{{ guide.title }}</a>
      {% else %}
        {{ guide.title }}
      {% endif %}
    </summary>

    {% if guide.sections %}
      {% for section in guide.sections %}
          {% capture section_prefix %}{{ guide.slug }}/{{ section.slug }}/{% endcapture %}
          {% assign section_pages = sorted_pages | where_exp: "item", "item.path contains section_prefix" | sort: "order" %}

          {% if section_pages.size > 0 %}
            <h3>{{ section.title }}</h3>
            <ul>
              {% for doc in section_pages %}
                {% assign filename = doc.path | split: "/" | last %}
                {% unless filename == "index.md" or filename == "_meta.md" or filename == "_ordering.md" %}
                  <li><a href="{{ doc.url | relative_url }}">{{ doc.title | default: filename }}</a></li>
                {% endunless %}
              {% endfor %}
            </ul>
          {% endif %}
      {% endfor %}
    {% else %}
      {% capture root_prefix %}{{ guide.slug }}/{% endcapture %}
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
