#!/bin/env python
"""
Created on Tue 09 Jul 2019 02:55:09 PM CEST

Client to the diode module
give it wavelenght, it will return the conversion factor (nA/nW)

@author: Johan Bregeon (bregeon@in2p3.fr)
"""

import sys
from ccobnb import diode

if __name__ == "__main__":
    # get data from text file
    wl_dict = diode.read_data('calib/diode_calibration_data.dat')
    # Check that there is a wavelenght
    if len(sys.argv[1:]) < 1:
        print('Please give a wavelength')
        sys.exit(1)

    wl_list = sys.argv[1:]
    # check if there is an input current
    if len(wl_list) == 2:
        wl = float(wl_list[0])
        current = float(wl_list[1])
        val = diode.get_value(wl, wl_dict)
        power = current/val
        print('wavelenght\tConversion\tCurrent\t\tPower')
        print('{:<8}\t{:<10}\t{:<10}\t{:<10}'.format(wl, val, current, power))
    else:
        wl = float(wl_list[0])
        val = diode.get_value(wl, wl_dict)
        print('wavelenght\tConversion')
        print('{:<8}\t{:<10}'.format(wl, val))
