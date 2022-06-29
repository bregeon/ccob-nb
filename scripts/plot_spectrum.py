# -*- coding: utf-8 -*-
"""
Created on Mon Jul  10 16:19:22 2019

@author: Johan Bregeon
"""

import sys
from utils.tools import fit_peak
from ccobnb.spectro import read_data, plot_spectrum


if __name__ == "__main__":
    # give a file path and wavelength
    if len(sys.argv[1:]) < 1:
        print('Please give a file path to a spectrum')
        print('Try:\n \
        python scripts/plot_spectrum.py ../data/data_12062020_spectro/20200612_103843_Spectrum_A1-I6.csv')
        sys.exit(1)
    file_path = sys.argv[1]

    # read data from file
    np_x, np_y = read_data(file_path)
    # show full spectrum
    plot_spectrum(np_x, np_y)
