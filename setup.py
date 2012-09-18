from setuptools import setup, find_packages
import os

version = '1.2dev'

setup(name='collective.blog.star',
      version=version,
      description="Blog suite for Plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone blog',
      author='Jarn AS',
      author_email='info@jarn.com',
      url='http://svn.plone.org/svn/collective/collective.blog.star/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.blog'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.blog.feeds>=1.3',
          'collective.blog.portlets>=1.3',
          'collective.blog.view>=1.4',
          'collective.twitterportlet',
          'collective.flowplayer',
          'qi.portlet.TagClouds',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
