# -*- coding: utf-8 -*-
"""
Created on Mon Jul  10 16:19:22 2019

@author: Johan Bregeon (bregeon@in2p3.fr)
"""

import sys
from utils.tools import fit_peak
from ccobnb.spectro import read_data, plot_spectrum


if __name__ == "__main__":
    # give a file path and wavelength
    if len(sys.argv[1:]) < 1:
        print('Please give a file path to a spectrum')
        print('Try:\n \
        python scripts/plot_spectrum.py ./example_data/hg_spectrum.dat')
        sys.exit(1)
    file_path = sys.argv[1]

    # read data from file
    np_nm, np_raw, np_signal = read_data(file_path)
    # show full spectrum
    plot_spectrum(np_nm, np_signal)
