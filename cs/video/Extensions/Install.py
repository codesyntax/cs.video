
from StringIO import StringIO

from Products.Archetypes.Extensions.utils import install_subskin
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import getFSVersionTuple

from cs.video.config import GLOBALS

def install(self):
    out = StringIO()

    tool=getToolByName(self, "portal_setup")


    install_subskin(self, out, GLOBALS, 'skins')

    if getFSVersionTuple()[:3]>=(3,0,0):
        tool.runAllImportStepsFromProfile(
            "profile-cs.video:default",
            purge_old=False)
    else:
        plone_base_profileid = "profile-CMFPlone:plone"
        tool.setImportContext(plone_base_profileid)
        tool.setImportContext("profile-cs.video:default")
        tool.runAllImportSteps(purge_old=False)
        tool.setImportContext(plone_base_profileid)

    print >> out, "cs.video successfully installed"

    return out.getvalue()
    
