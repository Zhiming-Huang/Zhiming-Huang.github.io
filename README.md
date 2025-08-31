# 📚 Academic Website

Modern, responsive academic website built with Pelican and deployed on GitHub Pages.

## 🌟 Features

- **Modern Design**: Clean, professional academic layout
- **Responsive**: Optimized for all devices
- **Dynamic Publications**: Auto-sync from markdown to web
- **Advanced Search**: Glass morphism search with real-time filtering
- **GitHub Pages Ready**: Automated deployment workflow

## 🚀 Quick Start

### Local Development
```bash
# Activate environment
source pelican-env/bin/activate

# Start development server
pelican --listen --autoreload

# Visit: http://localhost:8000
```

### Deploy to GitHub Pages
```bash
# Build and test locally
./deploy.sh

# Push to GitHub (auto-deploys)
git add .
git commit -m "Update website"
git push origin main
```

## 📖 Documentation

- **[Deployment Guide](DEPLOYMENT.md)**: Complete GitHub Pages setup
- **[Development Guide](README_DEV.md)**: Local development workflow

## 🔗 Live Website

Visit: [https://zhiminghuang.me](https://zhiminghuang.me)

---

**Built with ❤️ using Pelican & GitHub Pages**