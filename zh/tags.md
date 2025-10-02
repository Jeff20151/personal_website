---
layout: page
title: 標籤
description: "以主題瀏覽中文文章。"
permalink: /zh/tags/
lang: zh
alt_url: /tags/
---

{% assign current_lang = page.lang | default: site.default_lang %}
{% assign lang_posts = site.posts | where: "lang", current_lang %}
{% assign all_tags = "" | split: "" %}
{% for post in lang_posts %}
  {% assign all_tags = all_tags | concat: post.tags %}
{% endfor %}
{% assign tags = all_tags | uniq | sort %}

{% if tags.size == 0 %}
<p>目前尚無標籤，之後會同步更新。</p>
{% else %}
<ul class="tags-cloud">
  {% for tag in tags %}
    {% assign posts_for_tag = lang_posts | where_exp: "item", "item.tags contains tag" %}
    <li><a href="#{{ tag | slugify }}">{{ tag }}</a> ({{ posts_for_tag.size }})</li>
  {% endfor %}
</ul>

<hr />

{% for tag in tags %}
  {% assign posts_for_tag = lang_posts | where_exp: "item", "item.tags contains tag" %}
### {{ tag }} {#{{ tag | slugify }}}
  <ul>
    {% for post in posts_for_tag %}
      <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> <small>({{ post.date | date: "%Y-%m-%d" }})</small></li>
    {% endfor %}
  </ul>
{% endfor %}
{% endif %}
