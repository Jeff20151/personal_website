---
layout: post
title: "Open-Source Tools That Changed My Research Workflow"
description: "A curated list of open-source tools that have significantly improved my productivity as a biomedical researcher."
date: 2026-03-31
lang: en
category: Open Source Tools
tags: [open-source, tools]
---

Research is often bottlenecked not by ideas but by tooling. Over the past few years, I have assembled a set of open-source tools that have measurably improved my workflow. None of these are obscure; most are well-known in their respective communities. But I have found that many researchers, especially in biology, are not aware of them. Here are the ones I use most.

## Scanpy: Single-Cell and Spatial Analysis in Python

If you work with single-cell or spatial transcriptomics data, Scanpy is indispensable. It provides a complete pipeline from raw count matrices to clustering, trajectory analysis, and visualization, all in Python. The AnnData format it uses has become the de facto standard for storing annotated expression data. I use it daily for preprocessing, quality control, and exploratory analysis.

**Why it matters:** It replaces a fragmented workflow of R packages and custom scripts with a single, well-documented, GPU-acceleratable framework.

## Weights & Biases: Experiment Tracking

Training deep learning models involves hundreds of experiments with different hyperparameters, architectures, and data splits. Weights & Biases (wandb) tracks all of this automatically. Every training run logs its config, metrics, and artifacts to a central dashboard. Months later, I can look up exactly which settings produced a particular result.

**Why it matters:** Reproducibility. Without systematic experiment tracking, it is nearly impossible to reconstruct why one model outperformed another.

## Zotero: Reference Management

Zotero is a free, open-source reference manager that stores papers, extracts metadata, and generates citations in any format. With the browser extension, saving a paper is a single click. I organize papers by project and tag them by topic. The Zotero-to-Markdown export workflow also integrates cleanly with my note-taking system.

**Why it matters:** A researcher who cannot efficiently find and cite prior work is wasting hours every week.

## Quarto: Reproducible Documents

Quarto is the successor to R Markdown, but it supports Python, Julia, and Observable JS as well. I use it to write analysis reports that interleave code, figures, and narrative text. The output can be HTML, PDF, or even a presentation. When a reviewer asks "how did you generate Figure 3?", the answer is in the document itself.

**Why it matters:** It closes the gap between analysis and communication, making results inherently reproducible.

## Ollama: Local LLM Inference

Running large language models locally has become practical thanks to quantization and efficient inference engines. Ollama makes it trivially easy to pull and run models like Llama, Mistral, or Phi on a laptop. I use it for literature summarization, code generation, and brainstorming, all without sending data to an external API.

**Why it matters:** Data privacy matters in biomedical research. Local inference means sensitive data never leaves your machine.

## The Common Thread

What these tools share is that they reduce friction. They take tasks that used to require manual effort, institutional licenses, or proprietary software and make them accessible, reproducible, and free. The best tool is the one you actually use consistently, and open-source tools win on that metric because the barrier to adoption is zero.
