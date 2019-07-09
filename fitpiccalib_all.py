# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:23:22 2019

@author: andres
"""

import matplotlib.pyplot as plt
import numpy as np
from lmfit.models import ExponentialModel, GaussianModel

from data.Hg2_calibration_lamp import calib_lines

#spectre_lampe_calib_100ms.dat
#dat = np.loadtxt('spectre_lampe_calib_10ms.txt')
content = open('spectre_lampe_calib_100ms.txt').readlines()[14:]

all_x = list()
all_y = list()
for line in content:
    line = line.replace(',', '.')
    xy = line.split('\t')
    all_x.append(float(xy[0]))
    all_y.append(float(xy[1]))

np_x = np.array(all_x, 'float')
np_y = np.array(all_y, 'float')

fwhm=[]
wlg=[]

def fit_pic(wl):
    i_min = len(np_x)-sum(np_x>wl) - 5
    i_max = len(np_x)-sum(np_x>wl) + 10

    x = np_x[i_min:i_max]
    y = np_y[i_min:i_max]
 
    exp_mod = ExponentialModel(prefix='exp_')
    pars = exp_mod.guess(y, x=x)

    gauss1 = GaussianModel(prefix='g1_')
    pars.update(gauss1.make_params())



    pars['g1_center'].set(wl, min=wl-10, max=wl+10)
    pars['g1_sigma'].set(1, min=0.01)
    pars['g1_amplitude'].set(50000, min=10)



    mod = gauss1 + exp_mod

    init = mod.eval(pars, x=x)


    out = mod.fit(y, pars, x=x)
    print(out.fit_report(min_correl=0.5))


    plot_components = False


    plt.figure()

    plt.plot(x, y, 'b+--',label='data')
    #plt.plot(x, init, 'k--')
    plt.plot(x, out.best_fit, 'r',label='fit : fwhm = %s'%(round(out.params['g1_fwhm'].value,3)))
    plt.legend()

    fwhm.append(round(out.params['g1_fwhm'].value,3))
    wlg.append(wl)

    if plot_components:
        comps = out.eval_components(x=x)
        plt.plot(x, comps['g1_'], 'b--')
        plt.plot(x, comps['exp_'], 'k--')

    plt.show()

for one in calib_lines:
    fit_pic(one)

plt.figure()
plt.plot(wlg,fwhm,'+b')
plt.xlabel(r'$\lambda$ (nm)')
plt.ylabel('Event')
# plt.legend()
plt.show()
