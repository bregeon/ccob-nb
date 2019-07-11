"""
Created on Tue 09 Jul 2019 03:30:31 PM CEST

@author: Johan Bregeon
"""

import matplotlib.pyplot as plt
import numpy as np
from lmfit.models import ExponentialModel, GaussianModel
from spectro.spectro import read_data


def fit_peak(wl, np_x, np_y, with_plot=True, plot_components=False):
    ''' Fit one peak
        wl wavelength
        x axis values as a numpy array
        y axis values as a numpy array
    '''
    i_min = len(np_x)-sum(np_x>wl) - 10
    i_max = len(np_x)-sum(np_x>wl) + 10

    x = np_x[i_min:i_max]
    many_x = np.arange(x[0], x[-1], 0.01)
    y = np_y[i_min:i_max]

    exp_mod = ExponentialModel(prefix='exp_')
    pars = exp_mod.guess(y, x=x)

    gauss1 = GaussianModel(prefix='g1_')
    pars.update(gauss1.make_params())
    pars['g1_center'].set(wl, min=wl-5, max=wl+5)
    pars['g1_sigma'].set(1, min=0.01)
    pars['g1_amplitude'].set(50000, min=10)

    mod = gauss1 + exp_mod
    # init = mod.eval(pars, x=many_x)
    out = mod.fit(y, pars, x=x)
    comps = out.eval_components(x=many_x)
    print(out.fit_report(min_correl=0.5))
    print('Gaussian line model')
    try:
        print('Mean={:.2f}+/-{:.2f}\tFWHM={:.2f}+/-{:.2f}'.format(
           out.params['g1_center'].value, out.params['g1_center'].stderr,
           out.params['g1_fwhm'].value, out.params['g1_fwhm'].stderr))
    except:
        print('Fit did not converge')

    if with_plot:
        fig = plt.figure()
        out.plot(fig=fig, numpoints=100)
        plt.show()

    # if with_plot:
    #     plt.figure()
    #     plt.plot(x, y, 'b+',label='data')
    #     # plt.plot(many_x, init, 'k--')
    #     # plt.plot(x, out.best_fit, 'r',label='fit')
    #     full_model = mod.eval(out.params, x=many_x)
    #     plt.plot(many_x, full_model, 'r--',label='model')
    #     plt.legend()
    #     if plot_components:
    #         plt.plot(many_x , comps['g1_'], 'b--')
    #         plt.plot(many_x, comps['exp_'], 'k--')
    #     plt.show()
    #
    return out


if __name__ == "__main__":
    # get data from text file and fit
    np_x, np_y = read_data('data/HDX004411_11-07-07-346.txt')
    out = fit_peak(400, np_x, np_y, plot_components=False)
