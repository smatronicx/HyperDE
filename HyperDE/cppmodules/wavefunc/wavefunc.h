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

#ifndef WAVEFUNC_H
#define WAVEFUNC_H

class WaveFunc {
  public:
    /*
    Find first y given value of x
    xvec: xaxis vector
    xlen: length of xaxis vector
    yvec: yaxis vector
    ylen: length of yaxis vector
    outvec: value of x
    yin: value of y for finding x
    start: index to start search

    return: index of xaxis or error

    */
    int FindYatX(double* xvec, long int xlen,
      double* yvec, long int ylen,
      double* outvec, long int outlen,
      double xin, long int xstart
    );

    /*
    Find first x given value of y
    xvec: xaxis vector
    xlen: length of xaxis vector
    yvec: yaxis vector
    ylen: length of yaxis vector
    outvec: value of x
    yin: value of y for finding x
    start: index to start search

    return: index of yaxis or error

    */
    int FindXatY(double* xvec, long int xlen,
      double* yvec, long int ylen,
      double* outvec, long int outlen,
      double yin, long int ystart
    );

    /*
    Find first index nearest to x
    xvec: xaxis vector
    xlen: length of xaxis vector
    xin: value of y for finding x
    start: index to start search

    return: index of xaxis or error

    */
    int FindNearestIndex(double* xvec, long int xlen,
      double xin, long int start
    );

  private:
    //Enum for errors
    enum error_code {
      err_no_error = -1,
      err_length_not_same = -2,
      err_not_found = -3,
      err_out_of_range = -4,
    };

};

#endif
