# -*- coding: utf-8 -*-
"""
Created on Thu July 2nd 15:21 2020

@authors: Johan Bregeon (bregeon@in2p3.fr)
"""

import os
import sys
from glob import glob
from utils.tools import fit_peak
from ccobnb import pico
from ccobnb import diode
from matplotlib import pyplot  as plt
import numpy as np


if __name__ == "__main__":
    """ do all the stuff
    """
    # Data taking of July 1st 2020
    # 17 mesurements from 300 nm to 1100 nm by step of 50 nm
    wl_series = range(300,1150,50)
    pico_files = """../data/data_01072020/PicoRead_20200701-110942.csv
    ../data/data_01072020/PicoRead_20200701-112510.csv
    ../data/data_01072020/PicoRead_20200701-114036.csv
    ../data/data_01072020/PicoRead_20200701-115602.csv
    ../data/data_01072020/PicoRead_20200701-121130.csv
    ../data/data_01072020/PicoRead_20200701-122657.csv
    ../data/data_01072020/PicoRead_20200701-124225.csv
    ../data/data_01072020/PicoRead_20200701-125752.csv
    ../data/data_01072020/PicoRead_20200701-131320.csv
    ../data/data_01072020/PicoRead_20200701-132858.csv
    ../data/data_01072020/PicoRead_20200701-134425.csv
    ../data/data_01072020/PicoRead_20200701-135951.csv
    ../data/data_01072020/PicoRead_20200701-141517.csv
    ../data/data_01072020/PicoRead_20200701-143044.csv
    ../data/data_01072020/PicoRead_20200701-144610.csv
    ../data/data_01072020/PicoRead_20200701-150138.csv
    ../data/data_01072020/PicoRead_20200701-151706.csv""".split()

    wl_dict = diode.read_data('calib/diode_calibration_data.dat')

    pow_ave_list = list()
    pow_rms_list = list()

    # make stability plots for each wl

    for wl, file_path in zip(wl_series, pico_files):
        print(wl, file_path)
        # read data from file
        times, currents = pico.read_data(file_path)
        # convert to light output
        conv_factor = diode.get_value(wl, wl_dict)
        print('\t Conversion factor %.2f'%conv_factor)
        powers = -currents/conv_factor
        # get mean
        pow_ave_list.append(np.mean(powers))
        pow_rms_list.append(np.std(powers))
        # show full time series
        time_series = (times, powers)
        fig = pico.make_fig_time_series(time_series, wl=wl, file_path=file_path, save=True)
        plt.show()

    # make summary power plot
    fig = plt.figure(1, figsize=(15, 9))
    plt.rcParams.update({'font.size': 22})
    plt.title('Power against wavelenght @ 12000 mm')
    plt.xlabel('Wavelenght (nm)')
    plt.ylabel('Power (nW)')
    # Reference data
    wl_refs = [350, 700, 1000]
    pow_refs = [23, 4, 8]
    # Acquired data
    plt.errorbar(wl_series, pow_ave_list, xerr=1.5, yerr=pow_rms_list,
                 ls='none', marker='+', label='data', markersize=16)
    plt.errorbar(wl_refs, pow_refs, yerr=1, lolims=True, ls='none',
                 marker='_', color='red', label='reference', markersize=16)
    plt.legend()
    plt.tight_layout()
    plt.show()
