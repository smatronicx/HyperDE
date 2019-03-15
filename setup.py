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

from setuptools import setup, Extension
import os
import sys

# Build c modules
c_modules = ["wavefunc"]
cext_modules = list()

script_path = os.path.abspath(os.path.dirname(sys.argv[0]))
c_modules_path = os.path.join(script_path, "HyperDE","cmodules")


for cmod in c_modules:
    mod_path = os.path.join(c_modules_path, cmod)
    os.chdir(mod_path)
    cfile = cmod
    ext_mod = Extension("_" + cmod, sources=[cmod + ".i", cfile + ".c"])
    cext_modules.append(ext_mod)

setup(
    name="cmodules",
    ext_modules=cext_modules,
    py_modules=c_modules
)
