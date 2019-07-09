# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:23:22 2019

@author: andres, bregeon
"""

import sys
import numpy as np
from utils.tools import fit_peak

#spectre_lampe_calib_100ms.dat
#dat = np.loadtxt('spectre_lampe_calib_10ms.txt')
# content = open('HDX004411_10-13-13-243.txt').readlines()[14:]
# content = open('HDX004411_14-25-09-210.txt').readlines()[14:]
# content = open('HDX004411_15-21-26-328.txt').readlines()[14:]
# content = open('data/HDX004411_15-26-27-108.txt').readlines()[14:] # 20/20 um, s=1.3
# content = open('data/HDX004411_10-36-24-949.txt').readlines()[14:] # 900 nm, 7 um, s=1.3
content = open('data/HDX004411_11-07-07-346.txt').readlines()[14:] # 400 nm, 7 um, s=1.4

# content = open('spectre_lampe_calib_100ms.txt').readlines()[14:]


all_x = list()
all_y = list()
for line in content:
    line = line.replace(',', '.')
    xy = line.split('\t')
    all_x.append(float(xy[0]))
    all_y.append(float(xy[1]))

np_x = np.array(all_x, 'float')
np_y = np.array(all_y, 'float')

wl = 400

fit_peak(400, np_x, np_y)




#HDX004411_14_47_05_194.dat    400nm
