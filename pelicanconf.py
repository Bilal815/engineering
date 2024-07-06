# Import required module
import os

# Author and site information
AUTHOR = 'Wasif'
SITENAME = 'F and D Engineering'
SITEURL = 'fanddeng.com'
CATEGORY = ''
SITEDESCRIPTION = 'My Blog'
DEFAULT_LOCALE = 'en_US'

# To read markdown file in 
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html',
}

# Explicitly define the Markdown reader
from pelican.readers import MarkdownReader
READERS = {'md': MarkdownReader}

# Contact information
CONTACT_INFORMATION = {
    'Phone Number': '+92 335 822-1316',
    'Email Address': 'wasif.ali@fanddeng.com',
    'Street Address': 'Plot No. 97 Area 37-B, Landhi, Karachi',
    'Map Embed URL': "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3620.4826186946034!2d67.19400428564973!3d24.847361121052195!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3eb3309a497b70d7%3A0xfaed3cfbf988702d!2s37%20b%2C%20Sector%2037%20B%20Landhi%20Town%2C%20Karachi%2C%20Karachi%20City%2C%20Sindh%2075160%2C%20Pakistan!5e0!3m2!1sen!2sus!4v1716700235376!5m2!1sen!2sus"
}

# Content settings
PATH = 'content/'

# Time and language settings
TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = 'en'

# Appearance settings
SITELOGO = ""
FAVEICON = '{}/theme/assets/images/icon.png'.format(SITEURL)
DELETE_OUTPUT_DIRECTORY = True
THEME = 'theme/'

# Feed generation settings
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Article settings
ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}.html'

# Page settings
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Index settings
INDEX_URL = '/'
INDEX_SAVE_AS = 'index.html'

# Category settings
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORY_PAGINATION_URL = 'category/{slug}/page/{number}/'
CATEGORY_PAGINATION_SAVE_AS = 'category/{slug}/page/{number}/index.html'

# Tag settings
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAG_PAGINATION_URL = 'tag/{slug}/page/{number}/'
TAG_PAGINATION_SAVE_AS = 'tag/{slug}/page/{number}/index.html'

# Author settings
AUTHOR_URL = 'author/{slug}/'
AUTHOR_URL_SAVE_AS = 'author/{slug}/index.html'

# Pages
DIRECT_TEMPLATES = ['index', 'services', 'shop', 'blog']
TEMPLATE_PAGES = {
    'services.html': 'services.html',
    #'shop.html': 'shop.html',
    'blog.html': 'blog.html',
    'contact.html': 'contact.html',
    '404.html': '404.html',
}

# Static files
STATIC_PATHS = ['extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}

# Blogroll links
LINKS = (
    ('Pelican', 'https://getpelican.com/'),
    ('Python.org', 'https://www.python.org/'),
    ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
    ('You can modify those links in your config file', '#'),
)

# Social media links
SOCIAL_MEDIA_LINKS = (
    ('Twitter', 'https://twitter.com/your_twitter_username'),
    ('Facebook-F', 'https://facebook.com/your_facebook_username'),
    ('GitHub', 'https://github.com/your_github_username'),
    ('Youtube', 'https://youtube.com/your_youtube_username'),
    ('Tiktok', ''),
    # Add more social media links here
)

# Pagination settings
DEFAULT_PAGINATION = False
'''PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)'''

# Plugins
PLUGINS_PATH = os.path.join(os.getcwd(), "pelican-plugins")
PLUGIN_PATHS = [PLUGINS_PATH]
PLUGINS = ["sitemap", "articlejson", "share_post", "preprocess"]

# Sitemap settings
SITEMAP = {
    'siteurl': SITEURL,
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'daily',
        'pages': 'daily',
        'indexes': 'daily',
    },
    'exclude': [],  # ex: ['categories', 'tags']
}

# SEO settings
OPEN_GRAPH = True
TWITTER_TAGS = True
YOUR_TWITTER_HANDLE = "pytheme"
REL_CANONICAL = True
USE_GOOGLE_FONTS = True

# KwesForms settings
KWESFORMS_ACTION = "https://kwesforms.com/api/foreign/forms/S9CLmleGJB99fnH4f3kw"

# Disqus settings
DISQUS = True

# HIGHLIGHTER = True