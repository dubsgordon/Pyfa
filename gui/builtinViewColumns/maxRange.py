#===============================================================================
# Copyright (C) 2010 Diego Duclos
#
# This file is part of pyfa.
#
# pyfa is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyfa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyfa.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

from gui import builtinViewColumns
from gui.viewColumn import ViewColumn
from gui import bitmapLoader
import controller
from util import shorten

class MaxRange(ViewColumn):
    name = "Max range"
    def __init__(self, fittingView, params = None):
        if params == None:
            params = {"showIcon": True,
                      "displayName": False}
        ViewColumn.__init__(self, fittingView)
        cAttribute = controller.Attribute.getInstance()
        info = cAttribute.getAttributeInfo("maxRange")
        self.info = info
        if params["showIcon"]:
            iconFile = info.icon.iconFile if info.icon else None
            if iconFile:
                bitmap = bitmapLoader.getBitmap(iconFile, "pack")
                if bitmap:
                    self.imageId = fittingView.imageList.Add(bitmap)
                else:
                    self.imageId = -1
            else:
                self.imageId = -1
        else:
            self.imageId = -1

        if params["displayName"] or self.imageId == -1:
            self.columnText = info.displayName if info.displayName != "" else info.name

    def getText(self, stuff):
        maxRange = stuff.maxRange if hasattr(stuff, "maxRange") else stuff.getModifiedItemAttr("maxRange")
        falloff = stuff.getModifiedItemAttr("falloff")
        if falloff is None:
            falloff = ""
        else:
            falloff = "+%sm" % shorten(falloff, 3, 0, 3)

        if maxRange:
            return "%s" % shorten(maxRange, 3, 0, 3, unit=falloff == "") + falloff
        else:
            return "" + falloff

    def getImageId(self, mod):
        return -1

    def getParameters(self):
        return (("displayName", bool, False),
                ("showIcon", bool, True))

builtinViewColumns.registerColumn(MaxRange)
