import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='djangocms-flexslider',
    version='1.0.0',
    license='MIT License',
    description='A Django CMS image slider plugin that uses FlexSlider.',
    long_description=README,
    url='https://github.com/tdsymonds/djangocms-flexslider',
    author='Tom Symonds',
    author_email='tdsymonds@hotmail.com',
    keywords='djangocms-flexslider, flexslider, django, image-slider',
    packages=[
        'djangocms_flexslider',
    ],
    include_package_data=True,
    install_requires=[
        'django-cms>=3.2',
        'django-filer',
        'easy-thumbnails',
        'djangocms-text-ckeditor',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
