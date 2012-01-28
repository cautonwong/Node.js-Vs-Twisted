from setuptools import setup, find_packages
import sys, os

version = '0.0.1a'

setup(name='yukeyukeyuke',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Josh Johnson',
      author_email='lionface.lemonface@gmail.com',
      url='http://lionfacelemonface.wordpress.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      # package_data={
      #       'twisted': ['plugins/yukeyukeyuke_plugin.py'],
      #   },
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'Twisted',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
