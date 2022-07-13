# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:23:22 2019

@author: Nicolas Andres, Johan Bregeon
"""

import matplotlib.pyplot as plt
import numpy as np
from lmfit.models import ExponentialModel, GaussianModel

from utils.tools import fit_peak
from ccobnb.spectro import hg_calib_lines, read_data, plot_spectrum


def fit_one_line(wl, np_x, np_y, with_plot=True, plot_components=False):
    out = fit_peak(wl, np_x, np_y, with_plot=with_plot, plot_components=plot_components)
    mean = round(out.params['g1_center'].value, 3)
    fwhm = round(out.params['g1_fwhm'].value, 3)
    return mean, fwhm


if __name__ == "__main__":
    # read spectrum data
    np_nm, np_raw, np_signal = read_data('example_data/hg_spectrum.dat')
    # plot spectrum data
    plot_spectrum(np_nm, np_signal)
    # define exceptions
    wl_except=[253.652, 296.728, 302.150, 313.155, 334.148]
    clean_lines = list()
    for wl in hg_calib_lines():
        if wl not in wl_except:
            clean_lines.append(wl)
    # fit all the lines
    mean_list = list()
    fwhm_list=list()
    for one in clean_lines:
        mean, fwhm = fit_one_line(one, np_nm, np_signal, with_plot=False)
        mean_list.append(mean)
        fwhm_list.append(fwhm)

    # print fwhms
    print()
    print('wl\tfwhm')
    for wl, mean, fwhm in zip(clean_lines, mean_list, fwhm_list):
        print('{:5}\t{:.2f}\t{:.2f}'.format(wl, mean, fwhm))

    diffs = [a-b for a,b in zip(clean_lines, mean_list)]

    # plot calibration and resolution
    plt.rcParams["figure.figsize"] = [12, 9]
    fig, ax = plt.subplots(2, 1)
    axs = ax.ravel()
    axs[0].plot(clean_lines, diffs, '+r')
    axs[0].set_xlabel(r'$\lambda$ (nm)')
    axs[0].set_ylabel('Line center expcted-data (nm)')
    axs[1].plot(clean_lines, fwhm_list, '+b')
    axs[1].set_xlabel(r'$\lambda$ (nm)')
    axs[1].set_ylabel('FWHM (nm)')
    # plt.legend()
    plt.show()
