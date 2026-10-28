---
id: reward-model
title: Reward Model
type: concept
category: 关键概念 / 学术抓手
provider:
status: active
visibility: public
confidence: high
updated: 2026-04-06
tags:
  - 奖励模型
  - 偏好学习
  - 后训练
sources:
  - name: Training Language Models to Follow Instructions with Human Feedback
    url: https://arxiv.org/abs/2203.02155
related:
  - post-training
  - rlhf
---

## 是什么
Reward Model 是一个专门学“哪种回答更符合人类偏好”的评分器，作用是给模型候选输出打分，后面再用这些分数继续优化模型行为。

## 来源
- InstructGPT 原始论文《Training Language Models to Follow Instructions with Human Feedback》

## 相关条目
- [[post-training]]
- [[rlhf]]
