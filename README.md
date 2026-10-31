# AIKnowledge · AI 知识库

一个结构化的 AI 领域知识库，以「节点 + 关系」的方式组织概念、公司、模型、产品与场景，生成静态站点便于浏览与检索。

## 目录结构

- `docs/public/00_AI知识总览/` —— 知识库主体，含 `overview.json`（图数据）与 `nodes/` 下的分类节点：
  - `concepts/` —— 概念（Transformer、RAG、MCP、RLHF 等）
  - `companies/` —— 公司（OpenAI、Google、Anthropic、ByteDance、Tencent 等）
  - `models/` —— 模型（GPT、Claude、Gemini、DeepSeek、Qwen、Genie-3 等）
  - `products/` —— 产品（ChatGPT、Claude Code、Cursor、CodeBuddy、WorkBuddy、Manus、Midjourney 等）
  - `scenarios/` —— 应用场景
  - `themes/` —— 主题（Goodhart 定律、Metcalfe 定律等）
- `docs/aiknowledge_index.html` / `docs/index.html` —— 入口页
- `_legacy/` —— 历史归档

## 说明

节点以 Markdown 为主，页面遵循 `xavierstudio-site-kit` 统一视觉，引用 `docs/assets/theme/*.css`。
