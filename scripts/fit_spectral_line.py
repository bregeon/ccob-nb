# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:23:22 2019

@author: Nicolas Andres, Johan Bregeon (bregeon@in2p3.fr)
"""

import sys
from utils.tools import fit_peak
from ccobnb.spectro import read_data, plot_spectrum


if __name__ == "__main__":
    # give a file path and wavelength
    if len(sys.argv[1:]) < 2:
        print('Please give a file path and a wavelength')
        print('Try:\n \
        python scripts/fit_spectral_line.py example_data/hyperchromator_600nm.dat  600')
        sys.exit(1)
    file_path = sys.argv[1]
    wl = int(sys.argv[2])

    # read data from file
    np_nm, np_raw, np_signal = read_data(file_path)
    # show full spectrum
    plot_spectrum(np_nm, np_signal)
    # fit the line
    fit_peak(wl, np_nm, np_signal)
