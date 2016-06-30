#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'GuiGeek'
AUTHOR_EMAIL = u'groche@guigeek.org'
SITENAME = u"Guigeek's Blog"
SITETITLE = AUTHOR
SITESUBTITLE = u'Ingénieur réseau'
SITEURL = '//blog.guigeek.org'
BROWSER_COLOR = '#333333'


ROBOTS = u'index, follow'
TIMEZONE = 'Europe/Paris'
THEME = 'themes/Flex'

from subprocess import check_output
VERSION_HASH = check_output(['git', 'rev-parse', '--short', 'HEAD']).strip()

USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True

# http://pygments.org/docs/lexers/#lexers-for-various-shells

DEFAULT_LANG = u'fr'
DEFAULT_CATEGORY = 'uncategorized'

SITELOGO = SITEURL+'/images/cropped-doctor-futurama.png'

# Feed generation is usually not desired when developing
TRANSLATION_FEED_ATOM = None
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Retro-compat with my Old WP setup
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

LINKS = (('CV', '//blog.guigeek.org/extra/cv.pdf'),)

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

# Social widget
# http://fontawesome.io/icons/ (just remove « fa- »
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/guillaume-roche-a544198'),
          ('github', 'https://github.com/guigeek208'),
          ('rss', '//blog.guigeek.org/feeds/all.rss.xml'),
          )

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['neighbors']

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/keybase.txt': {'path': 'keybase.txt'},
    }


COPYRIGHT_YEAR = 2016

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
