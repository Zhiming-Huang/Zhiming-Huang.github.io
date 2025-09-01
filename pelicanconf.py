AUTHOR = 'Zhiming Huang'
SITENAME = "Zhiming's Page"
SITEURL = ""

# Academic Profile Settings
ACADEMIC_TITLE = "PhD"  # PhD, PhD Candidate, Professor, etc.
ACADEMIC_POSITION = "University of Victoria, BC, Canada"
ACADEMIC_DEPARTMENT = "Computer Science"
RESEARCH_INTERESTS = ["Online Learning", "Bandit Algorithms", "Game Theory", "Computer Networks", "Machine Learning"]

# SEO Settings
SITE_DESCRIPTION = f"{ACADEMIC_TITLE} in {ACADEMIC_DEPARTMENT} specializing in {', '.join(RESEARCH_INTERESTS[:3]).lower()} with applications to computer networks. University of Victoria researcher."
SITE_KEYWORDS = f"{AUTHOR}, {ACADEMIC_DEPARTMENT.lower()}, {', '.join([interest.lower() for interest in RESEARCH_INTERESTS])}, University of Victoria, {ACADEMIC_TITLE.lower()} researcher"

# Analytics (uncomment and add your tracking ID when ready)
# GOOGLE_ANALYTICS = "G-XXXXXXXXXX"
# GOOGLE_TAG_MANAGER = "GTM-XXXXXXX"

PATH = "content"

TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme settings
THEME = 'themes/modern-academic'
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Menu items - simplified structure
MENUITEMS = (
    ('Home', '/'),
    ('Research', '/pages/research.html'),
    ('Publications', '/pages/publications.html'),
)

# Social links - match the reference website
SOCIAL = (
    ('Google Scholar', 'https://scholar.google.com/citations?user=YOUR_USER_ID'),
    ('GitHub', 'https://github.com/zhiminghuang'),
    ('LinkedIn', 'https://linkedin.com/in/zhiminghuang'),
)

# Page settings
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'



# Article settings (for news/blog posts)
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

# Static paths
STATIC_PATHS = ['images', 'files', 'extra/CNAME', 'extra/robots.txt', 'extra/sitemap.xml']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/sitemap.xml': {'path': 'sitemap.xml'}
}

DEFAULT_PAGINATION = False

# Plugin configuration
PLUGIN_PATHS = ['plugins']
PLUGINS = ['publications_sync']

# Template context variables
EXTRA_CONTEXT = {
    'ACADEMIC_TITLE': ACADEMIC_TITLE,
    'ACADEMIC_POSITION': ACADEMIC_POSITION,
    'ACADEMIC_DEPARTMENT': ACADEMIC_DEPARTMENT,
    'RESEARCH_INTERESTS': RESEARCH_INTERESTS,
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
