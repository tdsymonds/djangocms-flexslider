# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms.models import ModelForm
from django.utils.translation import ugettext_lazy as _

from cms.forms.fields import PageSelectFormField

from .models import Slide


class SlideForm(ModelForm):
    page_url = PageSelectFormField(label=_('page'), required=False)

    class Meta:
        model = Slide
        fields = '__all__'
