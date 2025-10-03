---
layout: post
title: "Auto Trading? Try Sinopac Shioaji"
date: 2025-10-03
lang: en
alt_url: /zh/2025/10/03/shioaji-login/
tags: [trading-log, automation]
---

Before any strategy touches money, I prove that the brokerage login flow is deterministic. For Sinopac’s Shioaji API, that means respecting the token handshake documented in their guide (<https://sinotrade.github.io/zh/tutor/prepare/terms/>). Here is the minimal, testable setup I deploy before a single order fires.

## 1. Define the invariant

- **Objective**: authenticated session with signed accounts returned in under 3 seconds.
- **Inputs**: `api_key`, `secret_key`, clock drift < 1s.
- **Failure states**: unsigned accounts, timeout, stale contracts cache.

If any failure state occurs, no trades are executed; the automation pipeline stops here.

## 2. Write the login harness

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

**Checks**

1. **Time sync**: if you hit `Sign data is timeout`, sync the machine clock (I use NTP every launch).
2. **Contracts callback**: pass a lambda to `contracts_cb` and log the securities fetched; missing contracts = incomplete trading universe.
3. **Trade subscription**: keep `subscribe_trade=True` so fills stream into your risk monitor.

## 3. List accounts & set defaults

```python
fut_acc, stock_acc = api.futopt_account, api.stock_account
print("Futures:", fut_acc)
print("Stock:", stock_acc)
```

If any account prints without `signed=True`, stop and complete Sinopac’s paperwork before proceeding.

## 4. Cache the contracts

```python
api.fetch_contracts(timeout=0)
```

Store the contracts JSON locally so subsequent runs can boot faster (set `fetch_contract=False`), but invalidate the cache whenever Sinopac rolls a new contract month.

## 5. Wire clean exit

Always log out when the job ends to free connection slots:

```python
api.logout()
```

---

**Why this matters**: every automated trade is only as trustworthy as the assumptions under it. By treating the login flow as an invariant—token, time sync, signed accounts—we eliminate a whole class of “it worked on my laptop” failures. Fork the snippet, drop in your keys, and prove your setup passes before you let the bot touch live capital.

Code repo + nightly automation notes will follow in upcoming entries.
