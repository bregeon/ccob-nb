#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:08:13 2019

@authors: andres, bregeon
"""

from matplotlib import pyplot  as plt
import numpy as np


def read_data(file_path='../data/diode_response.dat'):
    ''' Read diode data from a text file
    '''
    wl_dict=dict()
    lbd=[]
    pwr=[]
    error=[]
    content = open(file_path).readlines()[1:]
    i=0
    for line in content:
        one = line.split()
        wl = int(one[0])
        pow = float(one[1])
        err = float(one[2])
        lbd.append(wl)
        pwr.append(pow)
        error.append(err)
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
    plt.show()


def val(wlgt,lbd,pwr,x2):
    ''' Linear interpolation
    '''
    for i in range(len(x2)):
        if lbd[i]==wlgt:
            return (wlgt,(pwr[lbd.index(wlgt)]))

    x3=list(np.zeros(len(x2)))
    for i in range(len(x2)):
        x3[i]=x2[i]-wlgt
        x3[i]=abs(x3[i])
    a=min(x3)
    idxa=x3.index(a)
    ya=pwr[idxa]
    xa=x2[idxa]
    x3[idxa]=2000
    b=np.min(np.abs(x3))
    idxb=x3.index(b)
    yb=pwr[idxb]
    xb=x2[idxb]
    t=ya-((yb-ya)/(xb-xa))*xa
    return (wlgt,((yb-ya)/(xb-xa))*wlgt + t)

if __name__ == "__main__":
    # get data from text file
    wl_dict = read_data()

    # print table back for crosscheck
    # print_diode(wl_dict)

    # plot diode response
    plot_diode(wl_dict)

    # wl_list = list(wl_dict.keys())
    # wl_list.sort()
    # pwr = list()
    # for wl in wl_list:
    #     pwr.append(wl_dict[wl][0])
    #
    # x2=list(np.copy(lbd))
    #
    # print(val(1000,lbd,pwr,x2))
    # print(val(1001,lbd,pwr,x2))
    # print(val(1004,lbd,pwr,x2))
    #
    # tableau=np.zeros((len(lbd),3))
    # for i in range(len(lbd)):
    #     tableau[i,0]=lbd[i]
    #     tableau[i,1]=pwr[i]
    #     tableau[i,2]=error[i]
