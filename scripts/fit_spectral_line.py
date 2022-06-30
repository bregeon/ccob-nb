# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:23:22 2019

@author: andres, bregeon
"""

import sys
from utils.tools import fit_peak
from ccobnb.spectro import read_data, plot_spectrum


if __name__ == "__main__":
    # give a file path and wavelength
    if len(sys.argv[1:]) < 2:
        print('Please give a file path and a wavelength')
        print('Try:\n \
        python scripts/fit_spectral_line.py ../data/data_12062020_spectro/20200612_103843_Spectrum_A1-I6.csv 304')
        sys.exit(1)
    file_path = sys.argv[1]
    wl = int(sys.argv[2])

    # read data from file
    np_x, np_y = read_data(file_path)
    # show full spectrum
    # plot_spectrum(np_x, np_y)
    # fit the line
    fit_peak(wl, np_x, np_y)
