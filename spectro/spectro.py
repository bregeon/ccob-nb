#/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue 09 Jul 2019 04:43:23 PM CEST

@author: bregeon
"""
import matplotlib.pyplot as plt
import numpy as np


def connect():
    ''' Try to connect to the spectrometer
    '''
    import seabreeze
    seabreeze.use("pyseabreeze")

    import seabreeze.spectrometers as sb
    spec = sb.Spectrometer.from_serial_number()
    spec.integration_time_micros(20000)
    spec.wavelengths()

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
        all_x.append(float(xy[0]))
        all_y.append(float(xy[1]))

    np_x = np.array(all_x, 'float')
    np_y = np.array(all_y, 'float')

    return np_x, np_y

def plot_spectrum(np_x, np_y):
    ''' Plot a spectrum from x and y numpy arrays
    '''
    plt.figure()
    plt.plot(np_x, np_y, 'b+--',label='data')
    plt.show()


if __name__ == "__main__":
    # get data from text file
    np_x, np_y = read_data('data/HDX004411_11-07-07-346.txt')
    # print a few lines
    for i in range(10):
        print('{} {}'.format(np_x[i], np_y[i]))
    # plot data
    plot_spectrum(np_x, np_y)
