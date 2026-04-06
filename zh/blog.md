---
layout: page
title: "文章"
description: "關於深度學習、商業、交易與開源工具的文章。"
permalink: /zh/blog/
lang: zh
alt_url: /blog/
---

{% assign posts = site.posts | where: "lang", "zh" | sort: "date" | reverse %}
{% assign categories = posts | map: "category" | uniq %}

{% for cat in categories %}
<section class="blog-section">
  {% assign sample = posts | where: "category", cat | first %}
  <h2 class="blog-category">{{ sample.category_zh | default: cat }}</h2>
  <div class="post-list">
    {% assign cat_posts = posts | where: "category", cat %}
    {% for post in cat_posts %}
    <article class="post-item">
      <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y-%m-%d" }}</time>
      <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      <p>{{ post.excerpt | strip_html | truncate: 200 }}</p>
    </article>
    {% endfor %}
  </div>
</section>
{% endfor %}

{% if posts.size == 0 %}
<p>尚無文章，敬請期待。</p>
{% endif %}
