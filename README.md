# 🎓 Modern Academic Website

A beautiful, responsive, and feature-rich academic website built with Pelican static site generator. Designed specifically for researchers, academics, and students who need a professional online presence.

[![Deploy Status](https://github.com/zhiming-huang/zhiming-huang.github.io/workflows/Deploy%20to%20GitHub%20Pages/badge.svg)](https://github.com/zhiming-huang/zhiming-huang.github.io/actions)
[![Live Demo](https://img.shields.io/badge/demo-zhiminghuang.me-blue)](https://zhiminghuang.me)

## ✨ Key Features

### 🎨 **Modern Design System**
- **Clean & Professional**: Minimalist design focused on content readability
- **Custom Color Scheme**: Carefully chosen academic colors with consistent theming
- **Typography**: Optimized font selections for academic content
- **Visual Hierarchy**: Clear information architecture for academic profiles

### 📱 **Fully Responsive**
- **Mobile-First**: Optimized for all devices from phones to desktops
- **Adaptive Layouts**: Content reflows intelligently across screen sizes
- **Touch-Friendly**: Enhanced mobile navigation and interactions
- **Cross-Browser**: Compatible with all modern browsers

### 🔍 **Advanced Search System**
- **Glass Morphism UI**: Beautiful transparent search overlay with blur effects
- **Real-Time Filtering**: Instant search results as you type
- **Smart Search**: Searches across titles, authors, venues, and keywords
- **Category Filters**: Filter publications by type (conference, journal, in progress)
- **Collapsible Interface**: Space-efficient design that expands on demand

### 📚 **Dynamic Publications Management**
- **Structured Data**: YAML-based publication entries with rich metadata
- **Auto-Sync**: Automatic conversion from Markdown to web-ready JSON
- **Live Updates**: Publications update automatically during development
- **Rich Metadata**: Support for authors, venues, dates, links, status, and awards
- **Smart Links**: Automatic file path resolution and categorized link styling
- **Citation Ready**: Properly formatted academic citations

### 🏠 **Comprehensive Academic Profile**
- **Profile Section**: Professional photo with click-to-enlarge modal
- **About Integration**: Seamless content flow from personal info to research
- **Social Integration**: Academic social links (Google Scholar, GitHub, LinkedIn, CV)
- **News Feed**: Collapsible recent updates with "Show All" functionality
- **Research Showcase**: Dedicated research page with categorized projects
- **CV Integration**: Direct CV download with professional file icon

### 🚀 **Developer Experience**
- **Native Pelican Workflow**: Built-in plugin system for seamless development
- **Hot Reload**: Instant preview during development
- **GitHub Actions**: Automated deployment to GitHub Pages
- **Plugin Architecture**: Custom publications sync with native Pelican signals
- **Error Handling**: Robust error handling and graceful fallbacks
- **Documentation**: Comprehensive development and deployment guides

### 🎯 **Academic-Specific Features**
- **Research Categorization**: Organized research themes with related publications
- **Publication Status**: Track submission status, revisions, and acceptances
- **Award Highlighting**: Special styling for best paper awards and honors
- **Multi-Format Support**: PDFs, slides, posters, videos, and datasets
- **Conference Integration**: Proper venue formatting and date handling
- **Collaboration Credits**: Proper author attribution and co-author highlighting

## 🛠️ Technology Stack

- **Static Site Generator**: [Pelican](https://getpelican.com/)
- **Frontend Framework**: [Bootstrap 5](https://getbootstrap.com/)
- **Icons**: [Bootstrap Icons](https://icons.getbootstrap.com/)
- **Deployment**: [GitHub Pages](https://pages.github.com/) with GitHub Actions
- **Content Format**: Markdown with YAML front matter
- **Styling**: Modern CSS with custom properties and animations
- **Build System**: Python-based with automated dependency management

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Git
- Text editor or IDE

### Local Development
```bash
# Clone the repository
git clone https://github.com/your-username/your-repo.git
cd your-repo

# Set up virtual environment
python -m venv pelican-env
source pelican-env/bin/activate  # On Windows: pelican-env\Scripts\activate

# Install dependencies
pip install pelican[markdown] beautifulsoup4 pyyaml

# Start development server with auto-reload
pelican --listen --autoreload

# Visit: http://localhost:8000
```

### Content Management
```bash
# Edit your profile information
vim content/index.md

# Add publications
vim content/pages/publications.md

# Update research information
vim content/pages/research.md

# Add news items
vim content/news.md
```

### Deployment
```bash
# Test production build
./deploy.sh

# Deploy to GitHub Pages (automated)
git add .
git commit -m "Update content"
git push origin main
```

## 📁 Project Structure

```
├── content/                    # Site content
│   ├── index.md               # Home page with profile info
│   ├── news.md                # News and updates
│   ├── teaching.md            # Teaching experience
│   ├── service.md             # Academic service
│   ├── pages/                 # Static pages
│   │   ├── publications.md    # Publications data (YAML)
│   │   └── research.md        # Research overview
│   ├── files/                 # Static files (PDFs, CVs)
│   └── images/                # Images and photos
├── themes/modern-academic/     # Custom theme
│   ├── templates/             # Jinja2 templates
│   └── static/               # CSS, JS, and assets
├── plugins/                   # Custom Pelican plugins
├── .github/workflows/         # GitHub Actions deployment
├── pelicanconf.py            # Development configuration
├── publishconf.py            # Production configuration
└── deploy.sh                 # Local deployment script
```

## 🎨 Customization

### Colors and Theming
The theme uses CSS custom properties for easy customization:

```css
:root {
    --custom-text-heading: #286687;  /* Main heading color */
    --custom-primary: #007bff;       /* Primary accent color */
}
```

### Adding Publications
Publications are managed in `content/pages/publications.md` using YAML format:

```yaml
Publications:
  - title: "Your Paper Title"
    authors: "**Your Name**, Co-Author Name"
    venue: "Conference Name (CONF 2024)"
    date: "2024-05"
    type: "conference"
    status: "Published"
    links:
      - text: "PDF"
        url: "your-paper.pdf"
        type: "full"
      - text: "IEEE"
        url: "https://doi.org/..."
        type: "publisher"
```

### Responsive Breakpoints
The theme includes comprehensive responsive design:
- **Mobile**: ≤575px
- **Tablet**: 576px - 991px  
- **Desktop**: 992px - 1399px
- **Large Desktop**: ≥1400px

## 📖 Documentation

- **[Deployment Guide](DEPLOYMENT.md)**: Comprehensive GitHub Pages setup
- **[Development Guide](README_DEV.md)**: Local development workflow
- **[Theme Customization](docs/CUSTOMIZATION.md)**: Styling and layout guides
- **[Content Management](docs/CONTENT.md)**: Adding and managing content

## 🔗 Live Demo

Visit the live website: **[https://zhiminghuang.me](https://zhiminghuang.me)**

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Pelican](https://getpelican.com/) static site generator
- Styled with [Bootstrap 5](https://getbootstrap.com/) framework
- Icons from [Bootstrap Icons](https://icons.getbootstrap.com/)
- Deployed on [GitHub Pages](https://pages.github.com/)
- Inspired by modern academic website designs

## 📧 Contact

**Zhiming Huang**  
PhD, University of Victoria   
🌐 Website: [https://zhiminghuang.me](https://zhiminghuang.me)  

---

⭐ **Star this repository if you find it useful!** ⭐