---
layout: landing
title: "Jeff Chunag — Research × Art × Product"
description: "Bilingual hub for research, product experiments, and art projects."
lang: en
alt_url: /zh/
permalink: /
keywords:
  - Jeff Chuang
  - Biodesign
  - Cross-border commerce
  - PresenterAI
  - Startup research
---

# Startups × Capital × Art × Research

When AI redefines labor and gene editing rewrites what life can be, single-track careers feel insufficient. I’m building at the intersections—braiding startup speed, artistic empathy, and research rigor to surface answers that actually move people forward.

---

## What I'm Exploring

- **Research Programs** — With NTU BEBI labs, modeling gene expression from **spatial transcriptomics** data to fuse imaging and genomics.
- **Company Sprints** — Running **SaaS rapid iterations** and **cross-border commerce tests** to pressure-test market demand.
- **Art Narratives** — Translating **math and policy** into sensory stories that audiences can feel before they understand.

---

## Research & Product Highlights

- **Spider Silk Protein Generation** — Collaborating with NTU BST on sequence design experiments.
- **Spatial Transcriptomics Field Trials** — Clinical pilots with NTU BEBI medical teams.
- **PresenterAI** — Turning academic decks into a **generative storytelling tool** for public audiences.
- **Shihui** — An **end-to-end commerce app** helping new founders outgrow traditional cross-border playbooks.

---

## Latest Writing

{% assign latest_posts = site.posts | where: "lang", "en" | sort: "date" | reverse | slice: 0, 3 %}
{% if latest_posts.size > 0 %}
- {% for post in latest_posts %}[{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%b %d, %Y" }}{% endfor %}
{% else %}
- Essays in English are coming soon. Peek at the 中文版 for current notes.
{% endif %}

Browse the full archive on the [Blog](/blog/); I publish one essay a week around practice, research, and venture building.

---

## Collaborate & Connect

Reach out at [tomnandy922@gmail.com](mailto:tomnandy922@gmail.com) or [LinkedIn](https://www.linkedin.com/in/jeff-zhuang-b45117316).

I stream nightly on [Twitch](https://www.twitch.tv/cooljeffchuang) from 20:00–22:00, unpacking research notes and founder routines.
