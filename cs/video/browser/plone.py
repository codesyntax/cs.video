from zope.interface import implements, Interface
from Products.Five.browser import BrowserView

from cs.video.config import IS_PLONE2, IS_PLONE3


class IPloneVersionChecker(Interface):
    def isPlone2():
        """ return True if we are in Plone 2.x """

    def isPlone3():
        """ return True if we are in Plone 3.x """


class PloneVersionChecker(BrowserView):
    implements(IPloneVersionChecker)

    def isPlone2(self):
        return IS_PLONE2

    def isPlone3(self):
        return IS_PLONE3
    
