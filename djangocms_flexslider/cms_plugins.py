# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .forms import SlideForm
from .models import Slide, Slider
from .settings import app_settings


class SliderPlugin(CMSPluginBase):
    name = _('Slider')
    module = _('DjangoCMS FlexSlider')
    model = Slider
    render_template = 'djangocms_flexslider/_slider.html'
    cache = False
    allow_children = True
    child_classes = ['SlidePlugin', ]

    def render(self, context, instance, placeholder):
        context = super(SliderPlugin, self).render(context, instance, placeholder)
        context['app_settings'] = app_settings
        return context

plugin_pool.register_plugin(SliderPlugin)


class SlidePlugin(CMSPluginBase):
    name = _('Slide')
    module = _('DjangoCMS FlexSlider')
    model = Slide
    form = SlideForm
    render_template = 'djangocms_flexslider/_slide.html'
    cache = False
    require_parent = True

plugin_pool.register_plugin(SlidePlugin)
