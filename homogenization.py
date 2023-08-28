import numpy as np
from parameters import *

# core homogenization

# given data
micro_gamma_U235 = 101
micro_gamma_U238 = 2.73
micro_ab_O = 20 * 10**(-5)
macro_ab_Fe = 0.22
macro_ab_H2O = 0.022
Na = 6.02214076 * 10**(23)
dens = 10.5  # convention

# atomic number density : N = (density*Na)/m
m = ((0.0495/235.04393 + 0.9505/238.05078)**(-1)+15.999*2)
n_UO2 = dens * Na / m
n_U235 = (0.0495 * Na * 10.5 / 235.04393) * (238.05078 / m)
n_U238 = (0.9505 * Na * 10.5 / 238.05078) * (235.04393 / m)
n_O = 2 * n_UO2
n_Fe = 7.874 * Na / 55.845
n_H2O = 0.999 * Na / 18.015

# parameters
macro_gamma_U235 = n_U235 * micro_gamma_U235 * 10 ** (-24)
macro_gamma_U238 = n_U238 * micro_gamma_U238 * 10 ** (-24)
macro_gamma_O = n_O * micro_ab_O * 10 ** (-24)


# calculations

macro_gamma_gamma = (((macro_gamma_U235 + macro_gamma_U238 + macro_gamma_O)*(tt_vol_UO2)) +
                       (micro_ab_O * tt_vol_H2O) + (macro_ab_Fe * tt_vol_Fe))/tt_act_core_vol


micro_gamma_gamma = (((macro_gamma_U235 + macro_gamma_U238 + macro_gamma_O)*(tt_vol_UO2)) +
                       (macro_ab_H2O * tt_vol_H2O) + (macro_ab_Fe * tt_vol_Fe))/(tt_act_core_vol * (n_UO2 + n_H2O + n_Fe))


macro_gamma_s = (((macro_gamma_U235 + macro_gamma_U238 + macro_gamma_O)*(tt_vol_UO2)) +
                       (macro_ab_H2O * tt_vol_H2O) + (macro_ab_Fe * tt_vol_Fe))/tt_act_core_vol


# macro sigma n s = (sum of macroscopic cross section of U235, U238 and O) * Vfuel + macroscopic cross section H2O * VH2O + macroscopic cross section Fe * VolFe 
# + (sum of macroscopic cross section U238 (?????????) and oxygen) * (Voxygen(? como achar)


# micro signa n s = ((sum of macroscopic cross section of U235, U238 and O) * Vfuel + macroscopic cross section H2O * VH2O + macroscopic cross section Fe * VolFe)
# / (Vtotal*(NUO2 + NH2O + NFe))

#macro sigma n f = (Macroscopic section (U238 OU 235????)*Vfuel)

#micro sigma n f = (Macroscopic section (U238 OU 235????)*Vfuel + Macroscopic Section O * Vfuel)/(Nfuel + ?????)*Vtotal


#macro sigma tr = micro sigma tr U238 * NU238 * Vfuel + micro sigma tr U235 * NU235 * VFuel + (microsigma tr*N*V)H2O + (microsigma tr*N*V)Fe


#diffusion coefficient = d_coef = 1/(3*macro sigma tr)

#square of diffusion lenght = sq_d_len = D/macro sigma absortion (qual elemento usar para o sigma de absorção?)


# source:
# 1- Nuclear Reactor Analysis - James Duderstadt, Louis Hamilton  (data)