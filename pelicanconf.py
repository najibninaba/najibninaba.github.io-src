#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Najib Ninaba'
SITENAME = 'Najib Ninaba: Writings & Musings'
SITEURL = ''

PATH = 'content'
PLUGIN_PATHS = ['./plugins']
PLUGINS = []
THEME = 'themes/svbhack'
USER_LOGO_URL = SITEURL + '/images/logo.jpg'
TAGLINE = 'Husband & Dad | Big Data, Backends & Bits | Certified Scrum Master | Silat, Kuntau, Kali'

TIMEZONE = 'Asia/Singapore'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('About', '#'),
         ('Now', '#'),)

# Social widget
SOCIAL = (('Twitter', '#'),
          ('LinkedIn', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
