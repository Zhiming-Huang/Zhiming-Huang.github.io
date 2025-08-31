AUTHOR = 'Zhiming Huang'
SITENAME = "Zhiming's Page"
SITEURL = ""

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
STATIC_PATHS = ['images', 'files', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

DEFAULT_PAGINATION = False

# Plugin configuration
PLUGIN_PATHS = ['plugins']
PLUGINS = ['publications_sync']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
