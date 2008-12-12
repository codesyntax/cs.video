from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from cs.video import videoMessageFactory as _

# -*- extra stuff goes here -*-

class IVideo(Interface):
    """An object referring to externally hosted FLV files"""
