# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings


app_settings = getattr(settings, 'DJANGOCMS_FLEXSLIDER', {})

CDN_BASE_URL = 'https://cdnjs.cloudflare.com/ajax/libs/flexslider/2.6.1/'

if 'JS_URL' not in app_settings:
    app_settings['JS_URL'] = CDN_BASE_URL + 'jquery.flexslider.min.js'
if 'CSS_URL' not in app_settings:
    app_settings['CSS_URL'] = CDN_BASE_URL + 'flexslider.min.css'
