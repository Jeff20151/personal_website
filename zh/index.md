---
layout: landing
title: "莊詠旭 Jeff Chunag — 研究 × 產品 × 藝術"
description: "雙語個人網站，匯整研究專案、產品實驗與藝術合作。"
lang: zh
alt_url: /
keywords:
  - 莊詠旭
  - 生物設計
  - 新創
  - 投資
  - 跨領域
permalink: /zh/
---

# 新創 × 投資 × 藝術 × 研究

當人工智慧重塑勞動、基因編輯改寫生命藍圖，我相信單一職業框架已不足以回應這個世代的難題。於是我選擇把商業的速度、藝術的感知與研究的嚴謹交織在一起，持續尋找推動人類前進的答案。

---

## 我正在探索的主題

- **研究計畫** — 與台大生醫電子所合作，進行 **Spatial Transcriptomics 基因表現預測**，連結醫學影像與基因資訊。
- **新創公司** — 透過 **SaaS 快速迭代** 與 **跨境電商測試** 驗證市場需求，追求從 0 到 1 的產品突破。
- **藝術敘事** — 把 **數學與美學** 結合，讓抽象數據與政策議題化為可被感受的故事。

---

## 研究與產品亮點

- **蜘蛛絲蛋白序列生成** — 與 NTU BST 單位協作測試。
- **Spatial Transcriptomics 臨床試驗** — 與 NTU BEBI 醫療團隊進行場域實驗。
- **PresenterAI** — 將學術簡報轉化為面向大眾的 **生成式敘事工具**。
- **市檜（Shihui）** — 協助新手突破傳統框架的 **跨境電商 end-to-end app**。

---

## 最新文章

{% assign latest_posts_zh = site.posts | where: "lang", "zh" | sort: "date" | reverse | slice: 0, 3 %}
{% if latest_posts_zh.size > 0 %}
- {% for post in latest_posts_zh %}[{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%Y-%m-%d" }}{% endfor %}
{% else %}
- 英文版文章撰寫中，近期會同步更新。
{% endif %}

更多內容請見 [部落格](/zh/blog/)，每週一篇，紀錄生活、研究與創業的思考。

---

## 合作與交流

歡迎來信 [tomnandy922@gmail.com](mailto:tomnandy922@gmail.com) 或透過 [LinkedIn](https://www.linkedin.com/in/jeff-zhuang-b45117316) 聯繫。

🟣 每晚 20:00-22:00，我都在 [Twitch](https://www.twitch.tv/cooljeffchuang) 分享研究與創業日常。
