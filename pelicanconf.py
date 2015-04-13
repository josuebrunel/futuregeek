#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Josue Kouka'
SITENAME = u'FutureGeek'
SITEURL = 'http://www.josuebrunel.org'

TIMEZONE = 'Europe/Paris'
DEFAULT_DATE = u'fs'
DEFAULT_LANG = u'fr'

DISQUS_SITENAME ='fgjosue'

GOOGLE_ANALYTICS = 'UA-32441224-2'

GITHUB_URL = 'https://github.com/josuebrunel/'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          )

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/josuebrunel'),
          ('Github', 'https://github.com/josuebrunel'),)

TWITTER_USERNAME = 'josuebrunel'

DEFAULT_PAGINATION = 10

THEME = 'notmyidea'

DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives']

STATIC_PATHS = ['images',]

NEWEST_FIRST_ARCHIVES = True

ARCHIVES_SAVE_AS = 'archives.html'

MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
