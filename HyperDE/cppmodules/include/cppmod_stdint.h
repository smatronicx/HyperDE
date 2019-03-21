//
// This file is part of HyperDE.
// Copyright (c) 2019 by Smatronicx.
// All Rights Reserved.
//
// HyperDE is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// HyperDE is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with HyperDE.  If not, see <https://www.gnu.org/licenses/>.
//

// Wrapper for stdint for VisualC

#ifndef CMOD_STDINT_H
#define CMOD_STDINT_H

#ifdef _MSC_VER

typedef __int32 int32_t;
typedef unsigned __int32 uint32_t;
typedef __int64 int64_t;
typedef unsigned __int64 uint64_t;

#else
#include <stdint.h>
#endif

#endif
