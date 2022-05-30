# -*- coding: utf-8 -*-
"""
Created on Thu July 2nd 15:21 2020

@authors: Johan Bregeon (bregeon@in2p3.fr)
"""

import os
import sys
from glob import glob
from utils.tools import fit_peak
from pico import pico
from diode import diode
from matplotlib import pyplot  as plt
import numpy as np


def make_light_fig_time_series(time_series, wl, file_path, save=False):
    ''' Plot a diode response converted to light output
    '''
    from diode import diode
    mean_current = np.mean(time_series[1])
    min_time = min(time_series[0])
    max_time = max(time_series[0])
    label='Photodiode time series'
    if file_path is not None:
        label = 'Picoamperemeter - %s'%file_path.split('/')[-1]
    fig = plt.figure(1, figsize=(12, 6))
    plt.plot(time_series[0], time_series[1],'+b', label=label)
    if wl is not None:
        plt.title('Power @ %snm'%wl)
    plt.xlabel('Date - Time')
    plt.ylabel('Power (nW)')
    plt.ylim(ymin=mean_current*0.98, ymax=mean_current*1.02)
    plt.hlines(mean_current*0.99, min_time, max_time, colors='r')
    plt.hlines(mean_current*1.01, min_time, max_time, colors='r')
    plt.text(max_time-30, mean_current*0.987, '-1%')
    plt.text(max_time-30, mean_current*1.013, '+1%')
    plt.legend()
    plt.grid(linestyle='--', linewidth=0.5)
    if save:
        plt.savefig(file_path[:-4]+'.png')
    return fig

if __name__ == "__main__":
    """ do all the stuff
    """
    data_path = './data_01072020'
    wl_series = range(300,1150,50)

    wl_dict = diode.read_data('diode/diode_calibration_data.dat')

    pow_ave_list = list()
    pow_rms_list = list()

    # make stability plots for each wl
    pico_files = glob(os.path.join(data_path,'PicoRead_20200701*.csv'))
    pico_files.sort()
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
        fig = make_light_fig_time_series(time_series, wl=wl, file_path=file_path, save=True)
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
