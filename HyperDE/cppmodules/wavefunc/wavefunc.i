/*
This file is part of HyperDE.
Copyright (c) 2019 by Smatronicx.
All Rights Reserved.

HyperDE is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

HyperDE is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with HyperDE.  If not, see <https://www.gnu.org/licenses/>.

*/

%module wavefunc
%{
  #define SWIG_FILE_WITH_INIT
  #include "wavefunc.h"
%}

/*  include the numpy typemaps */
%include "../include/numpy.i"
%fragment("NumPy_Fragments");
/*  need this for correct module initialization */
%init %{
    import_array();
%}

%apply (double* IN_ARRAY1, int DIM1) {(double* xvec, long int xlen)};
%apply (double* IN_ARRAY1, int DIM1) {(double* yvec, long int ylen)};
%apply (double* IN_ARRAY1, int DIM1) {(double* outvec, long int outlen)};

/* Header Files */
%include "wavefunc.h"
