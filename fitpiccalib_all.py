# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:23:22 2019

@author: andres
"""

import matplotlib.pyplot as plt
import numpy as np
from lmfit.models import ExponentialModel, GaussianModel

from data.Hg2_calibration_lamp import calib_lines
from utils.tools import fit_peak
from spectro.spectro import read_data, plot_spectrum


def fit_one_line(wl, np_x, np_y, with_plot=True, plot_components=False):
    out = fit_peak(wl, np_x, np_y, with_plot=with_plot, plot_components=plot_components)
    fwhm = round(out.params['g1_fwhm'].value,3)
    return fwhm


if __name__ == "__main__":
    # read spectrum data
    np_x, np_y = read_data('data/spectre_lampe_calib_100ms.txt')
    # plot spectrum data
    # plot_spectrum(np_x, np_y)
    # fit all the lines
    fwhm_list=list()
    for one in calib_lines:
        fwhm = fit_one_line(one, np_x, np_y, with_plot=False)
        fwhm_list.append(fwhm)
    # plot resolution
    plt.figure()
    plt.plot(calib_lines, fwhm_list, '+b')
    plt.xlabel(r'$\lambda$ (nm)')
    plt.ylabel('FWHM (nm)')
    # plt.legend()
    plt.show()
