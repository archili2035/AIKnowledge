---
id: static-dynamic-eval
title: 静态/动态评估
type: theme
category: 核心热点 / 方法论
provider:
status: active
visibility: public
confidence: medium
updated: 2026-04-06
tags:
  - 评估
  - 方法论
  - Benchmark
  - Agent
sources:
  - name: 公开 AI 评估方法资料
related:
  - high-quality-data
  - goodhart-law
  - agent
---

## 是什么
静态/动态评估可以先理解为两种不同的看法：静态评估更像固定题库、固定答案的测验；动态评估更像把模型放进任务流程里，看它在真实环境中会不会做、敢不敢做、能不能做完。

## 归类
它属于“评估方法论”，和具体模型、产品名称不同。前者回答“怎么判断强弱”，后者回答“到底是什么对象”。

## 为什么重要
随着产品逐渐从“会说”走向“能做”，只看静态题库越来越不够。尤其是 Agent 场景，更需要动态地看规划、调用工具、纠错和收尾能力。

## 观察与判断
这不是说静态评估没用了，而是它更适合做基线。真正进入工作流时，还要补动态评估，否则很容易出现榜单很好看、实际体验却不稳定的落差。

## 来源
- 公开 AI 评估方法资料
- 后续可继续补基准测试、任务评测和 Agent 评估框架

## 相关条目
- [[high-quality-data]]
- [[goodhart-law]]
- [[agent]]
