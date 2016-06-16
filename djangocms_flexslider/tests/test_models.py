# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.files import File

from cms.test_utils.testcases import CMSTestCase
from filer.models import Image as FilerImage

from ..models import Slider, Slide


class SliderModelTest(CMSTestCase):
    def test_creating_new_slider(self):
        s = Slider.objects.create(name='test')

        all_sliders = Slider.objects.all()

        self.assertEqual(all_sliders.count(), 1)
        self.assertEqual(all_sliders[0], s)
        self.assertEqual(s.__str__(), s.name)


class SlideModelTest(CMSTestCase):
    def setUp(self):
        f = FilerImage.objects.create(original_filename='test',
            file=File(open('djangocms_flexslider/tests/media/avatar.png')))
        self.slide = Slide.objects.create(image=f)

    def test_creating_new_slide(self):
        s = self.slide

        all_slides = Slide.objects.all()

        self.assertEqual(all_slides.count(), 1)
        self.assertEqual(all_slides[0], s)
        self.assertEqual(s.__str__(), s.image.url)

        s.caption = 'test caption'
        self.assertEqual(s.__str__(), s.caption)

    def test_dimensions(self):
        s = self.slide
        dimensions = '%sx%s' % (s.width, s.height)
        self.assertEqual(s.get_dimensions(), dimensions)
