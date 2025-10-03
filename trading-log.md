---
layout: page
title: "Trading Log"
description: "Structured reflections on market experiments and revenue sprints."
permalink: /trading-log/
lang: en
alt_url: /zh/trading-log/
---

<div class="page-body">
  <p>Every entry here is a first-principles audit of an automated trade: the hypothesis, the data plumbing, the execution script, and the post-trade decision loop. Each log ships with runnable code so you can trace the exact mechanics.</p>

  <h2>Systems Under Observation</h2>
  <ul>
    <li><strong>Policy × Position Loop</strong> — Daily linkage between macro signals and position sizing; nothing is assumed without a data citation.</li>
    <li><strong>Automation Stack</strong> — Python agents syncing broker ledgers (Sinopac Shioaji) into internal dashboards for reconciliation and risk triggers.</li>
  </ul>

  <p>Expect each update to read like a lab note: explicit assumptions, instrumented code, and the product decisions the trade unlocks.</p>
</div>
