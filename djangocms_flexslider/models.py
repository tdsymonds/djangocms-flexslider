# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from djangocms_text_ckeditor.fields import HTMLField
from cms.models import CMSPlugin, Page
from filer.fields.image import FilerImageField


@python_2_unicode_compatible
class Slider(CMSPlugin):
    """
    Used to model the image slider.
    """
    name = models.CharField(_('name'), max_length=100)
    slider_id = models.CharField(_('slider ID'), max_length=100, default='slider',
        help_text=_('The ID attribute used in the HTML'))
    slider_config = models.TextField(_('slider config'), blank=True, null=True,
        help_text=_('The JSON object passed to Flexslider. For more info <a target="_blank" href="https://github.com/woothemes/FlexSlider/wiki/FlexSlider-Properties">click here</a>'))
    carousel = models.BooleanField(_('carousel'), default=False,
        help_text=_('Add a thumbnail carousel to the slider'))
    carousel_id = models.CharField(_('slider ID'), max_length=100, default='carousel',
        help_text=_('The ID attribute used in the HTML'))
    carousel_config = models.TextField(_('carousel config'), blank=True, null=True,
        help_text=_('The JSON object passed to Flexslider for the carousel. For more info <a target="_blank" href="https://github.com/woothemes/FlexSlider/wiki/FlexSlider-Properties">click here</a>'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Slider')
        verbose_name_plural = _('Sliders')


@python_2_unicode_compatible
class Slide(CMSPlugin):
    """
    Used to model the slides in a slider.
    """
    image = FilerImageField()
    width = models.IntegerField(_('width'), blank=True, null=True, help_text=_('in pixels'))
    height = models.IntegerField(_('height'), blank=True, null=True, help_text=_('in pixels'))
    caption = HTMLField(_('caption'), blank=True, null=True,
        help_text=_('Optional caption that is displayed with the image'))
    link_url = models.URLField(_('link url'), max_length=500, null=True, blank=True,
        help_text=_('If a url is specified, this slide will act as a hyperlink to that url.'))
    page_url = models.ForeignKey(Page, verbose_name=_('page url'), null=True, blank=True,
        on_delete=models.SET_NULL, help_text=_('If a page is specified, this slide will act as a hyperlink to that page.'))

    def __str__(self):
        if self.caption:
            return self.caption[:50]
        return self.image.url

    class Meta:
        verbose_name = _('Slide')
        verbose_name_plural = _('Slides')

    def save(self, *args, **kwargs):
        if not self.height:
            self.height = self.image.height
        if not self.width:
            self.width = self.image.width
        super(Slide, self).save(*args, **kwargs)

    def clean(self):
        if self.link_url and self.page_url:
            raise ValidationError(_('You cannot have both a link url and page url specified'))

    def get_dimensions(self):
        return '%sx%s' % (self.width, self.height)
