# Awesome Vibe Coding 🪄

> 一份精选的 Vibe Coding（氛围编程）开源项目合集 —— 从 AI 编码助手、Agent 框架、MCP 生态，
> 到 **AI 硬件 / 边缘 AI / 机器人**，全部收录 **Star ≥ 100** 的项目，按分类与 Star 数排序。

![repos](https://img.shields.io/badge/收录项目-283-blue) ![stars](https://img.shields.io/badge/累计Star-8.4M-orange) ![license](https://img.shields.io/badge/license-CC0--1.0-lightgrey) ![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen)

---

## 什么是 Vibe Coding

> 「有一种新的编程方式，我称之为 vibe coding：你完全沉浸在氛围里，拥抱指数级的变化，
> 甚至忘记代码本身的存在。我在构建一个项目或网页应用，但这其实不太算写代码 ——
> 我只是看到东西、说出想法、运行一下、复制粘贴，然后它多半就能跑起来。」
>
> —— **Andrej Karpathy**（OpenAI 创始成员），2025 年初

在传统编程里，人是**作者**；在 vibe coding 里，人是**导演**。你用自然语言描述想要什么，
让 AI Agent 负责实现细节。这份清单收录的就是支撑这套工作流的整个生态。

## 收录标准

- **Star ≥ 100**：低于 100 star 的项目不收录，避免清单被玩具项目淹没。
- **与 vibe coding 强相关**：AI 编码工具、Agent、MCP、上下文工程、AI 硬件等。
- **按分类 + Star 数排序**：每个分类内按 Star 从高到低排列。
- 数据通过 GitHub API 自动采集，采集脚本见 [`scripts/collect.py`](scripts/collect.py)，原始数据见 [`data/repos.json`](data/repos.json)。

> 数据快照时间：**2026-09-10**。Star 数会随时间变化，欢迎提交 PR 更新。

---

## 目录

- [🤖 AI 编程助手与 IDE 插件](#ai-编程助手与-ide-插件) — 14 个项目
- [🖥️ AI IDE 与代码编辑器](#ai-ide-与代码编辑器) — 10 个项目
- [⌨️ 终端与 CLI 编码 Agent](#终端与-cli-编码-agent) — 25 个项目
- [🌐 Prompt-to-App 全栈应用生成](#prompt-to-app-全栈应用生成) — 21 个项目
- [🧩 Agent 框架与多智能体编排](#agent-框架与多智能体编排) — 24 个项目
- [🔌 MCP 生态 Model Context Protocol](#mcp-生态-model-context-protocol) — 29 个项目
- [🧠 上下文工程 规范驱动 Skills 与记忆](#上下文工程-规范驱动-skills-与记忆) — 31 个项目
- [🔍 代码审查 测试与安全](#代码审查-测试与安全) — 12 个项目
- [🎨 AI 设计与 UI 生成](#ai-设计与-ui-生成) — 12 个项目
- [🔧 硬件 边缘 AI 与机器人](#硬件-边缘-ai-与机器人) — 51 个项目
- [⚙️ 本地模型与自托管](#本地模型与自托管) — 19 个项目
- [📚 学习资源 教程与 Awesome 列表](#学习资源-教程与-awesome-列表) — 35 个项目
- [统计概览](#统计概览)
- [如何挑选工具](#如何挑选工具)
- [贡献指南](#贡献指南)
- [License](#license)

---

## AI 编程助手与 IDE 插件

> 🤖 装进编辑器里的 AI 结对程序员，负责补全、改代码、跑任务。
>
> *AI Coding Assistants & Plugins*

| 项目 | 简介 | ⭐ Star | 语言 |
|:---|:---|---:|:---|
|**[小米遥控器竟然是Vibe Coding神器](https://www.bilibili.com/video/BV1FFYp6jEFf/)** |60块的小米遥控器竟然是Vibe Coding神器|666|TypeScript|
| **[cline/cline](https://github.com/cline/cline)** | 自主编码 Agent，可作为 SDK、IDE 插件或 CLI 使用，能读文件、跑命令、改代码。 | 67.7k | TypeScript |
| **[continuedev/continue](https://github.com/continuedev/continue)** | 开源编码 Agent，支持 VS Code / JetBrains，可接任意模型。 | 35.9k | TypeScript |
| **[TabbyML/tabby](https://github.com/TabbyML/tabby)** | 可自托管的 AI 编码助手，主打隐私与本地部署。 | 33.9k | Rust |
| **[VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents)** | 100+ 专业 Claude Code 子代理合集。 | 25.0k | Shell |
| **[RooCodeInc/Roo-Code](https://github.com/RooCodeInc/Roo-Code)** | 在编辑器里给你一整支 AI 开发团队，Cline 的功能增强分支。 | 24.3k | TypeScript |
| **[mksglu/context-mode](https://github.com/mksglu/context-mode)** | 为 AI 编码 Agent 做上下文窗口优化，把工具输出放进沙箱。 | 21.8k | TypeScript |
| **[avante-corp/avante.nvim](https://github.com/avante-corp/avante.nvim)** | 让 Neovim 用上类 Cursor 的 AI 编程体验，建议可直接落到源文件。 | 18.2k | Lua |
| **[github/CopilotForXcode](https://github.com/github/CopilotForXcode)** | GitHub 官方为 Xcode 打造的 AI 编码助手。 | 6.3k | Swift |
| **[Zoo-Code-Org/Zoo-Code](https://github.com/Zoo-Code-Org/Zoo-Code)** | 编辑器内多 Agent 协作的编码助手。 | 1.8k | TypeScript |
| **[callstackincubator/agent-skills](https://github.com/callstackincubator/agent-skills)** | 面向 React Native 的 Agent 技能包。 | 1.6k | Shell |
| **[tddworks/ClaudeBar](https://github.com/tddworks/ClaudeBar)** | macOS 菜单栏工具，实时监控各家 AI 编码助手的用量与额度。 | 1.5k | Swift |
| **[editor-code-assistant/eca](https://github.com/editor-code-assistant/eca)** | 编辑器无关的 AI 结对编程助手，Emacs 等编辑器也能用。 | 990 | Clojure |
| **[MicrosoftDocs/Agent-Skills](https://github.com/MicrosoftDocs/Agent-Skills)** | 微软 / Azure 官方整理的 Agent Skills 合集。 | 738 | — |
| **[bawadou/ai-data-extractor](https://github.com/bawadou/ai-data-extractor)** | 从各家 AI 编码助手导出聊天记录的开源工具。 | 555 | Python |

<sub>共 14 个项目 · [回到目录](#目录)</sub>

---

## AI IDE 与代码编辑器

> 🖥️ 以 AI 为核心重新设计的编辑器与开发环境。
>
> *AI IDEs & Code Editors*

| 项目 | 简介 | ⭐ Star | 语言 |
|:---|:---|---:|:---|
| **[zed-industries/zed](https://github.com/zed-industries/zed)** | 高性能多人协作编辑器，原生集成 AI 能力。 | 90.0k | Rust |
| **[stablyai/orca](https://github.com/stablyai/orca)** | 面向并行 Agent 舰队的 ADE（Agent 开发环境），可同时跑多个编码 Agent。 | 65.2k | TypeScript |
| **[can1357/oh-my-pi](https://github.com/can1357/oh-my-pi)** | 把 IDE 直接接线进来的编码 Agent。 | 30.4k | TypeScript |
| **[voideditor/void](https://github.com/voideditor/void)** | 开源 AI 代码编辑器，常被视为 Cursor 的开源替代。 | 28.8k | TypeScript |
| **[superset-sh/superset](https://github.com/superset-sh/superset)** | agentic IDE，可并行编排 100+ 编码 Agent。 | 14.0k | TypeScript |
| **[athasdev/athas](https://github.com/athasdev/athas)** | 基于 Tauri（Rust + React）的轻量跨平台代码编辑器。 | 3.1k | TypeScript |
| **[0-AI-UG/cate](https://github.com/0-AI-UG/cate)** | 可无限缩放的编码画布，编辑器、终端、浏览器同屏。 | 2.1k | TypeScript |
| **[hanshuaikang/nezha](https://github.com/hanshuaikang/nezha)** | 面向 AI Agent 时代的代码编辑器，可在本机并行跑多个 Claude Code / Codex。 | 1.9k | TypeScript |
| **[we0-dev/we0](https://github.com/we0-dev/we0)** | 面向开发者与产品经理的 AI 代码编辑器。 | 925 | TypeScript |
| **[JetBrains/thinkrail](https://github.com/JetBrains/thinkrail)** | JetBrains 出品的轻量真实 IDE，主打 vibe coding 体验。 | 436 | TypeScript |

<sub>共 10 个项目 · [回到目录](#目录)</sub>

---

## 终端与 CLI 编码 Agent

> ⌨️ 跑在命令行里的编码智能体，最适合「描述需求 → 看它干活」的工作流。
>
> *Terminal & CLI Coding Agents*

| 项目 | 简介 | ⭐ Star | 语言 |
|:---|:---|---:|:---|
| **[anomalyco/opencode](https://github.com/anomalyco/opencode)** | 开源编码 Agent，主打终端体验。 | 206k | TypeScript |
| **[anthropics/claude-code](https://github.com/anthropics/claude-code)** | Anthropic 官方终端编码 Agent，理解代码库、执行任务、管理 git，全程自然语言。 | 145k | Python |
| **[farion1231/cc-switch](https://github.com/farion1231/cc-switch)** | 跨平台一键切换 Claude Code / Codex 账号与配置的桌面助手。 | 132k | Rust |
| **[openai/codex](https://github.com/openai/codex)** | OpenAI 的轻量级终端编码 Agent。 | 123k | Rust |
| **[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)** | Google 开源终端 AI Agent，把 Gemini 直接带进命令行。 | 107k | TypeScript |
| **[Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)** | 让 Claude Code / Codex / OpenCode 等免费用（自带免费额度池）。 | 54.2k | Python |
| **[aaif-goose/goose](https://github.com/aaif-goose/goose)** | 可扩展的本地 AI Agent，支持任意 LLM 与 MCP 扩展。 | 54.1k | Rust |
| **[Aider-AI/aider](https://github.com/Aider-AI/aider)** | 终端里的 AI 结对编程工具，直接改写你本地的 git 仓库。 | 48.9k | Python |
| **[Hmbown/Codewhale](https://github.com/Hmbown/Codewhale)** | Rust 编写的开源终端编码 Agent。 | 40.9k | Rust |
| **[herdrdev/herdr](https://github.com/herdrdev/herdr)** | 编码 Agent 的运行时底座。 | 37.1k | Rust |
| **[esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix)** | 面向 DeepSeek 的终端编码 Agent。 | 35.5k | Go |
| **[iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)** | 24/7 常驻的多 Agent 协作桌面应用。 | 32.7k | TypeScript |
| **[charmbracelet/crush](https://github.com/charmbracelet/crush)** | Charm 出品的终端 AI 编码 Agent，界面精致。 | 28.0k | Go |
| **[QwenLM/qwen-code](https://github.com/QwenLM/qwen-code)** | 通义千问的终端编码 Agent。 | 27.7k | TypeScript |
| **[manaflow-ai/cmux](https://github.com/manaflow-ai/cmux)** | 基于 Ghostty 的开源 macOS 终端，支持纵向标签与通知。 | 27.0k | Swift |
| **[lidge-jun/opencodex](https://github.com/lidge-jun/opencodex)** | OpenAI Codex / Claude Code 的通用服务商代理，可接任意 LLM。 | 14.1k | TypeScript |
| **[opencode-ai/opencode](https://github.com/opencode-ai/opencode)** | 用 Go 打造的终端 AI 编码 Agent。 | 13.7k | Go |
| **[siteboon/claudecodeui](https://github.com/siteboon/claudecodeui)** | 在手机和网页上使用 Claude Code、Codex、Cursor CLI。 | 13.6k | TypeScript |
| **[getagentseal/codeburn](https://github.com/getagentseal/codeburn)** | 纯本地工具，追踪 37 种 AI 编码工具的 token 消耗与成本。 | 10.9k | TypeScript |
| **[smtg-ai/claude-squad](https://github.com/smtg-ai/claude-squad)** | 像管终端进程一样管理多个 AI Agent 会话。 | 8.5k | Go |
| **[fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi)** | 快速、自包含的终端 AI 编码 Agent。 | 3.4k | Python |
| **[semanser/codel](https://github.com/semanser/codel)** | 可执行复杂任务与项目的全自主 AI Agent。 | 2.5k | TypeScript |
| **[Nano-Collective/nanocoder](https://github.com/Nano-Collective/nanocoder)** | 社区共建的终端开源编码 Agent。 | 2.5k | TypeScript |
| **[kbwo/ccmanager](https://github.com/kbwo/ccmanager)** | Claude Code / Gemini CLI / Codex CLI 的会话管理器。 | 1.2k | TypeScript |
| **[xichan96/dinotty](https://github.com/xichan96/dinotty)** | 面向 AI 编码 Agent 的多设备终端服务器。 | 690 | TypeScript |

<sub>共 25 个项目 · [回到目录](#目录)</sub>

---

## Prompt-to-App 全栈应用生成

> 🌐 用一句话生成网站、App、后端与工作流，vibe coding 的正面战场。
>
> *Prompt-to-App Builders*

| 项目 | 简介 | ⭐ Star | 语言 |
|:---|:---|---:|:---|
| **[n8n-io/n8n](https://github.com/n8n-io/n8n)** | 原生 AI 能力的可视化工作流自动化平台。 | 204k | TypeScript |
| **[langgenius/dify](https://github.com/langgenius/dify)** | 构建 Agentic 工作流与 RAG 管道的 LLM 应用开发平台。 | 155k | TypeScript |
| **[abi/screenshot-to-code](https://github.com/abi/screenshot-to-code)** | 截图直接转代码（HTML / Tailwind / React / Vue）。 | 78.4k | Python |
| **[AntonOsika/gpt-engineer](https://github.com/AntonOsika/gpt-engineer)** | 用自然语言描述，直接生成整个代码库。 | 55.1k | Python |
| **[jeecgboot/JeecgBoot](https://github.com/jeecgboot/JeecgBoot)** | 企业级 AI 低代码平台，一句话生成前后端甚至整个系统。 | 47.7k | Java |
| **[ToolJet/ToolJet](https://github.com/ToolJet/ToolJet)** | 开源企业级应用生成平台。 | 40.9k | JavaScript |
| **[Pythagora-io/gpt-pilot](https://github.com/Pythagora-io/gpt-pilot)** | 最早真正能端到端写全栈应用的 AI 开发者之一。 | 33.7k | Python |
| **[activepieces/activepieces](https://github.com/activepieces/activepieces)** | AI Agent + MCP + 工作流自动化平台。 | 24.4k | TypeScript |
| **[nocobase/nocobase](https://github.com/nocobase/nocobase)** | 开源 AI + 无代码业务系统搭建平台。 | 24.1k | TypeScript |
| **[dyad-sh/dyad](https://github.com/dyad-sh/dyad)** | 本地开源 AI 应用生成器，v0 / Lovable / Replit 的本地替代。 | 21.4k | TypeScript |
| **[wasp-lang/open-saas](https://github.com/wasp-lang/open-saas)** | 免费的现代 JS SaaS 脚手架（React / NodeJS / Prisma）。 | 15.8k | MDX |
| **[InsForge/InsForge](https://github.com/InsForge/InsForge)** | 面向 agentic coding 的一体化开源后端平台。 | 12.9k | TypeScript |
| **[mcp-use/mcp-use](https://github.com/mcp-use/mcp-use)** | 全栈 MCP 框架，为 ChatGPT / Claude 开发 MCP 应用。 | 10.6k | TypeScript |
| **[21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp)** | 在 Cursor / Claude Code / Windsurf 里搜索 10000+ UI 组件。 | 5.8k | TypeScript |
| **[cloudflare/vibesdk](https://github.com/cloudflare/vibesdk)** | Cloudflare 开源 vibe coding 平台，帮你搭自己的 vibe-coding 产品。 | 5.4k | TypeScript |
| **[get-convex/chef](https://github.com/get-convex/chef)** | 「懂后端」的 AI 应用生成器。 | 4.6k | TypeScript |
| **[FullAgent/fulling](https://github.com/FullAgent/fulling)** | AI 驱动的全栈工程师 Agent。 | 2.4k | TypeScript |
| **[guanyang/open-agent-hub](https://github.com/guanyang/open-agent-hub)** | 零依赖 CLI，管理和激活 Agent 能力包。 | 963 | TypeScript |
| **[tastyeffectco/sandboxd](https://github.com/tastyeffectco/sandboxd)** | 自托管 AI 应用生成器，Agent 在隔离沙箱里构建真实应用。 | 936 | Go |
| **[Marve10s/Better-Fullstack](https://github.com/Marve10s/Better-Fullstack)** | 一键生成生产级全栈项目脚手架，支持 TS / Rust / Python / Go。 | 741 | TypeScript |
| **[giselles-ai/giselle](https://github.com/giselles-ai/giselle)** | 开源 AI 应用构建器。 | 555 | TypeScript |

<sub>共 21 个项目 · [回到目录](#目录)</sub>

---

## Agent 框架与多智能体编排

> 🧩 让一堆 Agent 分工协作，把「一个人写代码」变成「指挥一支团队」。
>
> *Agent Frameworks & Orchestration*

| 项目 | 简介 | ⭐ Star | 语言 |
|:---|:---|---:|:---|
| **[langchain-ai/langchain](https://github.com/langchain-ai/langchain)** | Agent 工程平台，构建 LLM 应用的事实标准之一。 | 146k | Python |
| **[browser-use/browser-use](https://github.com/browser-use/browser-use)** | 让 Agent 真正会用浏览器。 | 114k | Python |
| **[bytedance/deer-flow](https://github.com/bytedance/deer-flow)** | 长时程 SuperAgent 编排框架，能研究、编码与推理。 | 82.1k | Python |
| **[ruvnet/ruflo](https://github.com/ruvnet/ruflo)** | 多智能体蜂群元 harness。 | 71.8k | TypeScript |
| **[FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT)** | 多 Agent 框架，目标是迈向「AI 软件公司」。 | 70.3k | Python |
| **[microsoft/autogen](https://github.com/microsoft/autogen)** | 微软的多 Agent 对话与协作框架。 | 60.9k | Python |
| **[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)** | 角色扮演式自主 Agent 编排框架。 | 58.3k | Python |
| **[HKUDS/nanobot](https://github.com/HKUDS/nanobot)** | 超轻量、可自托管的个人 AI Agent 框架。 | 48.0k | Python |
| **[langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)** | 构建有状态、可循环的多 Agent 应用编排框架。 | 41.3k | Python |
| **[Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)** | 面向 Claude Code 的团队式多 Agent 编排。 | 39.1k | TypeScript |
| **[openai/openai-agents-python](https://github.com/openai/openai-agents-python)** | OpenAI 官方 Agent SDK。 | 29.3k | Python |
| **[cft0808/edict](https://github.com/cft0808/edict)** | 「三省六部制」式多 Agent 编排系统，9 个专业角色分工。 | 16.9k | Python |
| **[HKUDS/DeepCode](https://github.com/HKUDS/DeepCode)** | 开放的 agentic 编码框架，聚焦 Agent Harness 与循环工程。 | 16.5k | Python |
| **[Untrivial-ai/agent-orchestrator](https://github.com/Untrivial-ai/agent-orchestrator)** | 从规划到合并，运行并监督整支编码 Agent 团队。 | 11.2k | Go |
| **[omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)** | 开源 AI Agent 框架与元 harness。 | 9.8k | Python |
| **[agent-of-empires/agent-of-empires](https://github.com/agent-of-empires/agent-of-empires)** | 从 TUI 或网页管理多个 Claude Code / OpenCode Agent。 | 3.2k | Rust |
| **[AgentsMesh/AgentsMesh](https://github.com/AgentsMesh/AgentsMesh)** | AI Agent 劳动力平台，跨机器跑上百个编码 Agent。 | 2.3k | Go |
| **[andyrewlee/awesome-agent-orchestrators](https://github.com/andyrewlee/awesome-agent-orchestrators)** | Agent 编排器清单。 | 1.8k | — |
| **[the-open-engine/zeroshot](https://github.com/the-open-engine/zeroshot)** | 独立的「执行—验证」编排，用于安全地改动软件。 | 1.8k | Rust |
| **[awslabs/cli-agent-orchestrator](https://github.com/awslabs/cli-agent-orchestrator)** | AI 编码 CLI 的多 Agent 编排（AWS Labs）。 | 1.2k | Python |
| **[Rath-Team/OpenRath](https://github.com/Rath-Team/OpenRath)** | 类 PyTorch 的动态多 Agent 运行时。 | 1.1k | Python |
| **[massgen/MassGen](https://github.com/massgen/MassGen)** | 开源多 Agent 扩展系统，在本地跑 Agent 集群。 | 1.1k | Python |
| **[Intrect-io/OpenSwarm](https://github.com/Intrect-io/OpenSwarm)** | 由 Claude Code 驱动的自主 AI 开发团队编排器。 | 855 | TypeScript |
| **[ruvnet/metaharness](https://github.com/ruvnet/metaharness)** | 为 AI Agent 提供元 harness，脚手架化你的专属框架。 | 642 | TypeScript |

<sub>共 24 个项目 · [回到目录](#目录)</sub>

---

## MCP 生态 Model Context Protocol

> 🔌 给 Agent 装上手和眼睛：官方 SDK、服务器合集、连接器与网关。
>
> *Model Context Protocol*

| 项目 | 简介 | ⭐ Star | 语言 |
|:---|:---|---:|:---|
| **[punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** | 最全的 MCP 服务器大全。 | 94.7k | — |
| **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** | MCP 官方服务器合集。 | 90.2k | TypeScript |
| **[upstash/context7](https://github.com/upstash/context7)** | 为 LLM 与 AI 编辑器提供最新代码文档。 | 61.8k | TypeScript |
| **[ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)** | 给编码 Agent 用的 Chrome DevTools。 | 51.5k | TypeScript |
| **[DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)** | 高性能代码智能 MCP 服务器，把代码库索引成图。 | 42.8k | C |
| **[oraios/serena](https://github.com/oraios/serena)** | 强大的编码 MCP 工具箱，提供语义检索与编辑。 | 29.1k | Python |
| **[ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp)** | 用任意 LLM 控制 Blender 3D。 | 27.9k | Python |
| **[PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp)** | 用 Python 快速构建 MCP 服务端与客户端。 | 27.6k | Python |
| **[modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)** | MCP 官方 Python SDK，构建服务端与客户端。 | 24.3k | Python |
| **[GLips/Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP)** | 把 Figma 布局信息喂给编码 Agent。 | 15.8k | TypeScript |
| **[CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp)** | AI 助手与 Unity 编辑器之间的 MCP 桥。 | 14.1k | C# |
| **[hangwin/mcp-chrome](https://github.com/hangwin/mcp-chrome)** | 基于 Chrome 扩展的 MCP 服务器。 | 12.4k | TypeScript |
| **[BeehiveInnovations/pal-mcp-server](https://github.com/BeehiveInnovations/pal-mcp-server)** | 把 Claude Code / Gemini CLI 的能力扩展成 MCP。 | 11.7k | Python |
| **[lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent)** | 用 MCP + 简单工作流构建高效 Agent。 | 8.5k | Python |
| **[firecrawl/firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server)** | Firecrawl 官方 MCP 服务器，网页抓取与搜索。 | 7.4k | JavaScript |
| **[modelcontextprotocol/registry](https://github.com/modelcontextprotocol/registry)** | MCP 社区驱动的注册表服务。 | 7.2k | Go |
| **[mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp)** | 移动端自动化与抓取的 MCP 服务器（iOS / Android）。 | 6.6k | TypeScript |
| **[MinishLab/semble](https://github.com/MinishLab/semble)** | 面向 Agent 的快速代码搜索，比 grep 少用 99% token。 | 6.0k | Python |
| **[appcypher/awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers)** | MCP 服务器精选列表。 | 5.8k | — |
| **[oomol-lab/open-connector](https://github.com/oomol-lab/open-connector)** | 开源鉴权网关，把 1400+ SaaS 服务接到 AI Agent。 | 5.7k | TypeScript |
| **[executeautomation/mcp-playwright](https://github.com/executeautomation/mcp-playwright)** | Playwright MCP 服务器，自动化浏览器与测试。 | 5.6k | TypeScript |
| **[nanbingxyz/5ire](https://github.com/nanbingxyz/5ire)** | 跨平台桌面 AI 助手与 MCP 客户端。 | 5.3k | TypeScript |
| **[IBM/mcp-context-forge](https://github.com/IBM/mcp-context-forge)** | 位于 MCP / A2A 之前的 AI 网关、注册表与代理。 | 4.4k | Python |
| **[zinja-coder/jadx-ai-mcp](https://github.com/zinja-coder/jadx-ai-mcp)** | JADX 的 MCP 插件，用 AI 辅助逆向。 | 2.8k | Java |
| **[stacklok/toolhive](https://github.com/stacklok/toolhive)** | 企业级 MCP 服务器运行与管理平台。 | 2.2k | Go |
| **[GongRzhe/Office-Word-MCP-Server](https://github.com/GongRzhe/Office-Word-MCP-Server)** | 读写 Word 文档的 MCP 服务器。 | 2.1k | Python |
| **[CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity)** | Unity 编辑器的 MCP 插件。 | 1.9k | C# |
| **[SecretiveShell/MCP-Bridge](https://github.com/SecretiveShell/MCP-Bridge)** | 提供可调用 MCP 的 OpenAI 兼容端点。 | 930 | Python |
| **[Adancurusul/embedded-debugger-mcp](https://github.com/Adancurusul/embedded-debugger-mcp)** | 通过探针做嵌入式调试的 MCP 服务器与技能。 | 183 | Rust |

<sub>共 29 个项目 · [回到目录](#目录)</sub>

---

## 上下文工程 规范驱动 Skills 与记忆

> 🧠 决定 vibe coding 上限的一层：规则、技能、规范与跨会话记忆。
>
> *Context Engineering, Spec-Driven & Memory*

| 项目 | 简介 | ⭐ Star | 语言 |
|:---|:---|---:|:---|
| **[mattpocock/skills](https://github.com/mattpocock/skills)** | 面向真正工程师的 Skills 合集，来自作者的 .agents 目录。 | 258k | Shell |
| **[multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)** | 源自 Karpathy 观点的单个 CLAUDE.md，改善 Claude Code 行为。 | 212k | — |
| **[microsoft/markitdown](https://github.com/microsoft/markitdown)** | 把各种文档转成 Markdown，方便喂给 LLM。 | 182k | Python |
| **[x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)** | 各家 AI 工具（Cursor / Claude Code / Devin 等）的系统提示词合集。 | 143k | — |
| **[github/spec-kit](https://github.com/github/spec-kit)** | GitHub 官方规范驱动开发（SDD）起步工具包。 | 134k | Python |
| **[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)** | 让 AI Agent 像房间里最懒的资深工程师那样思考。 | 133k | JavaScript |
| **[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)** | 把代码库连同文档、SQL、配置与 PDF 变成可查询知识图谱。 | 116k | Python |
| **[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)** | 跨会话持久记忆，为每个 Agent 捕获完整上下文。 | 93.6k | JavaScript |
| **[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)** | 面向 AI 编码 Agent 的生产级工程技能。 | 93.2k | JavaScript |
| **[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)** | 让 AI 有「品味」，停止生成无聊又通用的代码。 | 85.8k | JavaScript |
| **[Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything)** | 把任意代码变成可交互的知识图谱。 | 81.9k | TypeScript |
| **[ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)** | Claude Skills 资源与工具精选。 | 74.8k | Python |
| **[colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)** | 预索引的代码知识图谱，随代码变更自动同步。 | 70.3k | C |
| **[Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)** | 面向 AI 编码助手的规范驱动开发（SDD）。 | 67.8k | TypeScript |
| **[asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks)** | 泄露的各大模型系统提示词合集。 | 64.6k | JavaScript |
| **[gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done)** | 轻量但强大的元提示、上下文工程与规范驱动框架。 | 64.6k | JavaScript |
| **[wshobson/agents](https://github.com/wshobson/agents)** | 多 harness 的 agentic 插件市场（Claude Code / Codex / Cursor）。 | 39.5k | Python |
| **[VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)** | 1000+ Agent Skills 精选合集。 | 34.0k | — |
| **[rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)** | 面向 AI 编码 Agent 的持久记忆层。 | 28.2k | TypeScript |
| **[OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)** | 基于文件的持久规划，适合长任务与长时程 Agent。 | 26.8k | Python |
| **[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)** | 380 个 Claude Code 技能与插件（30+ Agent、70+ 命令）。 | 25.8k | Python |
| **[SuperClaude-Org/SuperClaude_Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework)** | 用专业命令、角色与工作流增强 Claude Code 的配置框架。 | 23.9k | Python |
| **[travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills)** | Claude Skills 精选列表。 | 15.0k | — |
| **[Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills)** | 面向全栈开发者的 67 个专业技能，把 Claude Code 变成工程团队。 | 11.4k | Python |
| **[cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering)** | AI 编码「循环工程」的实践模式、模板与 CLI。 | 11.1k | TypeScript |
| **[KhazP/vibe-coding-prompt-template](https://github.com/KhazP/vibe-coding-prompt-template)** | 生成 PRD、技术方案与 MVP 的模板与工作流。 | 3.1k | TypeScript |
| **[rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow)** | Claude Code 从你的纠正中学习，形成自我纠正的记忆。 | 2.8k | JavaScript |
| **[dyoshikawa/rulesync](https://github.com/dyoshikawa/rulesync)** | AI 编码 Agent 的配置同步 CLI 工具。 | 1.4k | TypeScript |
| **[GanyuanRan/Aegis](https://github.com/GanyuanRan/Aegis)** | 让 AI 编码 Agent 具备架构感知能力。 | 1.2k | Python |
| **[withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit)** | 规范驱动的编码 harness：你的 AI 会忘，它记得。 | 1.1k | JavaScript |
| **[KingLeoJr/awesome-vibe-coding-prompt-code-templates](https://github.com/KingLeoJr/awesome-vibe-coding-prompt-code-templates)** | 可直接投喂 Cursor / bolt.diy 等的构建器提示词模板。 | 277 | — |

<sub>共 31 个项目 · [回到目录](#目录)</sub>

---

## 代码审查 测试与安全

> 🔍 AI 写的代码谁来把关？这一层负责审查、测试与安全。
>
> *Code Review, Testing & Security*

| 项目 | 简介 | ⭐ Star | 语言 |
|:---|:---|---:|:---|
| **[KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon)** | 面向 Web 应用与 API 的 AI 渗透测试工具。 | 47.9k | TypeScript |
| **[zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill)** | 逆向工程 / 授权渗透 / 安全研究的 Agent 技能。 | 35.3k | PowerShell |
| **[mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)** | 817 个结构化网络安全技能，映射到 6 大框架。 | 32.5k | Python |
| **[alibaba/open-code-review](https://github.com/alibaba/open-code-review)** | 阿里巴巴规模验证的快速代码审查工具。 | 22.2k | Go |
| **[NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector)** | AI Agent 技能安全扫描器，检测漏洞与恶意技能。 | 16.8k | Python |
| **[aliasrobotics/cai](https://github.com/aliasrobotics/cai)** | 网络安全 AI（CAI）框架，面向 AI 安全研究。 | 9.8k | Python |
| **[TommyLemon/APIAuto](https://github.com/TommyLemon/APIAuto)** | 接口工具：零代码测试 + AI 问答 + 生成代码与文档。 | 2.2k | JavaScript |
| **[0xSteph/pentest-ai-agents](https://github.com/0xSteph/pentest-ai-agents)** | 把 Claude Code 变成你的攻击性安全研究助手。 | 2.2k | Shell |
| **[0xSteph/pentest-ai](https://github.com/0xSteph/pentest-ai)** | 开源 AI 渗透测试，用机器预言机证明每个发现。 | 1.7k | Python |
| **[mukul975/cve-mcp-server](https://github.com/mukul975/cve-mcp-server)** | 给 Claude 提供 27 个安全情报工具的 MCP 服务器。 | 1.5k | Python |
| **[mrphrazer/reverser_ai](https://github.com/mrphrazer/reverser_ai)** | 用 AI 提供自动化逆向工程辅助。 | 1.1k | Python |
| **[Tzohar/PassLLM](https://github.com/Tzohar/PassLLM)** | AI 密码猜测工具（PyTorch 实现）。 | 117 | Python |

<sub>共 12 个项目 · [回到目录](#目录)</sub>

---

## AI 设计与 UI 生成

> 🎨 从设计稿到代码，或者直接用自然语言生成界面。
>
> *AI Design & UI Generation*

| 项目 | 简介 | ⭐ Star | 语言 |
|:---|:---|---:|:---|
| **[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)** | 各大品牌设计系统的 DESIGN.md 分析合集，丢进项目就能让 AI 有设计感。 | 115k | — |
| **[nexu-io/open-design](https://github.com/nexu-io/open-design)** | 开源的 Claude Design 替代方案。 | 95.2k | TypeScript |
| **[google-labs-code/design.md](https://github.com/google-labs-code/design.md)** | 向编码 Agent 描述视觉标识的格式规范。 | 27.8k | TypeScript |
| **[onlook-dev/onlook](https://github.com/onlook-dev/onlook)** | 设计师的 Cursor，可视化构建与编辑 React 应用。 | 26.7k | TypeScript |
| **[alexpate/awesome-design-systems](https://github.com/alexpate/awesome-design-systems)** | 设计系统精选合集。 | 25.9k | — |
| **[nexu-io/html-anything](https://github.com/nexu-io/html-anything)** | agentic HTML 编辑器：本地 AI Agent 写 HTML，你只管调。 | 8.7k | HTML |
| **[grab/cursor-talk-to-figma-mcp](https://github.com/grab/cursor-talk-to-figma-mcp)** | Cursor / Claude Code 与 Figma 的双向 MCP 联动。 | 7.0k | JavaScript |
| **[ZSeven-W/openpencil](https://github.com/ZSeven-W/openpencil)** | 号称全球首个开源 AI 原生矢量设计工具。 | 5.9k | Rust |
| **[lnkiai/m3e-canvas](https://github.com/lnkiai/m3e-canvas)** | 在浏览器里画 Material 3 界面，并转成可用代码。 | 5.5k | TypeScript |
| **[maxbogo/awesome-ai-tools-for-ui](https://github.com/maxbogo/awesome-ai-tools-for-ui)** | 打造漂亮 UI / UX 的 AI 工具精选。 | 868 | — |
| **[0xnyn/airship](https://github.com/0xnyn/airship)** | 为 Claude Code / Codex / OpenCode 打造的 Figma 式可视化编辑器。 | 676 | TypeScript |
| **[Railly/tinte](https://github.com/Railly/tinte)** | 把设计系统编译成 Agent 插件。 | 619 | TypeScript |

<sub>共 12 个项目 · [回到目录](#目录)</sub>

---

## 硬件 边缘 AI 与机器人

> 🔧 vibe coding 溢出到物理世界：AI 开发板、语音硬件、机器人、给 Agent 做的实体外设。
>
> *Hardware, Edge AI & Robotics*

| 项目 | 简介 | ⭐ Star | 语言 |
|:---|:---|---:|:---|
| **[78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)** | 基于 MCP 的 ESP32 聊天机器人「小智」，国内 AI 硬件生态的爆款开源项目。 | 29.8k | C++ |
| **[huggingface/lerobot](https://github.com/huggingface/lerobot)** | 让机器人 AI 更易用的端到端学习库。 | 27.4k | Python |
| **[arendst/Tasmota](https://github.com/arendst/Tasmota)** | ESP8266 / ESP32 设备的替代固件。 | 24.7k | C |
| **[microsoft/onnxruntime](https://github.com/microsoft/onnxruntime)** | 跨平台高性能 ML 推理与训练加速。 | 21.8k | C++ |
| **[espressif/esp-idf](https://github.com/espressif/esp-idf)** | 乐鑫官方 IoT 开发框架，AI 硬件的地基。 | 19.0k | C |
| **[earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)** | 面向 CAD / CAE / CAM 的 Agent 技能库，用自然语言建模。 | 15.0k | Python |
| **[makerspet/oomwoo](https://github.com/makerspet/oomwoo)** | 开源扫地机器人。 | 10.6k | Python |
| **[PetoiCamp/OpenCat-Quadruped-Robot](https://github.com/PetoiCamp/OpenCat-Quadruped-Robot)** | 开源四足机器人宠物框架。 | 5.3k | C++ |
| **[torvalds/AudioNoise](https://github.com/torvalds/AudioNoise)** | Linus Torvalds 用 vibe coding 做的数字吉他效果器，硬件 DIY 项目。 | 4.5k | C |
| **[slvDev/esp32-ai](https://github.com/slvDev/esp32-ai)** | 在 ESP32 上跑 AI 的项目合集。 | 4.3k | Python |
| **[Seeed-Projects/reBot-DevArm](https://github.com/Seeed-Projects/reBot-DevArm)** | 面向所有开发者的开源机械臂。 | 4.2k | Python |
| **[isaac-sim/IsaacSim](https://github.com/isaac-sim/IsaacSim)** | NVIDIA 开源机器人仿真应用。 | 4.0k | Python |
| **[atopile/atopile](https://github.com/atopile/atopile)** | 用代码设计电路板，像写软件一样复用硬件设计。 | 3.9k | Python |
| **[ailyProject/aily-blockly](https://github.com/ailyProject/aily-blockly)** | 面向硬件开发的 AI IDE，支持 Arduino / MicroPython / ESP32 / STM32。 | 3.8k | TypeScript |
| **[adamcohenhillel/ADeus](https://github.com/adamcohenhillel/ADeus)** | 开源 AI 可穿戴设备，记录你所说与所听。 | 3.4k | TypeScript |
| **[mani-skill/ManiSkill](https://github.com/mani-skill/ManiSkill)** | GPU 并行机器人仿真与操作技能框架。 | 3.3k | Python |
| **[OpenMind/OM1](https://github.com/OpenMind/OM1)** | 面向机器人的模块化 AI 硬件抽象层（HAL）。 | 2.9k | Go |
| **[Nate711/StanfordDoggoProject](https://github.com/Nate711/StanfordDoggoProject)** | 会跳、会翻的开源四足机器人。 | 2.6k | — |
| **[Roboparty/roboto_origin](https://github.com/Roboparty/roboto_origin)** | 全开源 DIY 手搓级人形机器人。 | 2.4k | Python |
| **[facebookresearch/pyrobot](https://github.com/facebookresearch/pyrobot)** | 开源机器人研究平台。 | 2.3k | Python |
| **[google-deepmind/mujoco_playground](https://github.com/google-deepmind/mujoco_playground)** | GPU 加速机器人学习与 sim-to-real 库。 | 2.2k | Python |
| **[martin-ger/esp32_nat_router](https://github.com/martin-ger/esp32_nat_router)** | 支持 AI 的 ESP32 NAT 路由器 / 防火墙。 | 2.2k | C |
| **[akdeb/ElatoAI](https://github.com/akdeb/ElatoAI)** | 基于 Arduino ESP32 的实时语音 AI，支持 100+ 模型。 | 2.0k | TypeScript |
| **[BCN3D/BCN3D-Moveo](https://github.com/BCN3D/BCN3D-Moveo)** | 面向教育的开源 3D 打印机械臂。 | 2.0k | C++ |
| **[tuya/TuyaOpen](https://github.com/tuya/TuyaOpen)** | 面向 AI + IoT 的跨平台 C/C++ SDK，支持 ESP32 等，主打硬件在环的 vibe coding。 | 1.8k | C |
| **[Xilinx/Vitis-AI](https://github.com/Xilinx/Vitis-AI)** | Xilinx 硬件上的 AI 推理开发栈。 | 1.8k | Python |
| **[mjyc/awesome-robotics-projects](https://github.com/mjyc/awesome-robotics-projects)** | 开源、平价、少见的机器人项目清单。 | 1.8k | — |
| **[Skythinker616/foc-wheel-legged-robot](https://github.com/Skythinker616/foc-wheel-legged-robot)** | 轮腿机器人开源资料（结构 + 控制）。 | 1.7k | C |
| **[commaai/neo](https://github.com/commaai/neo)** | comma.ai 的全部开源硬件。 | 1.7k | — |
| **[ClimbSnail/HoloCubic_AIO](https://github.com/ClimbSnail/HoloCubic_AIO)** | 基于 ESP32 的多功能 AIO 固件（天气时钟、相册、投屏等）。 | 1.4k | C |
| **[pnoker/iot-dc3](https://github.com/pnoker/iot-dc3)** | 多协议、云原生、AI 驱动的开源工业 IoT 平台。 | 1.2k | Java |
| **[menloresearch/asimov-1](https://github.com/menloresearch/asimov-1)** | 开源人形机器人 Asimov v1。 | 1.2k | Python |
| **[mangdangroboticsclub/QuadrupedRobot](https://github.com/mangdangroboticsclub/QuadrupedRobot)** | 开源 ROS 机器狗套件。 | 1.2k | Python |
| **[CSCB/vibe-mouse](https://github.com/CSCB/vibe-mouse)** | 开源 Vibe Coding 交互鼠标项目。 | 1.1k | Python |
| **[poppy-project/poppy-humanoid](https://github.com/poppy-project/poppy-humanoid)** | 开源 3D 打印人形机器人，专注优化与实验。 | 1.1k | Jupyter Notebook |
| **[RealDeco/xiaozhi-esphome](https://github.com/RealDeco/xiaozhi-esphome)** | 在 ESPHome / Home Assistant 里使用小智 AI 设备。 | 812 | Rich Text Format |
| **[Explorerlowi/ESP32_AI_LLM](https://github.com/Explorerlowi/ESP32_AI_LLM)** | ESP32 / ESP32-S3 接入 15 款大模型实现语音对话。 | 556 | C |
| **[PetoiCamp/OpenCatEsp32-Quadruped-Robot](https://github.com/PetoiCamp/OpenCatEsp32-Quadruped-Robot)** | 基于 ESP32 的开源四足机器人宠物框架。 | 396 | C++ |
| **[AI-FanGe/AI_DesktopCat_Qwen3.5Omni](https://github.com/AI-FanGe/AI_DesktopCat_Qwen3.5Omni)** | 以 Qwen3.5 Omni 为模型的 AI 桌面硬件猫。 | 352 | Python |
| **[msb-msb/awesome-local-ai](https://github.com/msb-msb/awesome-local-ai)** | 在消费级硬件上本地运行 AI 的资源精选。 | 287 | — |
| **[ai-hpc/ai-hardware-engineer-roadmap](https://github.com/ai-hpc/ai-hardware-engineer-roadmap)** | AI 硬件工程师路线图：推理、Agent harness 与硬件工程。 | 267 | HTML |
| **[JasonLam08/cursor_agent_status_light](https://github.com/JasonLam08/cursor_agent_status_light)** | 用 ESP32-C3 做的 BLE 状态灯，实时显示 Cursor Agent 状态。 | 257 | C++ |
| **[maximilienroberti/lerobotdepot](https://github.com/maximilienroberti/lerobotdepot)** | 社区维护的开源机器人硬件项目清单。 | 243 | — |
| **[puritysb/AgentDeck](https://github.com/puritysb/AgentDeck)** | AI 编码 Agent 的物理控制器与多屏仪表盘。 | 229 | TypeScript |
| **[M64GitHub/WireClaw](https://github.com/M64GitHub/WireClaw)** | 带持久记忆与离线规则引擎的 ESP32 AI Agent。 | 185 | C++ |
| **[SensorsIot/Embedded-AI-Harness](https://github.com/SensorsIot/Embedded-AI-Harness)** | 嵌入式系统的 AI 闭环编程：AI 写码、烧录、调试。 | 173 | Python |
| **[akdeb/OpenToys](https://github.com/akdeb/OpenToys)** | 用 MacBook + Arduino 做本地 AI 玩具、机器人与设备。 | 159 | TypeScript |
| **[grpcer/tokpet](https://github.com/grpcer/tokpet)** | 把 AI 用量、额度与余额做成桌面宠物。 | 154 | C |
| **[FutureProofHomes/Satellite1-Hardware](https://github.com/FutureProofHomes/Satellite1-Hardware)** | 开源 AI 语音助手与多传感器硬件。 | 152 | — |
| **[open-edge-platform/edge-ai-suites](https://github.com/open-edge-platform/edge-ai-suites)** | 边缘 AI 示例应用合集。 | 130 | Python |
| **[conol-ai/openmicrokbd](https://github.com/conol-ai/openmicrokbd)** | OpenAI Codex Micro 宏键盘的开源复刻，PCB 用代码写。 | 115 | Rust |

<sub>共 51 个项目 · [回到目录](#目录)</sub>

---

## 本地模型与自托管

> ⚙️ 把模型和数据留在自己机器上，跑得起、花得少。
>
> *Local Models & Self-Hosting*

| 项目 | 简介 | ⭐ Star | 语言 |
|:---|:---|---:|:---|
| **[ollama/ollama](https://github.com/ollama/ollama)** | 一行命令在本地跑各种开源大模型。 | 181k | Go |
| **[open-webui/open-webui](https://github.com/open-webui/open-webui)** | 友好的自托管 AI 界面，支持 Ollama 与 OpenAI API。 | 151k | Python |
| **[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)** | 纯 C/C++ 的 LLM 推理实现，本地部署的基石。 | 128k | C++ |
| **[vllm-project/vllm](https://github.com/vllm-project/vllm)** | 高吞吐、显存高效的 LLM 推理与服务引擎。 | 91.4k | Python |
| **[nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all)** | 在任意设备上运行本地 LLM。 | 77.4k | C++ |
| **[unslothai/unsloth](https://github.com/unslothai/unsloth)** | 本地微调与运行 LLM / 扩散模型，支持 GGUF、MLX。 | 76.0k | Python |
| **[Mintplex-Labs/anything-llm](https://github.com/Mintplex-Labs/anything-llm)** | 自托管的私有 AI 工作台。 | 65.8k | JavaScript |
| **[BerriAI/litellm](https://github.com/BerriAI/litellm)** | 统一调用 100+ LLM API 的 AI 网关。 | 58.4k | Python |
| **[mudler/LocalAI](https://github.com/mudler/LocalAI)** | 开源本地 AI 引擎，可跑 LLM、视觉、语音等任意模型。 | 49.0k | Go |
| **[janhq/jan](https://github.com/janhq/jan)** | 100% 离线运行的 ChatGPT 开源替代。 | 44.4k | TypeScript |
| **[chatchat-space/Langchain-Chatchat](https://github.com/chatchat-space/Langchain-Chatchat)** | 基于 LangChain 的本地知识库问答。 | 38.6k | Python |
| **[khoj-ai/khoj](https://github.com/khoj-ai/khoj)** | 可自托管的 AI「第二大脑」。 | 37.2k | Python |
| **[AlexsJones/llmfit](https://github.com/AlexsJones/llmfit)** | 一条命令，找出你的硬件能跑哪些模型。 | 35.4k | Rust |
| **[mozilla-ai/llamafile](https://github.com/mozilla-ai/llamafile)** | 把模型与运行时分发成单个可执行文件。 | 25.9k | C++ |
| **[microsoft/vscode-copilot-chat](https://github.com/microsoft/vscode-copilot-chat)** | VS Code Copilot Chat 的开源实现。 | 10.0k | TypeScript |
| **[mudler/LocalAGI](https://github.com/mudler/LocalAGI)** | 可自托管的 AI Agent 平台。 | 2.0k | Go |
| **[gensyn-ai/codeassist](https://github.com/gensyn-ai/codeassist)** | 完全私有、本地运行的 AI 编码助手。 | 699 | Python |
| **[jaylfc/taOS](https://github.com/jaylfc/taOS)** | 自托管 AI Agent 操作系统，记忆、聊天、文件全在本地。 | 522 | Python |
| **[nirholas/PAI](https://github.com/nirholas/PAI)** | 装进 U 盘的完整私人电脑（可启动 Debian）。 | 109 | Shell |

<sub>共 19 个项目 · [回到目录](#目录)</sub>

---

## 学习资源 教程与 Awesome 列表

> 📚 从零学会 vibe coding，以及各类精选清单。
>
> *Learning, Tutorials & Awesome Lists*

| 项目 | 简介 | ⭐ Star | 语言 |
|:---|:---|---:|:---|
| **[f/prompts.chat](https://github.com/f/prompts.chat)** | 提示词分享与发现社区（原 Awesome ChatGPT Prompts）。 | 170k | HTML |
| **[dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)** | 提示工程指南：论文、课程与笔记。 | 78.1k | MDX |
| **[datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents)** | 《从零开始构建智能体》——智能体原理与实践教程。 | 78.0k | Python |
| **[shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code)** | 用 Bash 从零实现一个 nano claude code 式 agent harness。 | 76.4k | Python |
| **[microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners)** | 18 节课入门构建 AI Agent。 | 74.3k | Jupyter Notebook |
| **[hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** | Claude Code 生态资源精选。 | 53.8k | Python |
| **[rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)** | 从零开始学 AI 工程：学它、建它、发布它。 | 53.7k | Python |
| **[liyupi/ai-guide](https://github.com/liyupi/ai-guide)** | 程序员鱼皮的 AI 资源大全 + Vibe Coding 零基础教程。 | 19.7k | JavaScript |
| **[datawhalechina/easy-vibe](https://github.com/datawhalechina/easy-vibe)** | vibe coding 101：面向 AI 原生产品构建者的第一门课。 | 19.3k | JavaScript |
| **[microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)** | 微软开源的 MCP 入门课程。 | 17.2k | Jupyter Notebook |
| **[composio-community/awesome-codex-skills](https://github.com/composio-community/awesome-codex-skills)** | Codex 实用技能精选。 | 16.3k | Python |
| **[awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode)** | opencode 生态的插件、主题、Agent 与项目精选。 | 10.2k | JavaScript |
| **[adongwanai/AgentGuide](https://github.com/adongwanai/AgentGuide)** | AI Agent 开发指南，含 LangGraph 实战。 | 9.4k | MDX |
| **[WangRongsheng/awesome-LLM-resources](https://github.com/WangRongsheng/awesome-LLM-resources)** | 全世界最好的 LLM 资料总结（含 Agent、辅助编程、MCP）。 | 8.9k | — |
| **[WenyuChiou/awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)** | 三语（繁中 / English / 简中）agentic AI 学习路线图。 | 6.7k | Python |
| **[promptslab/Awesome-Prompt-Engineering](https://github.com/promptslab/Awesome-Prompt-Engineering)** | 提示工程手工精选资源。 | 6.3k | TypeScript |
| **[mahseema/awesome-ai-tools](https://github.com/mahseema/awesome-ai-tools)** | AI 工具精选清单。 | 6.2k | — |
| **[datawhalechina/vibe-vibe](https://github.com/datawhalechina/vibe-vibe)** | 首个系统性 Vibe Coding 教程，从零到全栈。 | 6.0k | Dockerfile |
| **[filipecalegario/awesome-vibe-coding](https://github.com/filipecalegario/awesome-vibe-coding)** | Vibe Coding 参考资料精选（最早的一批清单之一）。 | 5.2k | — |
| **[alvinreal/awesome-opensource-ai](https://github.com/alvinreal/awesome-opensource-ai)** | 真正开源的 AI 项目、模型与工具精选。 | 4.7k | Python |
| **[wesammustafa/Claude-Code-Everything-You-Need-to-Know](https://github.com/wesammustafa/Claude-Code-Everything-You-Need-to-Know)** | Claude Code 实用指南，含清晰心智模型与可复制示例。 | 3.0k | Python |
| **[automata/aicodeguide](https://github.com/automata/aicodeguide)** | 用 AI 写代码的路线图。 | 2.7k | — |
| **[EgoAlpha/prompt-in-context-learning](https://github.com/EgoAlpha/prompt-in-context-learning)** | 上下文学习与提示工程资源。 | 2.2k | Jupyter Notebook |
| **[stormzhang/ai-coding-guide](https://github.com/stormzhang/ai-coding-guide)** | 面向小白的 AI 编程 CLI 中文教程（Claude Code + Codex）。 | 1.8k | — |
| **[snwfdhmp/awesome-gpt-prompt-engineering](https://github.com/snwfdhmp/awesome-gpt-prompt-engineering)** | GPT 提示工程资源与工具精选。 | 1.6k | Python |
| **[hashgraph-online/awesome-codex-plugins](https://github.com/hashgraph-online/awesome-codex-plugins)** | OpenAI Codex / ChatGPT 插件与技能精选。 | 973 | Python |
| **[snwfdhmp/awesome-ralph](https://github.com/snwfdhmp/awesome-ralph)** | 关于「Ralph」这一 AI 编码技术的资源精选。 | 919 | — |
| **[awesome-vibe-coding/awesome-vibe-coding](https://github.com/awesome-vibe-coding/awesome-vibe-coding)** | Vibe Coding 工具与资源精选清单。 | 835 | HTML |
| **[ShaikhWarsi/free-ai-tools](https://github.com/ShaikhWarsi/free-ai-tools)** | 免费与低价 AI 工具、LLM API、IDE、Agent 精选。 | 776 | TypeScript |
| **[analyticalrohit/awesome-vibe-coding-guide](https://github.com/analyticalrohit/awesome-vibe-coding-guide)** | 成为 10x Vibe Coder 的指南、最佳实践与技巧。 | 377 | — |
| **[Awesome-AI-Pedia/Awesome-AI-Pedia](https://github.com/Awesome-AI-Pedia/Awesome-AI-Pedia)** | 全维度 AI 资源百科：大模型、Agent、RAG、多模态。 | 355 | TypeScript |
| **[acvnace/awesome-vibe-coding-resources](https://github.com/acvnace/awesome-vibe-coding-resources)** | Vibe Coding 资源精选。 | 285 | — |
| **[roboco-io/awesome-vibecoding](https://github.com/roboco-io/awesome-vibecoding)** | Vibe Coding 资源、教程、最佳实践与示例。 | 203 | JavaScript |
| **[taskade/awesome-vibe-coding](https://github.com/taskade/awesome-vibe-coding)** | 用自然语言构建软件的完整 vibe coding 指南。 | 138 | — |
| **[0xWelt/Awesome-Vibe-Coding](https://github.com/0xWelt/Awesome-Vibe-Coding)** | Vibe Coding 开源项目、工具与学习资源精选。 | 105 | — |

<sub>共 35 个项目 · [回到目录](#目录)</sub>

---

## 统计概览

| 分类 | 项目数 | 分类内最高 Star |
|:---|---:|:---|
| 🤖 AI 编程助手与 IDE 插件 | 14 | 67.7k (cline/cline) |
| 🖥️ AI IDE 与代码编辑器 | 10 | 90.0k (zed-industries/zed) |
| ⌨️ 终端与 CLI 编码 Agent | 25 | 206k (anomalyco/opencode) |
| 🌐 Prompt-to-App 全栈应用生成 | 21 | 204k (n8n-io/n8n) |
| 🧩 Agent 框架与多智能体编排 | 24 | 146k (langchain-ai/langchain) |
| 🔌 MCP 生态 Model Context Protocol | 29 | 94.7k (punkpeye/awesome-mcp-servers) |
| 🧠 上下文工程 规范驱动 Skills 与记忆 | 31 | 258k (mattpocock/skills) |
| 🔍 代码审查 测试与安全 | 12 | 47.9k (KeygraphHQ/shannon) |
| 🎨 AI 设计与 UI 生成 | 12 | 115k (VoltAgent/awesome-design-md) |
| 🔧 硬件 边缘 AI 与机器人 | 51 | 29.8k (78/xiaozhi-esp32) |
| ⚙️ 本地模型与自托管 | 19 | 181k (ollama/ollama) |
| 📚 学习资源 教程与 Awesome 列表 | 35 | 170k (f/prompts.chat) |
| **合计** | **283** | **8.4M 累计 Star** |

### Star 数 Top 20

| # | 项目 | ⭐ Star | 分类 |
|:--|:---|---:|:---|
| 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | 258k | 上下文工程 规范驱动 Skills 与记忆 |
| 2 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 212k | 上下文工程 规范驱动 Skills 与记忆 |
| 3 | [anomalyco/opencode](https://github.com/anomalyco/opencode) | 206k | 终端与 CLI 编码 Agent |
| 4 | [n8n-io/n8n](https://github.com/n8n-io/n8n) | 204k | Prompt-to-App 全栈应用生成 |
| 5 | [microsoft/markitdown](https://github.com/microsoft/markitdown) | 182k | 上下文工程 规范驱动 Skills 与记忆 |
| 6 | [ollama/ollama](https://github.com/ollama/ollama) | 181k | 本地模型与自托管 |
| 7 | [f/prompts.chat](https://github.com/f/prompts.chat) | 170k | 学习资源 教程与 Awesome 列表 |
| 8 | [langgenius/dify](https://github.com/langgenius/dify) | 155k | Prompt-to-App 全栈应用生成 |
| 9 | [open-webui/open-webui](https://github.com/open-webui/open-webui) | 151k | 本地模型与自托管 |
| 10 | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 146k | Agent 框架与多智能体编排 |
| 11 | [anthropics/claude-code](https://github.com/anthropics/claude-code) | 145k | 终端与 CLI 编码 Agent |
| 12 | [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | 143k | 上下文工程 规范驱动 Skills 与记忆 |
| 13 | [github/spec-kit](https://github.com/github/spec-kit) | 134k | 上下文工程 规范驱动 Skills 与记忆 |
| 14 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 133k | 上下文工程 规范驱动 Skills 与记忆 |
| 15 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | 132k | 终端与 CLI 编码 Agent |
| 16 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | 128k | 本地模型与自托管 |
| 17 | [openai/codex](https://github.com/openai/codex) | 123k | 终端与 CLI 编码 Agent |
| 18 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 116k | 上下文工程 规范驱动 Skills 与记忆 |
| 19 | [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 115k | AI 设计与 UI 生成 |
| 20 | [browser-use/browser-use](https://github.com/browser-use/browser-use) | 114k | Agent 框架与多智能体编排 |

---

## 如何挑选工具

| 你的需求 | 推荐从这里开始 |
|:---|:---|
| 第一次接触 AI 编程 | `datawhalechina/easy-vibe`、`liyupi/ai-guide`、`automata/aicodeguide` |
| 想要终端里的编码 Agent | `anthropics/claude-code`、`openai/codex`、`Aider-AI/aider`、`anomalyco/opencode` |
| 想要编辑器插件 | `cline/cline`、`RooCodeInc/Roo-Code`、`continuedev/continue` |
| 想用一句话生成 App | `dyad-sh/dyad`、`onlook-dev/onlook`、`AntonOsika/gpt-engineer` |
| 想让多个 Agent 分工 | `langchain-ai/langgraph`、`crewAIInc/crewAI`、`bytedance/deer-flow` |
| 想给 Agent 接工具 / 数据 | `modelcontextprotocol/servers`、`punkpeye/awesome-mcp-servers` |
| 想让 AI 少犯错、记得住 | `github/spec-kit`、`Fission-AI/OpenSpec`、`thedotmack/claude-mem` |
| 想做 AI 硬件 / 机器人 | `78/xiaozhi-esp32`、`tuya/TuyaOpen`、`huggingface/lerobot` |
| 想本地跑模型、数据不出门 | `ollama/ollama`、`ggml-org/llama.cpp`、`mudler/LocalAI` |

---

## 贡献指南

欢迎补充项目、修正描述或更新 Star 数：

1. Fork 本仓库并新建分支。
2. 在 `data/repos.json` 对应分类下新增或修改条目，保持按 Star 降序。
3. 确认项目 **Star ≥ 100** 且与 vibe coding 相关。
4. 提交 PR，说明收录理由。

也可以直接提 Issue 推荐项目，附上仓库链接与一句话简介。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## License

[![CC0](https://img.shields.io/badge/license-CC0--1.0-lightgrey)](LICENSE)

本清单采用 CC0-1.0 协议，可自由复制、修改与分发。各收录项目的版权归其各自作者所有。
