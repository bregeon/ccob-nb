#/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue 09 Jul 2019 04:43:23 PM CEST

@author: bregeon
"""
import matplotlib.pyplot as plt
import numpy as np


def hg_calib_lines(file_path='./calib/Hg_Ar_spectral_lines.dat'):
    """
    Get Hg calib lines from data file
    """
    content = open(file_path).readlines()[1:]
    lines_list = [float(line) for line in content]
    return lines_list


def read_data(file_path):
    ''' Read data from an Oceanview file
    '''
    content = open(file_path).readlines()
    all_nm = list()
    all_raw = list()
    all_signal = list()
    for line in content:
        if line[0] in ['#', 'W', 'U']:
            print(line.strip('\n'))
        elif len(line.split('\t')) != 3:
            pass
        elif len(line.split('\t')) == 3:
            line = line.replace(',', '.')
            data = line.split('\t')
            all_nm.append(float(data[0]))
            all_raw.append(float(data[1]))
            all_signal.append(float(data[1]))

    np_nm = np.array(all_nm, 'float')
    np_raw = np.array(all_raw, 'float')
    np_signal = np.array(all_signal, 'float')

    return np_nm, np_raw, np_signal


def plot_spectrum(np_x, np_y):
    ''' Plot a spectrum from x and y numpy arrays
    '''
    plt.figure()
    plt.plot(np_x, np_y, 'b+--',label='data')
    plt.xlabel(r'$\lambda$ (nm)')
    plt.ylabel('Corrected signal (ADC counts)')
    plt.show()


if __name__ == "__main__":
    # get data from text file
    np_nm, np_raw, np_signal = read_data('./example_data/hg_spectrum.dat')
    # print a few lines
    for i in range(10):
        print('{} {}'.format(np_nm[i], np_signal[i]))
    # plot data
    plot_spectrum(np_nm, np_signal)
