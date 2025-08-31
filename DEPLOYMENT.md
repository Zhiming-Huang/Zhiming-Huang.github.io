# 🚀 GitHub Pages 部署指南

本文档详细说明如何将你的学术网站部署到GitHub Pages。

## 📋 前提条件

1. **GitHub账户** 和仓库设置
2. **自定义域名** (可选): `zhiminghuang.me`
3. **本地环境**: Python + Pelican

## 🎯 部署方式

### 方式一：自动部署 (推荐)

我们已经配置了GitHub Actions工作流，每次push到主分支时会自动部署。

#### 1. 推送代码到GitHub

```bash
# 初始化git仓库 (如果还没有)
git init
git add .
git commit -m "Initial commit: Academic website setup"

# 添加远程仓库 (替换为你的仓库地址)
git remote add origin https://github.com/zhiminghuang/zhiminghuang.github.io.git

# 推送到main分支
git push -u origin main
```

#### 2. 启用GitHub Pages

1. 进入你的GitHub仓库
2. 点击 **Settings** 标签
3. 在左侧菜单中找到 **Pages**
4. 在 **Source** 下选择 **GitHub Actions**
5. 保存设置

#### 3. 配置自定义域名 (可选)

1. 在Pages设置中，在 **Custom domain** 字段输入: `zhiminghuang.me`
2. 等待DNS检查完成
3. 勾选 **Enforce HTTPS**

### 方式二：本地构建测试

```bash
# 运行部署脚本
./deploy.sh

# 或者手动构建
source pelican-env/bin/activate
pelican content -s publishconf.py

# 本地预览
cd output
python -m http.server 8080
# 访问 http://localhost:8080
```

## 🔧 文件结构

```
website/
├── .github/workflows/deploy.yml    # GitHub Actions工作流
├── content/                        # 网站内容
│   ├── extra/CNAME                # 自定义域名配置
│   ├── pages/                     # 页面文件
│   └── files/                     # 静态文件
├── themes/modern-academic/         # 网站主题
├── pelicanconf.py                 # 开发配置
├── publishconf.py                 # 生产配置
└── deploy.sh                      # 本地部署脚本
```

## ⚙️ 关键配置文件

### publishconf.py
```python
SITEURL = "https://zhiminghuang.me"
RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True
```

### CNAME文件
```
zhiminghuang.me
```

## 🔄 日常工作流程

1. **本地开发**:
   ```bash
   source pelican-env/bin/activate
   pelican --listen --autoreload
   # 访问 http://localhost:8000
   ```

2. **发布更新**:
   ```bash
   git add .
   git commit -m "Update: describe your changes"
   git push origin main
   # GitHub Actions会自动部署
   ```

3. **检查部署**:
   - 在GitHub仓库的 **Actions** 标签查看部署状态
   - 访问 https://zhiminghuang.me 查看结果

## 🐛 故障排除

### 部署失败
1. 检查GitHub Actions日志
2. 确保所有依赖都在工作流中安装
3. 检查Python和Pelican版本兼容性

### 域名问题
1. 确保DNS记录正确配置:
   ```
   A记录: zhiminghuang.me -> 185.199.108.153
   A记录: zhiminghuang.me -> 185.199.109.153
   A记录: zhiminghuang.me -> 185.199.110.153
   A记录: zhiminghuang.me -> 185.199.111.153
   ```
2. 或使用CNAME记录指向: `username.github.io`

### 样式/功能异常
1. 检查SITEURL配置是否正确
2. 确保RELATIVE_URLS = False
3. 清除浏览器缓存

## 📊 性能优化

- **CDN**: GitHub Pages自带CDN
- **缓存**: 静态文件自动缓存
- **压缩**: Gzip压缩自动启用
- **HTTPS**: 自动SSL证书

## 🔒 安全设置

- 强制HTTPS (在Pages设置中启用)
- 依赖自动更新 (通过Dependabot)
- Actions权限最小化

## 📈 监控与分析

考虑添加:
- Google Analytics
- Google Search Console
- 性能监控工具

---

## 🎉 快速开始

```bash
# 1. 本地测试
./deploy.sh

# 2. 推送到GitHub
git add .
git commit -m "Deploy academic website"
git push origin main

# 3. 等待几分钟，访问你的网站!
# https://zhiminghuang.me
```

**恭喜！你的学术网站现在已经部署到GitHub Pages了！** 🚀
