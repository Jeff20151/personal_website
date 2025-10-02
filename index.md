---
layout: landing
title: "Jeff Chunag — Research × Art × Product"
description: "Bilingual hub for research, product experiments, and art projects."
lang: en
alt_url: /zh/
permalink: /
---

# Research × Art × Product

I connect bioelectronics research, cross-border commerce, and storytelling to build products that move between the lab, the market, and cultural spaces. This hub collects my current research tracks, launch experiments, and art collaborations.

## Current Focus

- **Research Programs** — Synthetic biology × bioelectronics prototypes with NTU BEBI labs.
- **Product Experiments** — Rapid SaaS validation sprints and dropshipping funnels tuned for different markets.
- **Cultural Storyteller** — Exhibitions and narrative-driven installations that translate data into experiences.

## Research Highlights

- *Adaptive Bio-Sensors for Point-of-Care Diagnostics* — Field tests with NTU BEBI clinics.
- *PresenterAI* — Generative tooling that bridges research decks and public storytelling.
- *市檜 (Shihui)* — Integrating Taiwanese heritage crafts with modern materials science.

## Latest Writing

{% assign latest_posts = site.posts | where: "lang", "en" | sort: "date" | reverse | slice: 0, 3 %}
{% if latest_posts.size > 0 %}
- {% for post in latest_posts %}[{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%b %d, %Y" }}{% endfor %}
{% else %}
- Essays in English are coming soon. Peek at the 中文版 for current notes.
{% endif %}

Explore the full archive on the [Blog](/blog/).

## Build Tracks

- **Research** — [Research portfolio](/research/) with papers, slides, and poster downloads.
- **Projects** — [Projects library](/projects/) covering SaaS prototypes, e-commerce sprints, and community builds.
- **Art** — [Art collaborations](/art/) with galleries, media features, and behind-the-scenes notes.
- **Trading Log** — [Market experiments](/trading-log/) documenting decision rules and debriefs.

## Work Together

- Advising founders on bio-related GTM, cross-border commerce, and narrative design.
- Speaking on synthetic biology innovation, disaster-tech, and creative entrepreneurship.
- Collaborations that blend data, policy, and art installations.

Reach me at [tomnandy922@gmail.com](mailto:tomnandy922@gmail.com) or connect via [LinkedIn](https://www.linkedin.com/in/jeff-zhuang-b45117316).
