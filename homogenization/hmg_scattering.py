import sys
sys.path.append('../')  # Adjust the path as needed
from parameters import *

# core homogenization

# given data
macro_scattering_U235 = 15.04 * 10 ** (-24)
macro_scattering_U238 =  9.360 * 10 ** (-24) 
macro_scattering_O = 3.780 * 10 ** (-24)
macro_scattering_Fe = 0.933
macro_scattering_H2O = 3.45


# calculations

macro_cs_scattering = (((macro_scattering_U235 + macro_scattering_U238 + macro_scattering_O)*(tt_vol_UO2)) +
                       (macro_scattering_H2O * tt_vol_H2O) + (macro_scattering_Fe * tt_vol_Fe))/tt_act_core_vol


micro_cs_scattering = (((macro_scattering_U235 + macro_scattering_U238 + macro_scattering_O)*(tt_vol_UO2)) +
                       (macro_scattering_H2O * tt_vol_H2O) + (macro_scattering_Fe * tt_vol_Fe))/(tt_act_core_vol * (n_UO2 + n_H2O + n_Fe))


# source:
# 1- Nuclear Reactor Analysis - James Duderstadt, Louis Hamilton  (data)
# 2- https://atom.kaeri.re.kr/old/ton/ (data)