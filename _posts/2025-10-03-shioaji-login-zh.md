---
layout: trading-post
title: "想學自動化交易？試試 Sinopac Shioaji"
date: 2025-10-03
lang: zh
alt_url: /2025/10/03/shioaji-login/
tags: [交易日誌, 自動化]
permalink: /zh/2025/10/03/shioaji-login/
---

在任何策略進場之前，我先確認券商 API 的登入流程是可重現的。以永豐金 Shioaji 為例，核心是他們在文件裡揭露的 Token 驗證 (<https://sinotrade.github.io/zh/tutor/prepare/terms/>)。下面是我在自動化交易前必做的流程，確保系統在未獲得簽署帳號時就停止。

## 1. 先定義不可妥協的條件

- **目標**：3 秒內取得登入成功且所有帳號 `signed=True`。
- **輸入**：`api_key`、`secret_key`、機器時間與伺服器差 < 1 秒。
- **失敗條件**：Unsigned 帳號、timeout、商品檔下載失敗。

只要出現失敗條件，就不會進行任何下單流程。

## 2. 撰寫登入骨架

```python
import shioaji as sj
from datetime import datetime

TIMEOUT_MS = 30_000
api = sj.Shioaji()

accounts = api.login(
    api_key="YOUR_API_KEY",
    secret_key="YOUR_SECRET_KEY",
    fetch_contract=True,
    receive_window=TIMEOUT_MS,
)
assert all(getattr(acc, "signed", False) for acc in accounts), "Unsigned account detected"
print(f"Login OK @ {datetime.utcnow():%Y-%m-%d %H:%M:%S}Z")
```

**檢查點**

1. **時間同步**：若出現 `Sign data is timeout`，先校準電腦時間。
2. **商品檔 callback**：透過 `contracts_cb` 紀錄抓取到的標的，缺任何一類就表示交易宇宙不完整。
3. **委託/成交回報**：保留 `subscribe_trade=True`，讓所有成交即時回到風險系統。

## 3. 列出帳號並設定預設帳號

```python
fut_acc, stock_acc = api.futopt_account, api.stock_account
print("Futures:", fut_acc)
print("Stock:", stock_acc)
```

若沒有 `signed=True`，先完成永豐金 API 的簽署與測試流程，再繼續。

## 4. 快取商品檔

```python
api.fetch_contracts(timeout=0)
```

將商品檔 JSON 存在本地，下次啟動時可用 `fetch_contract=False` 加快速度，但契約換月時記得手動刷新。

## 5. 記得釋放連線

```python
api.logout()
```

---

**為什麼要這麼做？** 因為自動化交易的可靠性取決於最基本的假設。把登入視為一道不可跳過的檢查：token 正常、時間同步、帳號簽署完成，才能避免「在我電腦上可以」的風險。你可以直接套用這段程式碼，把金鑰填入，先驗證環境，再讓機器碰觸真實資金。

後續文章會陸續公開更多 code 範例與每日復盤筆記。
