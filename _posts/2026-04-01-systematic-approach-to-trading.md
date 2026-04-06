---
layout: post
title: "A Researcher's Approach to Systematic Trading"
description: "How I apply research methodology to build and evaluate trading strategies."
date: 2026-04-01
lang: en
category: Trade
tags: [trading, finance]
---

Most retail traders lose money. The statistics are well-documented: roughly 70-80% of day traders end up net negative over any meaningful time horizon. Having spent years in research, I find the reason obvious. Most traders do not treat trading as a system to be designed, tested, and evaluated. They treat it as a series of intuitions to be acted on.

Here is how I approach it differently.

## Start With a Hypothesis, Not a Hunch

Every trade I consider starts with a clearly stated hypothesis: "If condition X holds, then asset Y will move in direction Z within timeframe T." This is no different from writing a research proposal. The hypothesis must be specific enough to be falsifiable. "I think the market will go up" is not a hypothesis. "Mean reversion in SPY after a 2-standard-deviation intraday drop completes within 3 trading days" is one.

## Backtest Honestly

Backtesting is the trading equivalent of running experiments on historical data. The key word is "honestly." Overfitting is just as dangerous here as it is in machine learning. I follow a few rules:

- **Out-of-sample testing is mandatory.** If a strategy was developed on 2020-2024 data, it must be validated on 2025-2026 data before any capital is allocated.
- **Account for transaction costs.** A strategy that returns 0.1% per trade looks great until you subtract the spread, commissions, and slippage.
- **Beware of survivorship bias.** If your universe of stocks only includes companies that exist today, you are implicitly excluding the ones that went bankrupt, which were probably the ones your "short the weakest" strategy would have traded.

## Position Sizing Matters More Than Entry Signals

Beginners obsess over when to enter a trade. Experienced systematic traders know that position sizing and risk management determine long-term survival. I use a simple framework: no single position can risk more than 1% of total capital, and correlated positions count together. This means my worst-case drawdown in any single event is bounded, regardless of how wrong my directional bet is.

## Keep a Trading Journal

Every trade gets logged: the hypothesis, the entry and exit conditions, the actual result, and a brief post-mortem. Over time, this journal becomes the most valuable dataset I have. It reveals patterns in my own behavior that no backtest can capture: which types of setups I overtrade, when I deviate from my rules, and which market conditions make me emotionally reactive.

## The Parallels to Research

Trading and research share a core discipline: respect for evidence over narrative. In both domains, the biggest risk is confirmation bias, seeing what you want to see in the data rather than what is actually there. The antidote is the same: rigorous methodology, honest evaluation, and the humility to update your beliefs when the evidence says you are wrong.
