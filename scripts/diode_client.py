#!/bin/env python
"""
Created on Tue 09 Jul 2019 02:55:09 PM CEST

Client to the diode module
give it wavelenght, it will return the conversion factor (nA/nW)

@author: Johan Bregeon
"""

import sys
from diode import diode

if __name__ == "__main__":
    # get data from text file
    wl_dict = diode.read_data('data/diode_response.dat')
    # Check that there is a wavelenght
    if len(sys.argv[1:]) < 1:
        print('Please give a wavelength')
        sys.exit(1)

    wl_list = sys.argv[1:]
    print('wavelenght\tConversion')
    for one in wl_list:
        wl = float(one)
        val = diode.get_value(wl, wl_dict)
        print('{:<8}\t{:<10}'.format(wl, val))
