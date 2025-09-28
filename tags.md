---
layout: page
title: Tags
permalink: /tags
---

<ul class="tags-cloud">
  {% assign tags_list = site.tags | sort %}
  {% for tag in tags_list %}
    <li><a href="#{{ tag[0] }}">{{ tag[0] }}</a> ({{ tag[1].size }})</li>
  {% endfor %}
</ul>

<hr />

{% for tag in tags_list %}
### {{ tag[0] }} {#{{ tag[0] }}}
<ul>
  {% for post in tag[1] %}
    <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a> <small>({{ post.date | date: "%Y-%m-%d" }})</small></li>
  {% endfor %}
</ul>
{% endfor %}
