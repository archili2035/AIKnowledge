---
id: rag
title: RAG
type: concept
category: 关键概念
provider: 
status: active
visibility: public
confidence: medium
updated: 2026-04-05
tags:
  - 概念
  - 检索增强生成
  - 外部知识
sources:
  - name: Lewis et al. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
    url: https://arxiv.org/abs/2005.11401
related:
  - agent
---

## 是什么
RAG 可以先理解为：让模型在回答前先去拿外部资料，再基于这些资料生成结果，而不是只依赖参数里已经记住的内容。

## 归类
它属于“知识获取与生成结合”的方法层，不是单独一种模型，也不是等同于 Agent。

## 为什么重要
当问题依赖最新信息、私有资料或长尾知识时，只靠模型记忆往往不够，RAG 就成了把外部知识接进来的一种常见办法。

## 观察与判断
在知识图谱里，RAG 适合作为一个中间概念：它一头连向知识库、搜索、向量检索，另一头又经常和 Agent 组合出现。

## 来源
- RAG 原始论文
- 后续可继续补工程化实现与检索链路资料

## 相关条目
- [[agent]]
