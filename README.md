# AI4Chem 分子机器学习文献库

自动化的分子机器学习研究文献收集、分析、归档系统。每日自动检索最新论文，整理为结构化归档。

## 🎯 项目概述

**AI4Chem Library** 是一个由 Claude Code 云端 Routine 驱动的**自动化文献管理系统**。

- **覆盖范围**：2026 年 1-8 月，165 篇分子 ML 论文
- **自动化频率**：每天 06:00 荷兰时间执行
- **研究方向**：7 大分子 ML 领域（基础模型、性质预测、反应优化、分子设计、催化剂、逆合成等）
- **质量保障**：每篇论文包含完整作者、详细摘要、研究方向标签

## 📂 项目结构

```
.
├── papers/                      # 核心文献库
│   ├── 2026-01.md to 2026-08.md # 月度归档（按星期组织）
│   ├── index.json               # 去重索引（165 条记录）
│   ├── README.md                # 库统计与月度对比
│   └── ROUTINE_PROMPT.md        # Routine 自动化配置
│
├── README.md                    # 本文件（项目总览）
├── .gitignore                   # 版本控制配置
└── CONTRIBUTING.md              # 贡献指南（待补充）
```

## 🔬 研究方向覆盖（7 大领域）

| 方向 | 论文数 | 典型方法 | 应用 |
|------|--------|---------|------|
| **#foundation-MLIP** | 11 | 神经网络势、DFT 替代、NN-xTB | 分子模拟、材料设计 |
| **#property-pred** | 16 | GAT、KAN、ResGAT、FragNet | 高通量筛选、药物设计 |
| **#reaction-opt** | 6 | 产率预测、条件优化 | 工艺设计、催化 |
| **#mol-design** | 7 | 扩散模型、生成模型、RL | 药物发现、分子优化 |
| **#catalyst-ligand** | 5 | 催化剂发现、配体设计、LLM Agent | 反应加速、绿色化学 |
| **#TS-search** | 4 | 逆合成、反应路径规划 | 合成自动化、工艺规划 |
| **#organocatalysis** | 0 | — | 待补充（NHC、有机催化） |
| **#ml4chem-general** | 11 | 多学科融合应用 | 交叉研究 |

## 📅 月度进展概览

### H1 2026（1-6 月）— 范式转移

| 月份 | 主题 | 亮点 |
|------|------|------|
| **1月** | 基础模型元年 | ChemBERTa-2、Foundation Models 确立 |
| **2月** | 预训练热潮 | 多模态学习、迁移学习 |
| **3月** | GNN 竞争激烈 | 原子杂化、IC50 精确预测 |
| **4月** | 生成爆发 🔥 | 扩散 + RL 新范式（22 篇） |
| **5月** | 量子化学转折 | NN-xTB、DFT 替代方案 |
| **6月** | AlphaFold3 地震 | 蛋白质、复合物、小分子统一预测 |

### H2 2026（7-8月）— 架构成熟化

| 月份 | 主题 | 亮点 |
|------|------|------|
| **7月** | 图注意爆发 | KA-GNN、可解释性突破 |
| **8月** | RL 赋能设计 | ALCHIMIA、POLO、C-MORAL |

## 🤖 自动化 Routine

### 配置信息

- **触发时间**：每天 04:00 UTC（= 06:00 荷兰夏令时）
- **执行环境**：Claude Code Cloud Runtime
- **模型**：claude-sonnet-5
- **工具**：WebSearch、Bash、Read/Write/Edit、Grep
- **任务**：
  1. 检索过去 24-48 小时的 arXiv、ChemRxiv、bioRxiv 新论文
  2. 自动编写 3-5 句摘要、标注研究方向
  3. 更新 index.json（去重）、月度 MD 文件
  4. 发现相关 GitHub 项目
  5. Git commit & push

### Routine 管理

🔗 **链接**：[https://claude.ai/code/routines/trig_016pBE5hcq7P9mJbCDQ2kZsC](https://claude.ai/code/routines/trig_016pBE5hcq7P9mJbCDQ2kZsC)

- 查看历史运行记录
- 手动触发测试运行
- 修改 prompt 或触发条件
- 监控执行日志

## 📖 使用指南

### 查找论文

1. **按月份**：`papers/2026-XX.md`（XX = 月份号）
2. **按研究方向**：见 `papers/README.md` 的标签分类
3. **去重检查**：`papers/index.json`（快速查询是否已收录）

### 添加新论文

虽然系统自动化运行，但手动补充流程：

```bash
# 1. 编辑月度 MD 文件
vim papers/2026-09.md

# 2. 更新 index.json
# 增加新条目：
# {
#   "id": "arXiv:XXXX.XXXXX",
#   "title": "...",
#   "authors": "...",
#   "date_added": "2026-09-XX",
#   "tags": ["#direction1", "#direction2"]
# }

# 3. 更新 README.md 统计
vim papers/README.md

# 4. 提交
git add papers/
git commit -m "papers: add N entries (2026-09-XX)"
git push
```

## 📊 数据统计

### 论文总数：165 篇

**按方向分布**：
- #property-pred：16 篇（最热🔥🔥）
- #foundation-MLIP：11 篇
- #ml4chem-general：11 篇
- #mol-design：7 篇
- #reaction-opt：6 篇
- #catalyst-ligand：5 篇
- #TS-search：4 篇
- #organocatalysis：0 篇（待补充）

**按月分布**：
- 月均：20.6 篇
- 峰值：4月 22 篇（生成模型爆发）
- 最低：1月、2月、6月各 20 篇

### 研究热度演进

```
Jan  ████   基础模型
Feb  ████   预训练
Mar  █████  GNN 竞争
Apr  ██████ 生成爆发 🔥
May  █████  量子化学转折
Jun  ████   AlphaFold3
Jul  ██████ 图注意成熟
Aug  █████  RL 赋能
```

## 🔧 技术栈

- **语言**：Markdown（论文归档）、JSON（索引）
- **自动化**：Claude Code Routine（云端 Agent）
- **搜索**：WebSearch API
- **版本控制**：Git + GitHub
- **时区**：Europe/Amsterdam（荷兰）

## 📝 待办事项

- [ ] 补充 #organocatalysis 方向论文（NHC、有机催化专题）
- [ ] 创建可视化仪表板（月度趋势图、热力图）
- [ ] 添加引用格式（BibTeX、RIS）
- [ ] 建立论文推荐系统（基于阅读历史）
- [ ] 开发浏览器插件（快速添加论文）
- [ ] 扩展 9 月及以后的自动化收集

## 🤝 贡献指南

欢迎补充论文！格式要求见 `papers/README.md`。

**快速贡献流程**：
1. Fork 本仓库
2. 创建分支 `feat/add-papers-YYYY-MM`
3. 编辑 `papers/2026-XX.md` 和 `papers/index.json`
4. 提交 Pull Request
5. 等待 Routine 验证与集成

## 📞 联系方式

- **项目维护**：[ElioChen](https://github.com/ElioChen)
- **论文库**：[AI4Chem Library](https://github.com/ElioChen/ai4chem-library)
- **自动化支持**：Claude Code

## 📄 许可证

MIT License — 自由使用、修改、分享

---

**最后更新**：2026-08-31 | **论文总数**：165 | **下次更新**：2026-09-03 (Routine 首次运行)
