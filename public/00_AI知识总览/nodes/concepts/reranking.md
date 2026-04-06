---
id: reranking
title: Reranking
type: concept
category: 关键概念 / 学术抓手
provider: Cohere
status: active
visibility: public
confidence: medium
updated: 2026-04-06
tags:
  - 重排
  - 检索
  - RAG
sources:
  - name: Cohere Rerank
    url: https://docs.cohere.com/docs/rerank
related:
  - retrieval
  - rag
---

## 是什么
Reranking 指系统先完成一轮粗召回，再对候选结果做二次排序，作用是把最相关的文档尽量推到前面，减少“召回到了但排位不对”的问题。

## 来源
- Cohere 官方文档《Rerank》

## 相关条目
- [[retrieval]]
- [[rag]]
