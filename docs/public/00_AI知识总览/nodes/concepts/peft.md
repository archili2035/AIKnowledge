---
id: peft
title: PEFT
type: concept
category: 关键概念 / 学术抓手
provider:
status: active
visibility: public
confidence: medium
updated: 2026-04-06
tags:
  - PEFT
  - 参数高效微调
  - 微调
sources:
  - name: LoRA: Low-Rank Adaptation of Large Language Models
    url: https://arxiv.org/abs/2106.09685
related:
  - fine-tuning
  - lora
---

## 是什么
PEFT（Parameter-Efficient Fine-Tuning，参数高效微调）是一类只更新很少一部分参数就完成模型适配的方法，作用是降低显存、训练和部署成本。

## 来源
- LoRA 原始论文《LoRA: Low-Rank Adaptation of Large Language Models》

## 相关条目
- [[fine-tuning]]
- [[lora]]
