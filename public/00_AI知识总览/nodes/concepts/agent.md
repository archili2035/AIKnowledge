---
id: agent
title: Agent
type: concept
category: 关键概念
provider: 
status: active
visibility: public
confidence: medium
updated: 2026-04-05
tags:
  - 概念
  - Agent
  - 工具调用
  - 执行闭环
sources:
  - name: Anthropic Building Effective Agents
    url: https://www.anthropic.com/engineering/building-effective-agents
related:
  - claude
  - workbuddy
  - game-production
---

## 是什么
Agent 可以理解为：系统不只负责回答问题，还会围绕目标进行任务分解、调用工具、接收反馈并继续推进。

## 归类
它属于“执行编排”这一层，不应直接和模型、协议、产品封装当成同一层概念。

## 为什么重要
很多用户真正感知到的“AI 会做事了”，本质上都离不开 Agent 式的多步执行能力。

## 观察与判断
在知识图谱里，Agent 很适合作为一个中枢节点：它会同时连向模型、工具、场景和产品，因此后续很可能是横向关系最多的概念之一。

## 来源
- Anthropic 关于 Agent 的工程文章
- 后续可继续补平台型 Agent 文档与案例

## 相关条目
- [[claude]]
- [[workbuddy]]
- [[game-production]]
