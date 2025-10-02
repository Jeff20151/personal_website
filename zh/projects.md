---
layout: page
title: "專案"
description: "以旋轉展示呈現產品實驗、SaaS 原型與跨境商務衝刺。"
permalink: /zh/projects/
lang: zh
alt_url: /projects/
---

<section class="projects-hero">
  <p>專案軌道記錄我如何把研究、商務與敘事交織在一起。點擊卡片讓它移到正中央，再點一次就能進入案例頁面。</p>
</section>

<section class="carousel-section">
  <h2>精選作品</h2>
  <p class="lead">第一次點擊切換前景，第二次點擊即可查看完整介紹。</p>
  <div class="orbit-carousel" data-carousel data-radius="420">
    <button class="orbit-control prev" type="button" aria-label="上一個專案" data-action="prev">
      <svg viewBox="0 0 24 24"><path d="M14.5 5.5L8.5 12l6 6.5"/></svg>
    </button>
    <div class="orbit-ring">
      <a class="orbit-card is-active" href="{{ '/zh/projects/presenterai/' | relative_url }}" data-index="0">
        <img src="{{ '/assets/img/avatar.jpg' | relative_url }}" alt="PresenterAI 專案示意">
        <div class="orbit-meta">
          <strong>PresenterAI</strong>
          <span>把研究成果轉成具故事力的簡報。</span>
        </div>
      </a>
      <a class="orbit-card" href="{{ '/zh/projects/shihui/' | relative_url }}" data-index="1">
        <img src="{{ '/assets/img/avatar.jpg' | relative_url }}" alt="市檜專案照片">
        <div class="orbit-meta">
          <strong>市檜 — Shihui</strong>
          <span>將台灣工藝與永續材料結合的品牌實驗。</span>
        </div>
      </a>
      <a class="orbit-card" href="{{ '/zh/projects/night-market/' | relative_url }}" data-index="2">
        <img src="{{ '/assets/img/avatar.jpg' | relative_url }}" alt="夜市套裝專案照片">
        <div class="orbit-meta">
          <strong>Night Market Capsule</strong>
          <span>把夜市文化輸出海外的跨境體驗。</span>
        </div>
      </a>
    </div>
    <button class="orbit-control next" type="button" aria-label="下一個專案" data-action="next">
      <svg viewBox="0 0 24 24"><path d="M9.5 5.5L15.5 12l-6 6.5"/></svg>
    </button>
  </div>
</section>

<section class="projects-grid">
  <h2>案例庫</h2>
  <p class="lead">更多案例撰寫中，如需完整資料歡迎與我聯絡。</p>
  <ul>
    <li><a href="{{ '/zh/projects/presenterai/' | relative_url }}">PresenterAI — 讓研究簡報具備說服力的生成式工具。</a></li>
    <li><a href="{{ '/zh/projects/shihui/' | relative_url }}">市檜 Shihui — 以材料科學重啟傳統工藝供應鏈。</a></li>
    <li><a href="{{ '/zh/projects/night-market/' | relative_url }}">Night Market Capsule — 台灣飲食文化的跨境體驗套組。</a></li>
  </ul>
</section>
