#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:08:13 2019

@authors: Nicolas Andres, Johan Bregeon (bregeon@in2p3.fr)
"""

from matplotlib import pyplot  as plt
import numpy as np


def read_data(file_path='../data/diode_response.dat'):
    ''' Read diode data from a text file
    '''
    wl_dict=dict()
    content = open(file_path).readlines()[1:]
    for line in content:
        one = line.split()
        wl = int(one[0])
        pow = float(one[1])
        err = float(one[2])
        wl_dict[wl]=(pow, err)
    return wl_dict

def print_diode(wl_dict):
    ''' Format a diode dictionnary
    '''
    wl_list = list(wl_dict.keys())
    wl_list.sort()
    for wl in wl_list:
        print('{:<8} {:<10} {:<8}'.format(wl, wl_dict[wl][0], wl_dict[wl][1]))

def plot_diode(wl_dict):
    ''' Plot a diode response
    '''
    wl_list = list(wl_dict.keys())
    wl_list.sort()
    pwr = list()
    for wl in wl_list:
        pwr.append(wl_dict[wl][0])
    plt.plot(wl_list,pwr,'+b',label='Courbe caractéristique photodiode S2281')
    plt.xlabel(r'$\lambda$ (nm)')
    plt.ylabel('Conversion')
    plt.legend()
    plt.grid(linestyle='--', linewidth=0.5)
    plt.show()

def get_value(wl, wl_dict):
    ''' Linear interpolation if not on a reference point
    '''
    # Is there a reference point to get the value from ?
    if wl in wl_dict.keys():
        return wl_dict[wl][0]
   # No, so make a linear interpolation
    wl_list = list(wl_dict.keys())
    wl_list.sort()
    pow = list()
    for one in wl_list:
        pow.append(wl_dict[one][0])
    x2 = list(np.copy(wl_list))
    x3 = list(np.zeros(len(x2)))
    for i in range(len(x2)):
        x3[i] = x2[i]-wl
        x3[i] = abs(x3[i])
    a = min(x3)
    idxa = x3.index(a)
    ya = pow[idxa]
    xa = x2[idxa]
    x3[idxa] = 2000
    b = np.min(np.abs(x3))
    idxb = x3.index(b)
    yb = pow[idxb]
    xb = x2[idxb]
    t = ya-((yb-ya)/(xb-xa))*xa
    return ((yb-ya)/(xb-xa))*wl + t


if __name__ == "__main__":
    # get data from text file
    wl_dict = read_data()

    # print table back for crosscheck
    # print_diode(wl_dict)

    # Test get_value with and with out interpolation
    print('Testing get_value for a number of wavelengths')
    for wl in range(600, 611):
        val = get_value(wl, wl_dict)
        print('{:<8} {:<10}'.format(wl, val))

    # plot diode response
    plot_diode(wl_dict)
