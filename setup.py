#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages


setup(name='jakatonlib',
      version='0.0.1',
      author='Ivan Vladimir Meza Ruiz',
      author_email='ivanvladimir@gmail.com',
      url='https://github.com/jakaton/jakatonlib',
      download_url='https://github.com/jakaton/jakatonlib',
      description='Minor wrappers for NLP tools used in Jakatón 2015',
      long_description='It offers some wrappers for NLP tools used during the Jakatón 2015',

      packages = find_packages(),
      include_package_data = True,
      package_data = {
        '': ['*.txt', '*.rst'],
        'my_program': ['data/*.html', 'data/*.css'],
      },
      exclude_package_data = { '': ['README.txt'] },
      
      keywords='python jakaton',
      license='GPL',
      classifiers=['Development Status :: 5 - Production',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2',
                   'License :: OSI Approved :: GNU General Public License v2',
                   'Topic :: NLP',
                  ],
                  
      install_requires = ['setuptools','urllib','urllib2'],
     )
