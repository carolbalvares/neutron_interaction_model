import sys
sys.path.append('../')  # Adjust the path as needed
from parameters import *

# given data (micro scattering cross section)
micro_scattering_U235 = 15.04 * 10 ** (-24)
micro_scattering_U238 =  9.360 * 10 ** (-24) 
micro_scattering_O = 3.780 * 10 ** (-24)
micro_scattering_Fe = 11 * 10**(-24)
micro_scattering_H2O = 103 * 10**(-24)

# calculating macro scattering cross section
macro_scattering_U235 = micro_scattering_U235 * n_U235
macro_scattering_U238 = micro_scattering_U238 * n_U238
macro_scattering_O = micro_scattering_O * n_O
macro_scattering_Fe = micro_scattering_Fe * n_Fe
macro_scattering_H2O  = micro_scattering_H2O * n_H2O

#calculating homogeneous macro and micro scattering cross section
macro_cs_scattering = (((macro_scattering_U235 + macro_scattering_U238 + macro_scattering_O)*(tt_vol_UO2)) +
                       (macro_scattering_H2O * tt_vol_H2O) + (macro_scattering_Fe * tt_vol_Fe))/tt_act_core_vol


micro_cs_scattering = (((macro_scattering_U235 + macro_scattering_U238 + macro_scattering_O)*(tt_vol_UO2)) +
                       (macro_scattering_H2O * tt_vol_H2O) + (macro_scattering_Fe * tt_vol_Fe))/(tt_act_core_vol * (n_UO2 + n_H2O + n_Fe))


# source:
# 1- Nuclear Reactor Analysis - James Duderstadt, Louis Hamilton  (data)
# 2- https://atom.kaeri.re.kr/old/ton/ (data)