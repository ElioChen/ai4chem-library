# 贡献指南 — AI4Chem 论文库

感谢你对 AI4Chem 文献库的兴趣！本文档说明如何为项目贡献新论文。

## 🎯 贡献类型

### 1. 添加论文（最常见）

如果你发现了相关的分子 ML 论文，欢迎补充！

**要求**：
- 论文来自 arXiv、ChemRxiv、bioRxiv、Nature、Science、ACS 等学术平台
- 与 7 大研究方向之一相关（见下文）
- 有 DOI 或 arXiv ID（便于去重）

### 2. 改进现有条目

- 补充缺失的作者信息
- 优化摘要表述
- 纠正标签分类
- 增加关键词或注释

### 3. 改进自动化流程

- 优化 `ROUTINE_PROMPT.md` 的关键词
- 增加新的数据源
- 改进搜索策略

## 📋 研究方向分类

提交前，请根据论文内容选择最相关的标签（可多选）：

| 标签 | 说明 | 示例关键词 |
|------|------|-----------|
| `#foundation-MLIP` | Foundation 模型、MLIP、DFT 替代 | neural network potential, foundation model, NN-xTB |
| `#property-pred` | 分子性质预测 | HOMO-LUMO, toxicity, binding affinity, solubility |
| `#reaction-opt` | 化学反应优化 | yield prediction, condition optimization, selectivity |
| `#mol-design` | 分子生成与设计 | diffusion model, generative model, molecular generation |
| `#catalyst-ligand` | 催化剂与配体设计 | catalyst discovery, ligand design, screening |
| `#TS-search` | 反应路径、逆合成 | retrosynthesis, transition state, reaction pathway |
| `#organocatalysis` | 有机催化 | NHC carbene, organic catalyst, asymmetric catalysis |
| `#ml4chem-general` | 其他交叉领域 | multi-task learning, transfer learning, benchmark |

## 📝 论文条目格式

### Markdown 格式（在月度文件中）

```markdown
### [论文完整标题](https://arxiv.org/abs/XXXX.XXXXX)
**作者**：First Author et al.  
**发表年份**：2026  
**标签**：#direction1, #direction2  
**摘要**：用自己的话写 3-5 句。解释方法创新、结果、意义。
```

**要点**：
- 标题与 URL 必须对应
- 作者：列出前 2-3 名 + "et al."
- 摘要：NOT 逐字引用原文 abstract，要自己转述、指出创新点
- 标签：根据内容选择，可多选

### JSON 格式（index.json）

```json
{
  "id": "arXiv:2601.12345",
  "title": "论文标题",
  "authors": "Author A, Author B et al.",
  "source": "arxiv",
  "url": "https://arxiv.org/abs/2601.12345",
  "date_added": "2026-01-15",
  "tags": ["foundation-MLIP", "property-pred"]
}
```

**字段说明**：
- `id`：唯一标识（优先 arXiv ID，次选 DOI）
- `source`：arxiv / chemrxiv / biorxiv / nature / science / acs / other
- `date_added`：YYYY-MM-DD 格式
- `tags`：数组，选择 1-3 个最相关标签

## 🚀 贡献流程

### 方式 A：直接编辑（GitHub Web UI）

适合添加 1-2 篇论文。

1. 打开对应月份的文件（如 `papers/2026-09.md`）
2. 点击编辑（✏️ 图标）
3. 在适当星期区块添加论文条目
4. 同时编辑 `papers/index.json`（添加去重记录）
5. 编辑 `papers/README.md`（更新统计）
6. 提交 Commit（描述：`papers: add 1 entry (2026-09-XX)`）

### 方式 B：本地编辑 + Git（批量贡献）

适合添加 5+ 篇论文或改进自动化配置。

