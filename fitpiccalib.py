# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:23:22 2019

@author: andres
"""

import matplotlib.pyplot as plt
import numpy as np
from lmfit.models import ExponentialModel, GaussianModel

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
i_min = len(np_x)-sum(np_x>wl) - 10
i_max = len(np_x)-sum(np_x>wl) + 10

x = np_x[i_min:i_max]
y = np_y[i_min:i_max]
# x = dat[:, 0]
# y = dat[:, 1]


exp_mod = ExponentialModel(prefix='exp_')
pars = exp_mod.guess(y, x=x)

gauss1 = GaussianModel(prefix='g1_')
pars.update(gauss1.make_params())



pars['g1_center'].set(wl, min=wl-5, max=wl+5)
pars['g1_sigma'].set(1, min=0.01)
pars['g1_amplitude'].set(50000, min=10)



mod = gauss1 + exp_mod

init = mod.eval(pars, x=x)


out = mod.fit(y, pars, x=x)
print(out.fit_report(min_correl=0.5))


plot_components = False


plt.figure()

plt.plot(x, y, 'b+--',label='data')
plt.plot(x, init, 'k--')
plt.plot(x, out.best_fit, 'r',label='fit')
plt.legend()

if plot_components:
    comps = out.eval_components(x=x)
    plt.plot(x, comps['g1_'], 'b--')
    plt.plot(x, comps['exp_'], 'k--')

plt.show()





#HDX004411_14_47_05_194.dat    400nm
