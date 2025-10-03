---
layout: page
title: "Trading Log"
description: "Market experiments, strategy iterations, and cash flow tests."
permalink: /trading-log/
lang: en
alt_url: /zh/trading-log/
---

<div class="page-body">
  <p>First-principles experiments on automated trading: hypothesis, data pipeline, code execution, and post-trade review, with explanations on how results feed back into product decisions. Every article includes executable code.</p>

  <h2>Current Focus Areas</h2>
  <ul>
    <li><strong>Market Journal</strong> — Daily conversion of policy signals into position management strategies.</li>
    <li><strong>Trading Automation</strong> — Using Sinopac Shioaji API and Python to sync broker data into internal risk systems.</li>
  </ul>

  <p>All updates are structured like lab notes: clear assumptions, code, and review conclusions.</p>

  <h2>Recent Entries</h2>

  <article class="trading-entry">
    <div class="entry-header">
      <h3><a href="/2025/10/03/shioaji-login/" class="entry-title-link">Auto Trading? Try Sinopac Shioaji</a></h3>
      <div class="entry-meta">
        <time>Oct 03, 2025</time> • <span class="tags">#trading-log #automation</span>
      </div>
    </div>
    <p class="entry-excerpt">Before any strategy touches money, I prove that the brokerage login flow is deterministic. For Sinopac's Shioaji API, that means respecting the token handshake documented in their guide. Here is the minimal, testable setup I deploy before a single order fires.</p>
    <a href="/2025/10/03/shioaji-login/" class="read-more-btn">→ Read Full Article</a>
  </article>
</div>
