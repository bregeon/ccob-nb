# -*- coding: utf-8 -*-
"""
Created on Thu June  25 12:27 2020

@authors: Johan Bregeon (bregeon@in2p3.fr)
"""

import sys
from utils.tools import fit_peak
from ccobnb.pico import read_data, plot_time_series


if __name__ == "__main__":
    # give a file path and wavelength
    if len(sys.argv[1:]) < 1:
        print('Please give a file path to a spectrum')
        print('Try:\n \
        python scripts/plot_pico.py  example_data/PicoRead_600nm_v2.csv')
        sys.exit(1)
    file_path = sys.argv[1]

    # read data from file
    time_series = read_data(file_path)
    # show full time series
    plot_time_series(time_series, file_path, save=False)
    
