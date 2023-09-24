import sys
sys.path.append('../')  # Adjust the path as needed
from parameters import *

# core homogenization

# given data
micro_gamma_U235 = 98.81
micro_gamma_U238 = 2.73
micro_gamma_O = 190*10**(-3)
macro_gamma_Fe = 2.813
macro_abs_H2O = 0.022



# parameters
macro_gamma_U235 = n_U235 * micro_gamma_U235 * 10 ** (-24)
macro_gamma_U238 = n_U238 * micro_gamma_U238 * 10 ** (-24)
macro_gamma_O = n_O * micro_gamma_O * 10 ** (-24)
# print("238",macro_gamma_U238)
# print("235",macro_gamma_U235)
# print("O",macro_gamma_O)


# calculations

macro_cs_gamma_fuel = ((macro_gamma_U235 + macro_gamma_U238 + macro_gamma_O)*(tt_vol_UO2)/tt_act_core_vol)  ####assim msm??


macro_cs_gamma = (((macro_gamma_U235 + macro_gamma_U238 + macro_gamma_O)*(tt_vol_UO2)) +
                       (macro_abs_H2O * tt_vol_H2O) + (macro_gamma_Fe * tt_vol_Fe))/tt_act_core_vol
# print("macro_cs_gamma", macro_cs_gamma)

micro_cs_gamma = (((macro_gamma_U235 + macro_gamma_U238 + macro_gamma_O)*(tt_vol_UO2)) +
                       (macro_abs_H2O * tt_vol_H2O) + (macro_gamma_Fe * tt_vol_Fe))/(tt_act_core_vol * (n_UO2 + n_H2O + n_Fe))

# print("micro_cs_gamma", micro_cs_gamma)
# source:
# 1- Nuclear Reactor Analysis - James Duderstadt, Louis Hamilton  (data)
