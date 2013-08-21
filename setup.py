#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='django-inline-ordering',
    version='0.1.4',
    author='Ralf Kostulski',
    author_email='webdeveloper@ralfkostulski.de',
    url='https://github.com/ralfzen/django-inline-ordering/',
    description='Django app to ease ordering of related data - ' \
                'enable Drag&Drop ordering in admin with just a few LOC',
    #packages = ['inline_ordering',],
    packages=find_packages(),
    provides=['inline_ordering',],
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        #'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)