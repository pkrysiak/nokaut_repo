# -*- coding:UTF-8 -*-

from setuptools import setup

setup(name = 'Nokaut',
      version = '1.0',
      author = 'Paweł Krysiak',
      author_email = 'pawel.krysiak@stxnext.pl',
      packages = ['nokaut','tests'],
      install_requires = ['lxml','mock','argparse'],
      test_suite='tests',
      entry_points = {'console_scripts': ['main = lib.scripts:main']}
)