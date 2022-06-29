#/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue 09 Jul 2019 04:43:23 PM CEST

@author: bregeon
"""
import matplotlib.pyplot as plt
import numpy as np


def read_data(file_path):
    ''' Read data from an Oceanview file
    @TODO get info from header
    '''
    content = open(file_path).readlines()[14:]
    all_x = list()
    all_y = list()
    for line in content:
        line = line.replace(',', '.')
        xy = line.split('\t')
        try:
            all_x.append(float(xy[0]))
            all_y.append(float(xy[1]))
        except:
            pass

    np_x = np.array(all_x, 'float')
    np_y = np.array(all_y, 'float')

    return np_x, np_y

def plot_spectrum(np_x, np_y):
    ''' Plot a spectrum from x and y numpy arrays
    '''
    plt.figure()
    plt.plot(np_x, np_y, 'b+--',label='data')
    plt.xlabel(r'$\lambda$ (nm)')
    plt.ylabel('Counts')
    plt.show()


if __name__ == "__main__":
    # get data from text file
    np_x, np_y = read_data('../data/data_12062020_spectro/20200612_103843_Spectrum_A1-I6.csv')
    # print a few lines
    for i in range(10):
        print('{} {}'.format(np_x[i], np_y[i]))
    # plot data
    plot_spectrum(np_x, np_y)
