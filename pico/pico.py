#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:34 2020

@authors: Johan Bregeon (bregeon@in2p3.fr)
"""

from matplotlib import pyplot  as plt
import numpy as np
from datetime import datetime


def read_data(file_path='../data/PicoRead.csv'):
    ''' Read diode data from a text file
    '''
    date_list = list()
    current_list = list()
    content = open(file_path).readlines()[1:]
    for line in content:
        data = line.split()
        date_list.append(np.datetime64(datetime.strptime(data[0],
                                       '%Y%m%d-%H%M%S'), 's'))
        current_list.append(float(data[1]))
    date_array = np.array(date_list)
    current_array = np.array(current_list)
    time_series = (date_array, current_array)
    return time_series

def print_pico(time_series):
    ''' Format a pico time series
    '''
    print('Date\tCurrent')
    for date, current in zip(time_series[0], time_series[1]):
        print('{:<12} {:<8}'.format(date, current))

def plot_time_series(time_series, file_path=None, save=False):
    ''' Plot a diode response
    '''
    mean_current = np.mean(time_series[1])
    min_time = min(time_series[0])
    max_time = max(time_series[0])
    label='Picoamperemeter time series'
    if file_path is not None:
        label = 'Picoamperemeter - %s'%file_path.split('/')[-1]
    fig = plt.figure(1, figsize=(12, 6))
    plt.plot(time_series[0], time_series[1],'+b', label=label)
    plt.xlabel('Time')
    plt.ylabel('Current')
    plt.ylim(ymin=mean_current*0.98, ymax=mean_current*1.02)
    plt.hlines(mean_current*0.99, min_time, max_time, colors='r')
    plt.hlines(mean_current*1.01, min_time, max_time, colors='r')
    plt.text(max_time-30, mean_current*0.987, '-1%')
    plt.text(max_time-30, mean_current*1.013, '+1%')
    plt.legend()
    plt.grid(linestyle='--', linewidth=0.5)
    plt.show()
    if save:
        plt.savefig(file_path[:-4]+'.png')


if __name__ == "__main__":
    # get data from text file
    time_series = read_data()

    # plot diode response
    plot_time_series(time_series)
