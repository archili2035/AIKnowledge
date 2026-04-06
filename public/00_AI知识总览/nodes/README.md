# nodes 目录说明

这个目录用于承载 AI 知识图谱的**节点详情层**。

它和 `../overview.json` 的分工不同：

- `overview.json` 负责“总览主树”，回答“版图怎么分”。
- `nodes/` 负责“对象条目”，回答“某个概念 / 模型 / 产品到底是什么”。

## 当前建议的目录分法

- `concepts/`：概念，例如 Agent、RAG、Transformer
- `models/`：模型，例如 Claude、GPT、Gemini
- `products/`：产品 / 平台，例如 WorkBuddy、Cursor、ChatGPT
- `scenarios/`：场景 / 工作流，例如 游戏制作与AI
- `companies/`：公司，例如 Anthropic、OpenAI、腾讯
- `themes/`：议题 / 方法论，例如 高质量数据、评估、网络效应

## 命名建议

- 文件名用英文小写或 kebab-case，便于后续被 JSON/HTML 稳定引用
- front matter 中必须包含唯一 `id`
- 对外展示标题放在 `title`

## 推荐的条目结构

1. front matter：记录结构化元数据
2. `## 是什么`
3. `## 归类`
4. `## 为什么重要 / 解决什么问题`
5. `## 观察与判断`
6. `## 来源`
7. `## 相关条目`

## 现阶段原则

- **事实和观察分开写**
- **能给来源的尽量给来源**
- **先保证可维护，再追求一次性补全**

## 当前已创建的样例

当前已覆盖模型、产品、概念、公司、主题与场景等多类正式版节点，代表性样例如下：

- `models/claude.md`
- `models/gpt.md`
- `models/gemini.md`
- `models/qwen.md`
- `models/deepseek.md`
- `products/chatgpt.md`
- `products/google-ai.md`
- `products/claude-code.md`
- `products/codebuddy.md`
- `products/workbuddy.md`
- `products/manus.md`
- `products/midjourney.md`
- `concepts/agent.md`
- `concepts/rag.md`
- `concepts/transformer.md`
- `concepts/deep-learning.md`
- `concepts/reinforcement-learning.md`
- `themes/high-quality-data.md`
- `themes/static-dynamic-eval.md`
- `themes/goodhart-law.md`
- `themes/metcalfe-law.md`
- `companies/anthropic.md`
- `companies/openai.md`
- `companies/google.md`
- `companies/tencent.md`
- `companies/bytedance.md`
- `scenarios/game-production.md`
- `TEMPLATE.md`


