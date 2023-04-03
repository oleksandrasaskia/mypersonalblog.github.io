AUTHOR = 'Oleksandra Sopova'
SITENAME = 'Oleksandra Sopova'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('LinkedIn', 'https://www.linkedin.com/in/oleksandrasopova/'),
 )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'medius'

DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('Welcome', '/'),
    ('Contact', '/pages/contact.html'),
    ('About Me',   '/pages/about-me.html'),
    )