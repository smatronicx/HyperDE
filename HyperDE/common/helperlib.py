#
# This file is part of HyperDE.
# Copyright (c) 2018 by Smatronicx.
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

import sys
import math

# This class implements the utility functions

def export(fn):
    # Function to add function in __all__
    # Use 'from helperlib import export' to get function
    # Use @export above function to add it to __all__
    # This will put the function in top namespace

    mod = sys.modules[fn.__module__]
    if hasattr(mod, '__all__'):
        mod.__all__.append(fn.__name__)
    else:
        mod.__all__ = [fn.__name__]
    return fn

def frexp10(x):
    # Return mantissa and exponent (base 10)
    if x == 0:
        return 0, 0

    exp = math.floor(math.log10(abs(x)))
    return x/10**exp, exp

def engg_unit(x, precision=3, suffix=True):
    # Convert floating point to engineering notation
    # Component suffixes
    _suffix = ["f", "p", "n", "u", "m", "", "k", "Meg", "G", "T"]
    # Offset to unit multiplier (no suffix)
    _no_suffix_offset = _suffix.index("")

    sign = False
    if x < 0.0:
        sign = True
        x = -x
    if x is math.isinf(x):
        return x
    if x == 0:
        return "0.0"
    # Normalize the number and round to get significant digits
    mant, exp = frexp10(x)
    # Get integer exponent to group by factors of 1000
    p = int(math.floor(math.log10(x)))
    p3 = p // 3
    # Get root value string
    value = x / math.pow(10.0, 3*p3)
    value = round(value,precision)
    # Set sign
    if sign is True:
        value = -value

    if suffix:
        # Append units suffix
        p3i = p3 + _no_suffix_offset
        if p3i < 0:
            value = value*math.pow(10.0, 3*p3i)
            p3i = 0
        if p3i >= len(_suffix):
            value = value*math.pow(10.0, 3*(p3i - len(_suffix)+1))
            vmant, vexp = frexp10(value)
            value = str(vmant)+"e+"+str(int(vexp))
            p3i = len(_suffix) - 1
        s = _suffix[p3i]
        return "{}{}".format(value, s)
    else:
        # No suffix, return floating point string
        if p3 != 0:
            #return "{}e{:precision}".format(value, 3*p3)
            return "{}e{}".format(value, 3*p3)
        else:
            return "{}".format(value)
