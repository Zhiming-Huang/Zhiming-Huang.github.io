from datetime import date

AUTHOR = 'Zhiming Huang'
SITENAME = "Zhiming's Page"
SITEURL = ""
COPYRIGHT_YEAR = date.today().year
DEFAULT_PROFILE_IMAGE = "profile.jpeg"
DEFAULT_OCCUPATION_NAME = "Academic Researcher"

# Academic Profile Settings
ACADEMIC_TITLE = "Academic Researcher"  # Fallback when content/index.md has no Job_title
ACADEMIC_POSITION = ""
ACADEMIC_INSTITUTION = ""
ACADEMIC_DEPARTMENT = "Computer Science"
RESEARCH_INTERESTS = []

# SEO Settings
SITE_DESCRIPTION = SITENAME
SITE_KEYWORDS = AUTHOR

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

# Static menu items. Page links are controlled by each page's Markdown metadata.
MENUITEMS = (
    ('Home', '/'),
)

# Optional fallback social links. The footer uses content/index.md metadata first.
SOCIAL = ()

# Page settings
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'



# Article settings (for news/blog posts)
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

# Static paths
STATIC_PATHS = ['images', 'files', 'extra/CNAME', 'extra/robots.txt']
IGNORE_FILES = ['.#*', '.DS_Store']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
}
TEMPLATE_PAGES = {'templates/sitemap.xml': 'sitemap.xml'}

DEFAULT_PAGINATION = False

# Plugin configuration
PLUGIN_PATHS = ['plugins']
PLUGINS = ['publications_sync', 'page_visibility']

# Template context variables
EXTRA_CONTEXT = {
    'ACADEMIC_TITLE': ACADEMIC_TITLE,
    'ACADEMIC_POSITION': ACADEMIC_POSITION,
    'ACADEMIC_INSTITUTION': ACADEMIC_INSTITUTION,
    'ACADEMIC_DEPARTMENT': ACADEMIC_DEPARTMENT,
    'RESEARCH_INTERESTS': RESEARCH_INTERESTS,
    'COPYRIGHT_YEAR': COPYRIGHT_YEAR,
    'DEFAULT_PROFILE_IMAGE': DEFAULT_PROFILE_IMAGE,
    'DEFAULT_OCCUPATION_NAME': DEFAULT_OCCUPATION_NAME,
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
