#!/usr/bin/env python
"""
Wrapper to run code...

"""
__author__ = "Martin De Kauwe"
__version__ = "1.0 (10.04.2019)"
__email__ = "mdekauwe@gmail.com"

import numpy as np
import matplotlib.pyplot as plt
from gain_risk_model_other import gain_risk_model_other

G = gain_risk_model_other()
psoil = np.linspace(0.1, 2)

N_models = 7
N_samples = len(psoil)
all_opt_a = np.zeros((N_samples,N_models))
all_opt_g = np.zeros((N_samples,N_models))
all_opt_p = np.zeros((N_samples,N_models))

for i,ps in enumerate(psoil):

    G.p_soil = ps
    opt_a1, opt_g1, opt_p1 = G.get_optima_sperry()
    opt_a2, opt_g2, opt_p2 = G.get_optima_dewar()
    opt_a3, opt_g3, opt_p3 = G.get_optima_dewar_mod()
    opt_a4, opt_g4, opt_p4 = G.get_optima_eller()
    opt_a5, opt_g5, opt_p5 = G.get_optima_lambda()
    opt_a6, opt_g6, opt_p6 = G.get_optima_prentice()
    opt_a7, opt_g7, opt_p7 = G.get_optima_wap()

    opt = np.array([opt_a1,opt_a2,opt_a3,opt_a4,opt_a5,opt_a6,opt_a7])
    all_opt_a[i,:] = opt

    opt = np.array([opt_g1,opt_g2,opt_g3,opt_g4,opt_g5,opt_g6,opt_g7])
    all_opt_g[i,:] = opt

    opt = np.array([opt_p1,opt_p2,opt_p3,opt_p4,opt_p5,opt_p6,opt_p7])
    all_opt_p[i,:] = opt

psoil *= -1
psoil = np.flip(psoil)
all_opt_a = np.flip(all_opt_a)
all_opt_g = np.flip(all_opt_g)
all_opt_p = np.flip(all_opt_p)


fig = plt.figure(figsize=(9,10))
fig.subplots_adjust(hspace=0.1)
fig.subplots_adjust(wspace=0.15)
plt.rcParams['text.usetex'] = False
plt.rcParams['font.family'] = "sans-serif"
plt.rcParams['font.sans-serif'] = "Helvetica"

plt.rcParams['axes.labelsize'] = 14
plt.rcParams['font.size'] = 14
plt.rcParams['legend.fontsize'] = 14
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

labels = ["sperry", "dewar", "dewar_mod", "eller", "lambda", "prentice", "wolf"]

for i in range(N_models):
    ax1.plot(psoil, all_opt_a[:,i], label=labels[i])
    ax2.plot(psoil, all_opt_g[:,i])

ax1.legend(numpoints=1, loc="best", ncol=1, frameon=False)
plt.setp(ax1.get_xticklabels(), visible=False)
ax1.set_ylabel("opt_a")
ax2.set_ylabel("opt_g")
ax2.set_xlabel("$\Psi$$_{s}$ (MPa)")
plt.show()
