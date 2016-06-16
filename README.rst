.. image:: https://travis-ci.org/tdsymonds/djangocms-flexslider.svg?branch=master
    :target: https://travis-ci.org/tdsymonds/djangocms-flexslider
.. image:: https://coveralls.io/repos/github/tdsymonds/djangocms-flexslider/badge.svg?branch=master&t=1 
    :target: https://coveralls.io/github/tdsymonds/djangocms-flexslider?branch=master
.. image:: https://img.shields.io/badge/pypi-v1.0.0-blue.svg
    :target: https://github.com/tdsymonds/djangocms-flexslider
.. image:: https://img.shields.io/badge/license-MIT%20License-red.svg
    :target: https://github.com/tdsymonds/djangocms-flexslider
    
djangocms-flexslider
=====================
This is a simple `django-cms`_ plugin that implements the JavaScript `FlexSlider`_ library. 

Dependencies
------------
- django>=1.8
- django-cms>=3.2

Installation
------------
To install::

    pip install djangocms-flexslider

Then add djangocms-flexslider to your installed apps::

    INSTALLED_APPS = [
        ...
        'djangocms_flexslider',
        ...
    ]

If you're not already using `django-filer`_, `easy-thumbnails`_ and `djangocms-text-ckeditor`_ then these too will need to be added to your installed apps::

    INSTALLED_APPS = [
        ...
        'djangocms_text_ckeditor',
        'easy_thumbnails',
        'filer',
        ...
    ]


And run the migrations::

    ./manage.py migrate

The package assume that jQuery has been added to the site already. So if you're not using already, please add to you templates/base.html:

.. code:: html

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>


Configuration
-------------
The FlexSlider JS and CSS are by default loaded from the below CDN. If you wish to override this, this can be done in your settings.py file by adding the below with your updated URLs. This is optional. 

.. code:: python

    DJANGOCMS_FLEXSLIDER = {
        'JS_URL': 'https://cdnjs.cloudflare.com/ajax/libs/flexslider/2.6.1/jquery.flexslider.min.js',
        'CSS_URL': 'https://cdnjs.cloudflare.com/ajax/libs/flexslider/2.6.1/flexslider.min.css'
    }

Usage
------
The slider plugin is added to page, where the configuration for the slider is set. The settings allow you to add a carousel thumbnail slider if you wish, you are also provided the ability to pass the JSON config for both the carousel and the slider.

There are many `FlexSlider examples`_ on their site, or you can view the full `FlexSlider properties`_. The configuration JSON object is optional, so you have no obligation to provide this. A simple example of the config with a carousel is provided below.

Once the slider has been setup, slides are added by adding child slide plugins to the slider. Each slide has to have an image, (I've used `django-filer`_ for the images), and can optionally have an explicit height and/or width, a caption, url link or page link as well.


Example JSON Config
-------------------
Slider:

.. code:: javascript
  
  {
    animation: "slide",
    smoothHeight: true,
    controlNav: false,
    animationLoop: false,
    slideshow: false,
    sync: "#carousel"
  }

Carousel:

.. code:: javascript

  {
    animation: "slide",
    controlNav: false,
    animationLoop: false,
    slideshow: false,
    itemWidth: 210,
    itemMargin: 5,
    asNavFor: '#slider'
  }



.. _django-cms: https://github.com/divio/django-cms
.. _FlexSlider: http://www.woothemes.com/flexslider/
.. _FlexSlider examples: http://flexslider.woothemes.com/index.html
.. _FlexSlider properties: https://github.com/woothemes/FlexSlider/wiki/FlexSlider-Properties
.. _django-filer: https://github.com/divio/django-filer
.. _easy-thumbnails: https://github.com/SmileyChris/easy-thumbnails
.. _djangocms-text-ckeditor: https://github.com/divio/djangocms-text-ckeditor
