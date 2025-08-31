# Zhiming's Personal Website

This is the source code for Zhiming Huang's personal academic website, built with [Pelican](https://getpelican.com/) and deployed on GitHub Pages.

## Website: [https://zhiminghuang.me](https://zhiminghuang.me)

## Features

- **Academic Portfolio**: Research interests, publications, and CV
- **Static Site Generation**: Built with Pelican for fast, secure hosting
- **Automatic Deployment**: GitHub Actions workflow for seamless updates
- **Custom Domain**: Hosted on GitHub Pages with custom domain support

## Local Development

### Prerequisites

- Python 3.11+
- Git

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/website.git
cd website
```

2. Create and activate virtual environment:
```bash
python3 -m venv pelican-env
source pelican-env/bin/activate  # On Windows: pelican-env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Generate the site:
```bash
pelican content
```

5. Start local development server:
```bash
pelican --listen
```

Visit [http://localhost:8000](http://localhost:8000) to view the site.

### Development Workflow

1. **Edit Content**: Modify files in the `content/` directory
2. **Regenerate**: Run `pelican content` to rebuild the site
3. **Preview**: Use `pelican --listen` for live preview
4. **Deploy**: Push changes to trigger automatic deployment

## Content Structure

```
content/
├── index.md              # Homepage
├── pages/
│   ├── research.md       # Research interests
│   ├── publications.md   # Publication list
│   └── cv.md            # Curriculum Vitae
├── images/              # Static images
└── extra/
    └── CNAME           # Custom domain configuration
```

## Configuration

- `pelicanconf.py`: Development configuration
- `publishconf.py`: Production configuration
- `.github/workflows/deploy.yml`: GitHub Actions deployment

## Deployment

The site automatically deploys to GitHub Pages when changes are pushed to the main branch. The deployment process:

1. GitHub Actions triggers on push to main
2. Python environment is set up
3. Dependencies are installed
4. Site is generated with production settings
5. Generated files are pushed to `gh-pages` branch
6. GitHub Pages serves the site

## Customization

### Adding New Pages

1. Create a new `.md` file in `content/pages/`
2. Add appropriate metadata (Title, Date, Slug)
3. Update navigation in `pelicanconf.py` if needed

### Modifying Themes

The site uses Pelican's default theme with custom CSS. To customize:

1. Create a custom theme in `themes/` directory
2. Update `THEME` setting in `pelicanconf.py`
3. Rebuild the site

### Adding Static Files

1. Place files in `content/images/` or `content/extra/`
2. Configure `STATIC_PATHS` in `pelicanconf.py`
3. Use `EXTRA_PATH_METADATA` for special handling

## License

This website source code is available under the MIT License. Content is © Zhiming Huang.

## Contact

For questions about this website or its content, please contact:
- Email: zhiming@uvic.ca
- GitHub: [@zhiminghuang](https://github.com/zhiminghuang)
- LinkedIn: [zhiminghuang](https://linkedin.com/in/zhiminghuang)
