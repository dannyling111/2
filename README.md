# AI Venture Operating System (AVOS)


> ⚠️ 如果你看到的是这份 README 文本，而不是表单页面，说明你打开错页面了。
> 请直接打开：`/index.html` 或 `/app/index.html`（通过本地 HTTP 服务访问）。


你问得非常关键：**要不要继续多跑几轮？**

我把系统升级成了“可配置轮次 + 收敛判断”，不再只固定 5 轮。

## 现在能做什么

- 前端可选 `5~20` 轮自动迭代。
- CLI 支持 `--rounds` 参数。
- 每次运行都会给出“继续跑”还是“已收敛”的建议。

## 前端体验

```bash
cd app
python3 -m http.server 8787
```

打开 <http://localhost:8787>：
- 设置“自动迭代轮数（5-20）”
- 点击 `自动迭代 N 轮（无人干预）`

## CLI 体验

```bash
python3 scripts/autopilot_iterate.py --rounds 5
python3 scripts/autopilot_iterate.py --rounds 12
```

## 我的当前判断（基于现有规则引擎）

- 前几轮（通常 1~4 轮）提升明显。
- 之后容易进入平台期。
- 到平台期后，继续增加轮次收益有限，应切换到“真实用户数据驱动”的优化。

## 核心文件

- `app/index.html`：可配置轮数的自动迭代 UI。
- `scripts/autopilot_iterate.py`：支持 `--rounds` 和收敛建议的 CLI 引擎。
- `docs/03_mvp_plan.md`：v0.3 迭代标准与建议。


## 实测结论（你问的“最后结果”）

我已实际运行 `5 / 8 / 12 / 20` 轮：

- 最优轮次稳定在 `Round 4`
- 最优得分稳定在 `8.29`
- `8` 轮之后基本收敛

详细数据见：`docs/04_run_summary.md`


## 怎么打开网页（你这个问题的直接答案）

### 本地打开

在仓库根目录执行：

```bash
python3 -m http.server 8787
```

然后访问：

- `http://localhost:8787/`（现在根目录 `index.html` 会自动跳转到 `app/index.html`）
- 或直接 `http://localhost:8787/app/index.html`

### GitHub Pages 设置（Page setting）

因为现在根目录已经有 `index.html` 跳转页，最简单配置是：

1. GitHub 仓库 → `Settings` → `Pages`
2. `Build and deployment` 里选择：
   - `Source`: **Deploy from a branch**
   - `Branch`: **main**（或你的发布分支）
   - `Folder`: **/(root)**
3. 保存后等待发布完成。

发布后访问你的 Pages 链接即可（会自动跳到 `/app/index.html`）。
