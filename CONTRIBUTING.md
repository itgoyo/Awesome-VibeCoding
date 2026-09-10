# 贡献指南

感谢你愿意为 Awesome Vibe Coding 出一份力！本清单靠社区一起维护。

## 收录标准

提交项目前，请确认满足以下条件：

1. **Star ≥ 100** —— 硬性门槛，避免清单被玩具项目淹没。
2. **与 vibe coding 强相关** —— 属于以下任一方向：
   - AI 编码助手、IDE、编辑器插件
   - 终端 / CLI 编码 Agent
   - Prompt-to-App、全栈应用生成、低代码 / 无代码
   - Agent 框架与多智能体编排
   - MCP 生态（SDK、服务器、连接器、网关）
   - 上下文工程、规范驱动开发、Skills、Agent 记忆
   - 代码审查、测试、AI 安全
   - AI 设计 / UI 生成
   - **AI 硬件、边缘 AI、机器人**（本清单重点方向）
   - 本地模型与自托管
   - 学习资源、教程与 Awesome 列表
3. **项目可访问** —— 仓库公开、非空壳、有基本 README。
4. **不重复** —— 每个项目只归属一个分类。

## 提交方式

### 方式一：提交 PR（推荐）

1. Fork 本仓库，新建分支。
2. 编辑 `data/repos.json`，在对应分类的 `repos` 数组中新增条目：

```json
{
  "full_name": "owner/repo",
  "url": "https://github.com/owner/repo",
  "desc": "一句话中文简介，说明它是什么、解决什么问题。",
  "desc_en": "Original English description (optional)",
  "stars": 1234,
  "language": "TypeScript",
  "license": "MIT",
  "homepage": "https://example.com",
  "pushed_at": "2026-09-01",
  "created_at": "2025-01-01"
}
```

3. 保持同一分类内按 `stars` 降序排列。
4. 提交 PR，并在描述里说明收录理由。

### 方式二：提 Issue

如果你不方便改 JSON，直接开一个 Issue，附上：

- 仓库链接
- 建议归属的分类
- 一句话简介

维护者会代为处理。

## 描述写作约定

- 用**中文**写简介，一句话讲清楚「它是什么 + 有什么用」。
- 避免营销话术（「最强」「第一」「颠覆」），用事实描述。
- 不要照抄仓库英文简介的机翻，读起来要自然。

## 关于 Star 数

Star 数由 GitHub API 采集，会随时间变化。如果发现某个项目的 Star 数明显过期，欢迎在 PR 中一并更新；
也可以直接运行采集脚本刷新：

```bash
python3 scripts/collect.py          # 采集并写入 data/repos.json
```

## 更新流程

```bash
# 1. 采集最新数据
python3 scripts/collect.py

# 2. 检查 diff，确认没有异常项目混入
git diff data/repos.json

# 3. 提交
git commit -m "chore: refresh star counts"
```

## 行为准则

- 保持友善与耐心，对事不对人。
- 不接受刷 Star、付费推广类的项目。
- 维护者有权拒绝不符合收录标准的提交，并会说明原因。

---

再次感谢你的贡献！🪄
