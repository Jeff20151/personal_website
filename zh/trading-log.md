---
layout: page
title: "交易日誌"
description: "記錄市場實驗、策略迭代與現金流測試。"
permalink: /zh/trading-log/
lang: zh
alt_url: /trading-log/
---

<div class="page-body">
  <p>這裡記錄每次自動化交易的第一性原理實驗：假設、資料管線、程式碼與事後檢討，並說明這些結果如何反饋到產品決策。每篇文章都會附上可執行 code。</p>

  <h2>目前追蹤主題</h2>
  <ul>
    <li><strong>市場日誌</strong> —— 每天把政策訊號轉換成部位控管策略。</li>
    <li><strong>自動化交易</strong> —— 使用 Sinopac Shioaji API 與 Python 將券商資料同步到內部風險系統。</li>
  </ul>

  <p>所有更新都會像實驗室筆記：清楚列出假設、程式與復盤結論。</p>

  <h2>最新紀錄</h2>

  <article class="trading-entry">
    <div class="entry-header">
      <h3><a href="/zh/2025/10/03/shioaji-login/" class="entry-title-link">想學自動化交易？試試 Sinopac Shioaji</a></h3>
      <div class="entry-meta">
        <time>2025年10月3日</time> • <span class="tags">#交易日誌 #自動化</span>
      </div>
    </div>
    <p class="entry-excerpt">在任何策略進場之前，我先確認券商 API 的登入流程是可重現的。以永豐金 Shioaji 為例，核心是他們在文件裡揭露的 Token 驗證。下面是我在自動化交易前必做的流程，確保系統在未獲得簽署帳號時就停止。</p>
    <a href="/zh/2025/10/03/shioaji-login/" class="read-more-btn">→ 閱讀完整文章</a>
  </article>
</div>
