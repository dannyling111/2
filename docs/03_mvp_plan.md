# 03 MVP Plan（v0.3：可配置轮次 + 收敛判断）

## 目标

在无人干预自动迭代基础上，再提升两点：

1. 迭代轮次可配置（5~20）
2. 自动判断“是否还值得继续多跑”

## 当前完成度

- [x] 单页输入/输出
- [x] 自动 N 轮迭代（前端 5~20）
- [x] 自动 N 轮迭代（CLI `--rounds`）
- [x] 收敛建议（继续跑 / 切换数据优化）
- [ ] 真实用户反馈接入
- [ ] 自动部署与观测面板

## 使用方式

### 前端

```bash
cd app
python3 -m http.server 8787
```

打开：<http://localhost:8787>

### CLI

```bash
python3 scripts/autopilot_iterate.py --rounds 5
python3 scripts/autopilot_iterate.py --rounds 12
```

## 迭代流程

1. Proposal：生成初始方案。
2. Scoring：7 维评分。
3. Critique：对低分项给出可执行批评。
4. Revision：自动改写方案。
5. Selection：选择最优轮次。
6. Convergence Check：判断是否仍值得继续增轮。

## v0.3 验证指标

- 第 N 轮得分 >= 第 1 轮得分
- 收敛判断可输出明确建议
- 报告可复制为 Markdown
