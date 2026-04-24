# 05 Pages Setup（根目录 + app 子目录）

## 现状

- 真正应用入口：`app/index.html`
- 根目录入口：`index.html`（自动跳转到 `app/index.html`）

## 本地启动

```bash
python3 -m http.server 8787
```

访问：

- `http://localhost:8787/`
- `http://localhost:8787/app/index.html`

## GitHub Pages 配置步骤

1. 打开仓库 `Settings` → `Pages`
2. `Build and deployment` 选择 `Deploy from a branch`
3. Branch 选发布分支（例如 `main`）
4. Folder 选 `/(root)`
5. 保存并等待 Pages 发布

## 为什么选 /(root)

因为根目录已有 `index.html` 跳转页，用户打开站点根地址即可自动进入 `app/index.html`，不用额外 workflow。
