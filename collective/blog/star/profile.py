from zope.interface import implements

from Products.CMFPlone.interfaces import INonInstallable
from Products.CMFQuickInstallerTool.interfaces import INonInstallable as INonQ


class HiddenProfiles(object):
    implements(INonInstallable)

    def getNonInstallableProfiles(self):
        return [
            u'collective.blog.portlets:default',
            u'collective.blog.view:default',
            u'collective.twitterportlet:default',
            u'collective.flowplayer:default',
            u'qi.portlet.TagClouds:default',
            u'Products.fatsyndication:default',
            ]

class HiddenProducts(object):
    implements(INonQ)

    def getNonInstallableProducts(self):
        return [
            u'collective.blog.portlets',
            u'collective.blog.view',
            u'collective.twitterportlet',
            u'collective.flowplayer',
            u'fatsyndication', u'Products.fatsyndication', # Yes, both are needed.
            u'qi.portlet.TagClouds',
            u'plone.app.jquerytools',
            ]
