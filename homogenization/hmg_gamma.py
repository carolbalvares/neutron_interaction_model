import sys
sys.path.append('../')  # Adjust the path as needed
from parameters import *

# core homogenization

# given data
micro_gamma_U235 = 101
micro_gamma_U238 = 2.73
micro_ab_O = 20 * 10**(-5)
macro_ab_Fe = 0.22
macro_ab_H2O = 0.022



# parameters
macro_gamma_U235 = n_U235 * micro_gamma_U235 * 10 ** (-24)
macro_gamma_U238 = n_U238 * micro_gamma_U238 * 10 ** (-24)
macro_gamma_O = n_O * micro_ab_O * 10 ** (-24)


# calculations

macro_cs_gamma = (((macro_gamma_U235 + macro_gamma_U238 + macro_gamma_O)*(tt_vol_UO2)) +
                       (micro_ab_O * tt_vol_H2O) + (macro_ab_Fe * tt_vol_Fe))/tt_act_core_vol


micro_cs_gamma = (((macro_gamma_U235 + macro_gamma_U238 + macro_gamma_O)*(tt_vol_UO2)) +
                       (macro_ab_H2O * tt_vol_H2O) + (macro_ab_Fe * tt_vol_Fe))/(tt_act_core_vol * (n_UO2 + n_H2O + n_Fe))


# source:
# 1- Nuclear Reactor Analysis - James Duderstadt, Louis Hamilton  (data)
