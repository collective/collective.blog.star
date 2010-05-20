from zope.interface import implements

from Products.CMFPlone.interfaces import INonInstallable
from Products.CMFQuickInstallerTool.interfaces import INonInstallable as INonQ


class HiddenProfiles(object):
    implements(INonInstallable)

    def getNonInstallableProfiles(self):
        return [
            u'collective.blog.view:default',
            u'profile-collective.blog.view:default',
            u'collective.twitterportlet:default',
            u'collective.flowplayer:default',
            u'qi.portlet.TagClouds:default',
            u'Products.fatsyndication:default',
            ]

class HiddenProducts(object):
    implements(INonQ)

    def getNonInstallableProducts(self):
        return [
            'collective.blog.view:default',
            'collective.twitterportlet',
            'collective.flowplayer',
            'qi.portlet.TagClouds',
            'Products.fatsyndication',
            ]
