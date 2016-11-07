# coding: utf-8

from setuptools import setup, find_packages

setup(name='sbsched',
      version='0.1',
      description='Scrapes Silverbird Cinema website for movie schedules',
      url='https://github.com/eyedol/sbsched',
      author='Henry Addo',
      author_email='henry@addhen.org',
      license='Apache 2.0',
      py_modules=['sbsched'],
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'beautifulsoup4',
      ],
      zip_safe=False)