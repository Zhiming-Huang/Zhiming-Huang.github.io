# 配置指南 - 学术网站个性化设置

## 🎯 主要配置文件

### 1. `pelicanconf.py` - 全局配置

```python
# 基本信息
AUTHOR = 'Your Name'
SITENAME = "Your Name - Academic Researcher"

# 学术身份配置
ACADEMIC_TITLE = "PhD"  # 可选: PhD, PhD Candidate, Professor, Postdoc, MSc, etc.
ACADEMIC_POSITION = "Your University, Location"
ACADEMIC_DEPARTMENT = "Your Department"
RESEARCH_INTERESTS = [
    "Your Research Area 1", 
    "Your Research Area 2", 
    "Your Research Area 3"
]
```

### 2. `content/index.md` - 个人信息

```markdown
Title: Home
Profile_image: your_photo.jpg
Full_name: Your Full Name (中文名)
Position: PhD, Your University, Location
Google_scholar: https://scholar.google.com/citations?user=YOUR_ID
Github: https://github.com/yourusername
Linkedin: https://linkedin.com/in/yourusername
CV: your_cv.pdf

## About
Your detailed biography and research description...
```

## 🔧 可配置参数详解

### 学术头衔选项 (ACADEMIC_TITLE)
- `"PhD"` - 已获得博士学位
- `"PhD Candidate"` - 博士候选人
- `"PhD Student"` - 博士生
- `"Postdoc"` - 博士后研究员
- `"Professor"` - 教授
- `"Assistant Professor"` - 助理教授
- `"Associate Professor"` - 副教授
- `"Research Scientist"` - 研究科学家
- `"MSc"` - 硕士
- `"MSc Student"` - 硕士生

### 位置信息 (ACADEMIC_POSITION)
```python
# 示例格式
ACADEMIC_POSITION = "University of Victoria, BC, Canada"
ACADEMIC_POSITION = "Stanford University, CA, USA"
ACADEMIC_POSITION = "University of Cambridge, UK"
ACADEMIC_POSITION = "Tsinghua University, Beijing, China"
```

### 研究兴趣 (RESEARCH_INTERESTS)
```python
# 计算机科学示例
RESEARCH_INTERESTS = [
    "Machine Learning",
    "Computer Vision", 
    "Natural Language Processing",
    "Artificial Intelligence",
    "Deep Learning"
]

# 数学示例
RESEARCH_INTERESTS = [
    "Algebraic Geometry",
    "Number Theory",
    "Differential Equations",
    "Mathematical Analysis"
]

# 物理示例
RESEARCH_INTERESTS = [
    "Quantum Physics",
    "Condensed Matter Physics",
    "Theoretical Physics",
    "Particle Physics"
]
```

## 🎨 页面个性化

### 社交链接配置
在 `content/index.md` 中配置：

```markdown
Google_scholar: https://scholar.google.com/citations?user=YOUR_ID
Github: https://github.com/yourusername
Linkedin: https://linkedin.com/in/yourusername
ORCID: https://orcid.org/0000-0000-0000-0000
ResearchGate: https://www.researchgate.net/profile/Your_Profile
CV: your_cv_file.pdf
```

### 个人照片设置
```markdown
Profile_image: profile.jpeg  # 文件放在 content/images/ 目录
Profile_image_caption: 照片说明文字
```

## 📊 SEO自动优化

配置好以上参数后，系统会自动生成：

### 动态网站描述
```python
# 自动生成的描述
SITE_DESCRIPTION = f"{ACADEMIC_TITLE} in {ACADEMIC_DEPARTMENT} specializing in {research_areas}..."
```

### 动态关键词
```python
# 自动生成的关键词
SITE_KEYWORDS = f"{AUTHOR}, {department}, {research_interests}..."
```

### 结构化数据
- 学术身份信息 (JSON-LD)
- 研究领域标签
- 机构关联信息

## 🔄 配置更新流程

### 1. 更新学术状态
```python
# 从PhD Candidate升级为PhD
ACADEMIC_TITLE = "PhD"  # 修改这一行

# 更新位置（如果换工作）
ACADEMIC_POSITION = "New University, New Location"
```

### 2. 更新个人信息
```markdown
# content/index.md
Position: PhD, New University, New Location
```

### 3. 更新研究兴趣
```python
# 添加新的研究领域
RESEARCH_INTERESTS = [
    "Existing Area 1",
    "Existing Area 2", 
    "New Research Area"  # 新增
]
```

## 🎯 不同学术阶段的配置示例

### 博士生
```python
ACADEMIC_TITLE = "PhD Student"
ACADEMIC_POSITION = "University of Victoria, BC, Canada"
```

### 博士候选人
```python
ACADEMIC_TITLE = "PhD Candidate"
ACADEMIC_POSITION = "University of Victoria, BC, Canada"
```

### 新晋博士 ✅ 当前配置
```python
ACADEMIC_TITLE = "PhD"
ACADEMIC_POSITION = "University of Victoria, BC, Canada"
```

### 博士后
```python
ACADEMIC_TITLE = "Postdoc"
ACADEMIC_POSITION = "Stanford University, CA, USA"
```

### 助理教授
```python
ACADEMIC_TITLE = "Assistant Professor"
ACADEMIC_POSITION = "University of Toronto, ON, Canada"
ACADEMIC_DEPARTMENT = "Computer Science"
```

## 📝 注意事项

1. **一致性**: 确保 `pelicanconf.py` 和 `content/index.md` 中的信息保持一致
2. **SEO优化**: 修改配置后，网站的SEO标签会自动更新
3. **国际化**: 支持中英文混合显示
4. **灵活性**: 所有硬编码参数都已改为可配置
5. **向后兼容**: 如果没有设置某些参数，会使用合理的默认值

---

**提示**: 每次更新配置后，重新生成网站以使更改生效：
```bash
pelican content -s pelicanconf.py
```
