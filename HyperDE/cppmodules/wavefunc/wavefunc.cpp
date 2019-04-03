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

#include <math.h>
#include <stdio.h>
#include "wavefunc.h"

//Find first y given value of x with interpolation
int WaveFunc::FindYatX(double* xvec, long int xlen,
  double* yvec, long int ylen,
  double* outvec, long int outlen,
  double xin, long int start
) {
  // Check if lengths are same
  if(xlen != ylen) {
    return err_length_not_same;
  }

  //Check for index range
  if (start > xlen-1) {
    return err_out_of_range;
  }

  // Find y for x
  int rtn = err_not_found;
  double y;
  long int i;
  for(i = start; i<xlen-1; i++) {
    double x0 = xvec[i];
    double x1 = xvec[i+1];
    // Check if xin is between x0 and x1
    if(xin < x1 && xin >= x0) {
      double y0 = yvec[i];
      double y1 = yvec[i+1];
      // Interpolate to find y
      double f = (xin-x0)/(x1-x0);
      y = (1-f)*y0 + f*y1;
      rtn = i;
      break;
    }
  }
  //Check for last index
  if (rtn == err_not_found) {
    double x0 = xvec[i];
    if(xin == x0) {
      y = yvec[i];
      rtn = i;
    }
  }

  *outvec = y;
  return rtn;
}

//Find first x given value of y with interpolation
int WaveFunc::FindXatY(double* xvec, long int xlen,
  double* yvec, long int ylen,
  double* outvec, long int outlen,
  double yin, long int start
) {
  return FindYatX(yvec, ylen, xvec, xlen, outvec, outlen, yin, start);
}

//Find first index nearest to x
int WaveFunc::FindNearestIndex(double* xvec, long int xlen,
  double xin, long int start
) {
  //Check for index range
  if (start > xlen-1) {
    return err_out_of_range;
  }

  // Find nearest index
  int rtn = err_not_found;
  long int i;
  for(i = start; i<xlen-1; i++) {
    double x0 = xvec[i];
    double x1 = xvec[i+1];
    // Check if xin is between x0 and x1
    if(xin < x1 && xin >= x0) {
      rtn = i;
      break;
    }
  }

  //Check for last index
  if (rtn == err_not_found) {
    double x0 = xvec[i];
    if(xin == x0) {
      rtn = i;
    }
  }

  return rtn;
}

// Hit test of x,y with line within given redius
int WaveFunc::HitTest(double* xvec, long int xlen,
  double* yvec, long int ylen,
  double xin, double yin, double rin
) {
  // Check if lengths are same
  if(xlen != ylen) {
    return err_length_not_same;
  }

  // Find distance of xin,yin from lines
  double rsqr = rin*rin;
  long int i;
  for(i = 0; i<xlen-1; i++) {
    double x0 = xvec[i];
    double x1 = xvec[i+1];
    double y0 = yvec[i];
    double y1 = yvec[i+1];

    // length of segment
    double seglen = pow(x1 - x0, 2) + pow(y1 - y0, 2);
    double x, y, f;
    if (seglen == 0) {
      f = 0;
    } else {
      // Take dot product
      f = (x1 - x0)*(xin - x0) + (y1 - y0)*(yin - y0);
      // Take projection
      f = f / seglen;
      if (f < 0) {
        f = 0;
      }
      if (f > 1) {
        f = 1;
      }
    }

    x = f*x1 + (1 - f)*x0;
    y = f*y1 + (1 - f)*y0;

    // Get distance from point
    double pointdist = pow(x - xin, 2) + pow(y - yin, 2);
    // Check for hit
    if(pointdist <= rsqr) {
      return 1;
    }
  }

  return 0;
}
