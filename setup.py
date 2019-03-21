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
import numpy as np

# Build c modules
cpp_modules = ["wavefunc"]
cpp_ext_modules = list()

script_path = os.path.abspath(os.path.dirname(sys.argv[0]))
cpp_modules_path = os.path.join(script_path, "HyperDE","cppmodules")
include_path = os.path.join(cpp_modules_path, "include")


for cmod in cpp_modules:
    mod_path = os.path.join(cpp_modules_path, cmod)

    src_files = list()
    src_files.append(os.path.join(mod_path, cmod) + ".i")

    for file in os.listdir(mod_path):
        if file.endswith(".cpp") and "_wrap" not in file:
            src_files.append(os.path.join(mod_path, file))

    ext_mod = Extension("_" + cmod, sources=src_files,
        include_dirs=[include_path, np.get_include()],
        swig_opts=["-c++"])
    cpp_ext_modules.append(ext_mod)

# Set arguments
setup_path = sys.argv[0]
setup_cmd = None
if len(sys.argv) > 1:
    # Read setup command
    setup_cmd = sys.argv[1]

lib_path = os.path.join(script_path, "lib")
if setup_cmd == 'clean':
    # Clean build
    sys.argv = [setup_path, setup_cmd, '--all', '--build-lib', lib_path]
else:
    # Build
    sys.argv = [setup_path, 'build_ext', '--build-lib', lib_path]


setup(
    name="cppmodules",
    ext_modules=cpp_ext_modules,
    py_modules=cpp_modules
)
