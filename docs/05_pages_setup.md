# 05 Pages Setup（根目录 + app 子目录）

## 现状

- `index.html`（根目录）= 可直接运行的应用页面
- `app/index.html`（子目录）= 同一应用页面副本

> 这样做的目的是避免“只看到 README 文本、不见表单 UI”的混淆。

## 本地启动

```bash
python3 -m http.server 8787
```

访问任一地址：

- `http://localhost:8787/`
- `http://localhost:8787/index.html`
- `http://localhost:8787/app/index.html`

## GitHub Pages 配置步骤

1. 打开仓库 `Settings` → `Pages`
2. `Build and deployment` 选择 `Deploy from a branch`
3. Branch 选发布分支（例如 `main`）
4. Folder 选 `/(root)`
5. 保存并等待 Pages 发布

## 常见错误

- 看到的是 README 文本：说明你打开了 README 页面而不是站点首页。
- 正确入口始终是站点根地址（或 `index.html`）。
