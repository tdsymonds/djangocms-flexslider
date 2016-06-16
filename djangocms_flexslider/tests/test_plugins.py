# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from cms.api import add_plugin
from cms.models import Placeholder

from ..cms_plugins import SliderPlugin


class SliderPluginTests(TestCase):
    def test_plugin_context(self):
        placeholder = Placeholder.objects.create(slot='test')
        model_instance = add_plugin(
            placeholder,
            SliderPlugin,
            'en',
        )
        plugin_instance = model_instance.get_plugin_class_instance()
        context = plugin_instance.render({}, model_instance, None)
        self.assertIn('instance', context)

    def test_plugin_html(self):
        placeholder = Placeholder.objects.create(slot='test')
        model_instance = add_plugin(
            placeholder,
            SliderPlugin,
            'en',
        )
        html = model_instance.render_plugin({})
        self.assertTrue(html.find('class="flexslider">') > -1)
