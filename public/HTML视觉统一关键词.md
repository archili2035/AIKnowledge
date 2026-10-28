# HTML 视觉统一关键词（AIKnowledge）

> 适用范围：本仓库下所有 HTML 页面。
> 本文只讲本仓库怎么用，**样式本身不在这里维护**。

## 唯一真相源

样式来自 **site-kit**，与个人门户、健康档案共用同一套令牌：

- `assets/theme/tokens.css` — 设计令牌
- `assets/theme/base.css` — 重置、排版与组件原语
- 当前版本见 `portal.json` 的 `theme_version`

这两个文件由 site-kit 的 `sync-theme` 同步，**不要手改**。要调色、改字阶、改间距，
去改 site-kit 的 tokens.css，再同步回来。

> 本文此前内嵌过一份令牌（蓝紫渐变那套）。那种写法的问题是没有任何东西强制执行，
> 每个页面各自手抄一遍，于是必然漂移。现在令牌是真实文件，不再是文档里的代码块。

## 设计关键词

当前口径：**苹果官网的骨架 + 个人色**。

- 排版节奏与大留白，靠间距分区
- 双表面色带交替（`.band` / `.band-alt`），不靠边框堆叠
- 药丸按钮与状态标签
- 克制的阴影，层级优先用表面色差表达
- 赭石强调色、衬线标题、整体偏暖一度的表面色

明确**不再使用**：蓝紫渐变、作为装饰的渐变背景、厚重阴影。

## 页面怎么写

```html
<link rel="stylesheet" href="../../assets/theme/tokens.css">
<link rel="stylesheet" href="../../assets/theme/base.css">
...
<section class="band">
  <div class="page">
    <header class="hero">
      <span class="tag">public knowledge</span>
      <h1>标题</h1>
      <p class="lead">一句话定位</p>
    </header>
  </div>
</section>
```

相对路径按页面深度写（仓库根用 `assets/`，`public/xx/` 下用 `../../assets/`）。
相对引用在本地 `file://`、GitHub Pages、门户镜像三处都成立。

## 可用的组件词汇

`page` `page-reading` `page-wide` · `band` `band-alt` `band-inverse` `band-tight` ·
`hero` `tag` `lead` · `section` · `card` `grid` · `stats` `stat` ·
`timeline` `row` `date` · `pill`（`ok` `warn` `danger` `info` `accent`） ·
`button` `button-quiet` `links` · `alert` `warn` · `muted` `note` `mono` `micro`

## 三层约束

| 层 | 在哪 | 约束 |
|---|---|---|
| 一层 · 令牌 | `assets/theme/tokens.css` | 唯一真相源，页面不准写死色值与字号 |
| 二层 · 基础 | `assets/theme/base.css` | 只引用一层 |
| 三层 · 页面局部 | 各页 `<style>` | 自造组件允许保留，但**只能引用一层令牌** |

第三层是故意留的：长文页的 `glossary-block`、`flow-step`、`chain-item` 这类
自造组件不必被塞进统一组件集，共享令牌就足以统一观感。

页面局部样式写在 `<link>` 之后，因此同名类（`hero` `section` `tag` `card`）
会覆盖基础层——这是预期行为，但要留意只覆盖需要的属性。

## 迁移状态

| 页面 | 状态 |
|---|---|
| `index.html` | 已迁移 |
| `public/01_AI基础理论/一口气拆穿Skill／MCP／RAG／Agent／OpenClaw底层逻辑.html` | 已迁移（锚点页） |
| 其余 `public/**` 下的 HTML | 待迁移 |

迁移手法：插入两行 `<link>`，把页面原有的 `:root` 令牌块改为映射到 site-kit 令牌，
再把残留的写死色值按语义替换成令牌。组件规则本身基本不动。