```bash
# 1. Fork & Clone
git clone https://github.com/YOUR_USERNAME/ai4chem-library.git
cd ai4chem-library

# 2. 创建分支
git checkout -b feat/add-papers-2026-09
# 或改进 Routine
git checkout -b feat/improve-routine

# 3. 编辑文件
# - papers/2026-09.md（添加论文）
# - papers/index.json（添加索引）
# - papers/README.md（更新统计）
# - ROUTINE_PROMPT.md（如改进关键词）

# 4. 测试（可选）
python scripts/validate_papers.py  # 校验格式

# 5. 提交
git add papers/ ROUTINE_PROMPT.md
git commit -m "papers: add 5 entries from September 2026 (2026-09-XX)

- Topic 1: Paper title 1
- Topic 2: Paper title 2
- ..."

# 6. Push & 创建 PR
git push origin feat/add-papers-2026-09
# 在 GitHub 上创建 Pull Request
```

### 方式 C：自动化报告

如果你发现了大量相关论文，也可以提交一个 GitHub Issue，格式如下：

```markdown
## 新增论文批次报告

**月份**：2026-09  
**数量**：10 篇  
**来源**：arXiv cs.LG  
**主题**：Graph neural networks for molecules

### 论文列表
1. [标题](URL) — 作者 — 标签
2. [标题](URL) — 作者 — 标签
...
```

## ✅ 审查标准

贡献者提交的 PR 会被审查，标准包括：

- ✅ **去重**：index.json 中无重复 ID
- ✅ **格式**：Markdown 与 JSON 格式正确
- ✅ **信息完整**：有作者、URL、摘要
- ✅ **标签准确**：选择最相关的 1-3 个标签
- ✅ **摘要质量**：3-5 句，解释创新点与意义
- ✅ **统计更新**：README.md 的数字与新增论文相符

## 🤖 自动化 Routine

系统每天 06:00 荷兰时间自动执行收集。如果想改进自动化：

**编辑** `papers/ROUTINE_PROMPT.md`：
- 扩展关键词覆盖
- 添加新的数据源
- 改进标签判断逻辑
- 优化摘要生成

**测试**：在 Routine 管理页面点击"Run Now"手动触发一次。

## 📊 数据质量指南

为保持库的高质量，请遵循：

### ✅ DO（要做）

- ✅ 自己阅读论文后再添加
- ✅ 用自己理解的话写摘要
- ✅ 准确分类到对应研究方向
- ✅ 检查是否已在 index.json 中
- ✅ 遵循 Commit 消息格式

### ❌ DON'T（不要做）

- ❌ 盲目复制摘要（违反版权）
- ❌ 添加与分子 ML 无关的论文
- ❌ 同一篇论文用不同 ID 重复添加
- ❌ 为了凑数添加低质量论文
- ❌ 未检查就提交格式错误的条目

## 🐛 Bug 报告与改进建议

发现了问题？

1. **检查** [Issues](https://github.com/ElioChen/ai4chem-library/issues) 是否已有相同报告
2. **创建新 Issue**，包括：
   - 问题描述（具体、可复现）
   - 预期行为 vs 实际行为
   - 相关论文 ID 或月份
   - 环境信息（Git 版本、操作系统等）

3. **改进建议**也欢迎，如：
   - 新增研究方向标签
   - 改进自动化检索策略
   - 增加统计图表
   - 优化搜索性能

## 📞 联系与讨论

- **Discussions**（GitHub）：讨论研究方向、热点论文
- **Issues**：报告 Bug、提交改进建议
- **Email**：[项目维护者邮箱]

## 🎓 学习资源

想了解更多分子 ML？推荐阅读本库中的 landmark 论文：

- **Foundation Models**：ChemBERTa-2, ∇²DFT
- **Molecular Design**：DrugDiff, ALCHIMIA
- **Graph Networks**：KA-GNN, FragNet
- **Quantum Chemistry**：NN-xTB
- **Protein Structures**：AlphaFold3

---

感谢贡献！每一篇高质量论文都帮助社区更好地理解分子 ML 的最前沿进展。🙏
