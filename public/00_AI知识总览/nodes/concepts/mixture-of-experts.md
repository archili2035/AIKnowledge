---
id: mixture-of-experts
title: Mixture of Experts（MoE）
type: concept
category: 关键概念 / 学术抓手
provider:
status: active
visibility: public
confidence: medium
updated: 2026-04-06
tags:
  - MoE
  - 架构
  - 稀疏激活
sources:
  - name: Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer
    url: https://arxiv.org/abs/1701.06538
related:
  - transformer
  - qwen
  - deepseek
---

## 是什么
Mixture of Experts（MoE）是一种按需只激活少量“专家”子网络的模型架构，作用是在不让每次计算成本同比暴涨的情况下，继续扩大模型参数规模与能力。

## 来源
- 原始论文《Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer》

## 相关条目
- [[transformer]]
- [[qwen]]
- [[deepseek]]
