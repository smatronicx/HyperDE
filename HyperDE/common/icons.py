#
# This file is part of HyperDE.
# Copyright (c) 2019 by Smatronicx.
# All Rights Reserved.
#
# HyperDE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# HyperDE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with HyperDE.  If not, see <https://www.gnu.org/licenses/>.
#

# Import icons for use

class Icons():
    # Interface class for icons
    # Singleton instance
    __instance = None

    @staticmethod
    def getInstance():
        # Static access method
        if Icons.__instance is None:
            Icons()
        return Icons.__instance

    def __init__(self):
        # Initialize
        if Icons.__instance is not None:
            raise ValueError("The class ""Icons"" is defined\n\
            Use getInstance() method to access the class")

        else:
            #Virtual private constructor
            Icons.__instance = self
            self._CreateIconList()

    def _CreateIconList(self):
        # Create icon list from res path
        script_path = os.path.abspath(os.path.dirname(sys.argv[0]))
        icon_path = os.path.join(script_path, "res", "icons")
        self.icon_list = wx.ImageList(16,16)
        self.icon_idx = dict()
        # Load all icon files
        for icon_file in os.listdir(icon_path):
            icon_name = os.path.splitext(icon_file)[0]
            icon_file_full = os.path.join(icon_path, icon_file)
            icon_bmp = wx.Bitmap(icon_file_full, wx.BITMAP_TYPE_ANY)
            self.icon_idx[icon_name] = self.icon_list.Add(icon_bmp)

    def GetIconBitmap(self, name):
        # Get bitmap from icon list
        if name in self.icon_idx:
            return self.icon_list.GetBitmap(self.icon_idx[name])

        return None

    def GetIconList(self):
        # Get the list of icons
        return self.icon_list

    def GetIconIndex(self, name):
        # Get icon index from icon list
        if name in self.icon_idx:
            return self.icon_idx[name]

        return -1

    def __getitem__(self, name):
        # Get icon index
        self.GetIconIndex(name)
