#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://raul7gs.github.io/diana-website'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None

DELETE_OUTPUT_DIRECTORY = True

DISQUS_SITENAME = "cpacs"
GOOGLE_ANALYTICS = "UA-25164892-2"
