---
layout: landing
title: "莊詠旭 Jeff Chunag — 研究 × 產品 × 藝術"
description: "雙語個人網站，匯整研究專案、產品實驗與藝術合作。"
lang: zh
alt_url: /
permalink: /zh/
---

# 研究 × 產品 × 藝術

我把生醫電子研究、跨境商務與敘事設計結合起來，把實驗室的成果轉成市場與展覽裡可感知的作品。這裡紀錄我正在推進的研究議題、產品衝刺與藝術計畫。

## 目前主題

- **研究計畫** — 與台大生醫電子所合作的合成生物學、醫療偵測雛形。
- **產品實驗** — 快速迭代 SaaS、跨境電商漏斗，測試不同市場的需求。
- **文化敘事** — 透過展覽與裝置，把資料、政策議題轉化成能被感受到的故事。

## 研究亮點

- 《自適應生物感測器》 — 與 NTU BEBI 臨床單位共同進行場域測試。
- PresenterAI — 把研究簡報轉成面向大眾的生成式敘事工具。
- 市檜（Shihui） — 將台灣傳統工藝與材料科學結合的品牌計畫。

## 最新文章

{% assign latest_posts_zh = site.posts | where: "lang", "zh" | sort: "date" | reverse | slice: 0, 3 %}
{% if latest_posts_zh.size > 0 %}
- {% for post in latest_posts_zh %}[{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%Y-%m-%d" }}{% endfor %}
{% else %}
- 英文版文章撰寫中，近期會同步更新。
{% endif %}

完整文章清單請見 [部落格](/zh/blog/)。

## 發展路徑

- **研究** — [研究頁面](/zh/research/) 提供論文、投影片與海報下載。
- **專案** — [專案資料庫](/zh/projects/) 收錄 SaaS 原型、電商衝刺與社群活動。
- **藝術** — [藝術合作](/zh/art/) 展示畫廊合作、媒體露出與幕後紀錄。

## 合作邀請

- 顧問：協助生醫相關產品的 GTM、跨境電商成長、敘事設計。
- 演講：合成生物、災防科技、創意創業跨域合作。
- 共同創作：把資料、政策議題轉化為展覽與裝置。

歡迎來信 [tomnandy922@gmail.com](mailto:tomnandy922@gmail.com) 或在 [LinkedIn](https://www.linkedin.com/in/jeff-zhuang-b45117316) 與我聯繫。
