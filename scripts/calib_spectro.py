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
    fwhm = round(out.params['g1_fwhm'].value,3)
    return fwhm


if __name__ == "__main__":
    # read spectrum data
    np_x, np_y = read_data('example_data/hg_spectrum.csv')
    # plot spectrum data
    plot_spectrum(np_x, np_y)
    # define exceptions
    wl_except=[302, 435, 750, 800, 842, 912]
    clean_lines = list()
    for wl in hg_calib_lines():
        if wl not in wl_except:
            clean_lines.append(wl)
    # fit all the lines
    fwhm_list=list()
    for one in clean_lines:
        fwhm = fit_one_line(one, np_x, np_y, with_plot=True)
        fwhm_list.append(fwhm)

    # print fwhms
    print()
    print('wl\tfwhm')
    for wl, fwhm in zip(clean_lines, fwhm_list):
        print('{:5}\t{:.2f}'.format(wl, fwhm))

    # plot resolution
    plt.figure()
    plt.plot(clean_lines, fwhm_list, '+b')
    plt.xlabel(r'$\lambda$ (nm)')
    plt.ylabel('FWHM (nm)')
    # plt.legend()
    plt.show()
