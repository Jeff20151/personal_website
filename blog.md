---
layout: page
title: "Blog"
description: "Articles on deep learning, business, trading, and open-source tools."
permalink: /blog/
lang: en
alt_url: /zh/blog/
---

{% assign posts = site.posts | where: "lang", "en" | sort: "date" | reverse %}
{% assign categories = posts | map: "category" | uniq %}

{% for cat in categories %}
<section class="blog-section">
  <h2 class="blog-category">{{ cat }}</h2>
  <div class="post-list">
    {% assign cat_posts = posts | where: "category", cat %}
    {% for post in cat_posts %}
    <article class="post-item">
      <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time>
      <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
      <p>{{ post.excerpt | strip_html | truncate: 200 }}</p>
    </article>
    {% endfor %}
  </div>
</section>
{% endfor %}

{% if posts.size == 0 %}
<p>No posts yet. Check back soon.</p>
{% endif %}
