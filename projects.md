---
layout: page
title: "Projects"
description: "A revolving showcase of product experiments, SaaS prototypes, and commerce sprints."
permalink: /projects/
lang: en
alt_url: /zh/projects/
---

<section class="projects-hero">
  <p>The projects orbit is where I test how research, commerce, and storytelling reinforce one another. Rotate through the current demos — the front card opens a detailed case study.</p>
</section>

<section class="carousel-section">
  <h2>Featured Works</h2>
  <p class="lead">Click a tile to bring it to the front; click again to open the full write-up.</p>
  <div class="orbit-carousel" data-carousel data-radius="420">
    <button class="orbit-control prev" type="button" aria-label="Previous project" data-action="prev">
      <svg viewBox="0 0 24 24"><path d="M14.5 5.5L8.5 12l6 6.5"/></svg>
    </button>
    <div class="orbit-ring">
      <a class="orbit-card is-active" href="{{ '/projects/presenterai/' | relative_url }}" data-index="0">
        <img src="{{ '/assets/img/avatar.jpg' | relative_url }}" alt="PresenterAI screenshot">
        <div class="orbit-meta">
          <strong>PresenterAI</strong>
          <span>Generative decks for lab-to-market storytelling.</span>
        </div>
      </a>
      <a class="orbit-card" href="{{ '/projects/shihui/' | relative_url }}" data-index="1">
        <img src="{{ '/assets/img/avatar.jpg' | relative_url }}" alt="市檜 Shihui project photo">
        <div class="orbit-meta">
          <strong>市檜 · Shihui</strong>
          <span>Taiwanese craft + sustainable biomaterials.</span>
        </div>
      </a>
      <a class="orbit-card" href="{{ '/projects/night-market/' | relative_url }}" data-index="2">
        <img src="{{ '/assets/img/avatar.jpg' | relative_url }}" alt="Night Market Capsule photograph">
        <div class="orbit-meta">
          <strong>Night Market Capsule</strong>
          <span>Cross-border tasting kits with full-funnel analytics.</span>
        </div>
      </a>
    </div>
    <button class="orbit-control next" type="button" aria-label="Next project" data-action="next">
      <svg viewBox="0 0 24 24"><path d="M9.5 5.5L15.5 12l-6 6.5"/></svg>
    </button>
  </div>
</section>

<section class="projects-grid">
  <h2>Case Study Library</h2>
  <p class="lead">More write-ups are in flight — reach out if you want a private walkthrough.</p>
  <ul>
    <li><a href="{{ '/projects/presenterai/' | relative_url }}">PresenterAI — turning research briefs into persuasive decks.</a></li>
    <li><a href="{{ '/projects/shihui/' | relative_url }}">市檜 (Shihui) — restoring craft supply chains with material science.</a></li>
    <li><a href="{{ '/projects/night-market/' | relative_url }}">Night Market Capsule — global distribution for Taiwanese food rituals.</a></li>
  </ul>
</section>
