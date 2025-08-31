# 🚀 Publications Development Guide

## 🎯 **原生Pelican工作流 (推荐)**

### **标准开发命令**
```bash
source pelican-env/bin/activate
pelican --listen --autoreload
```

**就这么简单！** 🎉

## 🔧 **工作原理**

1. **编辑 `content/pages/publications.md`**
2. **保存文件**
3. **Pelican自动检测变化**
4. **插件自动同步到JSON**
5. **浏览器自动刷新**

### **📄 真正的自动化流程**

```
📝 你编辑 publications.md
    ↓ (保存文件)
🔍 Pelican检测文件变化
    ↓ (开始重新构建)
🔄 插件interceptor content_object_init信号
    ↓ (检测到publications.md被处理)
📄 自动运行sync_publications()
    ↓ (YAML → JSON转换)
🌐 Pelican完成构建
    ↓ (复制新JSON到output)
🔄 浏览器自动刷新显示更新
```

## 📂 文件结构

```
📁 content/pages/publications.md     ← 编辑这个文件
       ↓ (插件自动监听)
📁 themes/static/data/publications.json   ← 自动生成
       ↓ (Pelican自动复制)
📁 output/theme/data/publications.json    ← 网站读取
       ↓ (缓存破坏确保更新)
📁 网站显示最新内容 ✨
```

## 📝 Publications.md 格式说明

### **链接分类系统**

所有链接统一放在`links`下，通过`type`字段来区分颜色：

```yaml
- title: "Your Paper Title"
  authors: "**Your Name**, Co-author"
  venue: "Conference/Journal Name"
  date: "2025-05"
  type: "conference"
  status: "Published"
  links:
    # 出版方链接 (绿色按钮)
    - text: "IEEE"
      url: "https://doi.org/10.1109/..."
      type: "publisher"
    - text: "DOI"
      url: "https://doi.org/..."
      type: "doi"
      
    # 完整版本链接 (红色按钮) - 包含完整证明
    - text: "Extended PDF"
      url: "full_version.pdf"
      type: "full"
    - text: "arXiv"
      url: "https://arxiv.org/abs/..."
      type: "arxiv"
    - text: "Technical Report"
      url: "tech_report.pdf"
      type: "technical-report"
      
    # 其他材料 (蓝色按钮)
    - text: "Slides"
      url: "slides.pdf"
      type: "slides"
    - text: "Poster"
      url: "poster.pdf"
      type: "poster"
    - text: "Code"
      url: "https://github.com/..."
      type: "code"
    
    # 没有type字段的链接默认为蓝色
    - text: "PDF"
      url: "paper.pdf"
```

### **链接类型说明**

- **type: "publisher", "ieee", "acm", "springer", "doi"** → 🟢 绿色按钮
- **type: "full", "arxiv", "extended", "technical-report"** → 🔴 红色按钮  
- **其他type或无type** → 🔵 蓝色按钮

### **完整证明PDF的建议名称**
- `Extended PDF` - 扩展版PDF
- `Full Paper` - 完整论文
- `Technical Report` - 技术报告
- `Complete Version` - 完整版本

## 🔧 技术细节

### **信号机制**
- 使用Pelican原生的 `content_object_init` 信号
- 每当 `publications.md` 被处理时自动触发同步
- 避免文件监听线程在多进程环境的问题
- 与Pelican的autoreload完美集成

### **缓存破坏**
- `publications.html` 中的JavaScript自动添加时间戳
- 确保浏览器总是获取最新的JSON数据
- 无需手动清除缓存

## 📋 命令参考

| 命令 | 用途 |
|------|------|
| `pelican --listen --autoreload` | **推荐开发方式** |
| `python sync_publications.py` | 手动同步（调试用） |
| `pelican content` | 构建网站（部署用） |

## 🔍 故障排除

### **问题**: 自动同步不工作
**解决方案**: 
1. 确保在 `content/pages/publications.md` 中编辑
2. 确保保存文件后看到Pelican的 "re-generating..." 消息
3. 检查插件是否显示 "✅ Synced X publications"

### **问题**: 浏览器显示旧内容
**解决方案**:
1. 硬刷新: `Ctrl+Shift+R` (Mac: `Cmd+Shift+R`)
2. 检查控制台网络请求中JSON是否带时间戳

### **问题**: 端口占用
**解决方案**:
```bash
pkill -f "pelican.*listen"
lsof -ti:8000 | xargs kill -9
pelican --listen --autoreload
```

## ✅ **优势**

- ✅ **原生体验**：标准Pelican命令
- ✅ **真正自动化**：保存即同步
- ✅ **稳定可靠**：使用Pelican信号机制
- ✅ **无额外进程**：完全集成到Pelican
- ✅ **生产就绪**：同样的机制用于构建

## 🎯 **这就是你要的工作流！**

**一个命令启动开发：**
```bash
pelican --listen --autoreload
```

**然后就可以专心编辑publications.md，其他都是自动的！** 🚀