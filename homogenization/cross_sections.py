
### CStt = CSscat + CSabs
### CSAbs = cap radioativa + fissão = N,F + N,G
### CSScat - N,EL + N,NON 
#https://www-nds.iaea.org/exfor/endf.htm
#All data in barns (micro cross-section)
#############################

##U235
#U-235(N,EL) = 14.110209 
#U-235(N,F) = 590.64465
#U-235(N,G) = 100.135796
#U-235(N,NON) = No Data Found

##U238
#U-238(N,EL) = 9.240251
#U-238(N,F) = 1.86321E-5
#U-238(N,G) = 2.7003825
#U-238(N,NON) = No Data Found

##O
#O-16(N,EL) = 3.9152284 
#O-16(N,F) = No Data Found
#O-16(N,G) = 1.709078E-4
#O-16(N,NON) = No Data Found

##H
#U-H(N,EL) = 30.173471
#U-H(N,F) = No Data Found
#U-H(N,G) = 0.3346708
#U-H(N,NON) = No Data Found

##Fe
#U-Fe(N,EL) = 12.191882
#U-Fe(N,F) = No Data Found
#U-Fe(N,G) = 2.6213868
#U-Fe(N,NON) = No Data Found
import sys

sys.path.append("../")
from parameters import *


##Gamma
macro_gamma_Fe = 2.813
macro_abs_H2O = 0.022
micro_gamma_U235 = 100.135796
micro_gamma_U238 = 2.7003825
micro_gamma_O = 1.709078*10**(-4)

macro_gamma_U235 = n_U235 * micro_gamma_U235 * 10 ** (-24)
macro_gamma_U238 = n_U238 * micro_gamma_U238 * 10 ** (-24)
macro_gamma_O = n_O * micro_gamma_O * 10 ** (-24)

macro_cs_gamma = (((macro_gamma_U235 + macro_gamma_U238 + macro_gamma_O)*(tt_vol_UO2)) +
                       (macro_abs_H2O * tt_vol_H2O) + (macro_gamma_Fe * tt_vol_Fe))/tt_act_core_vol
micro_cs_gamma = (((macro_gamma_U235 + macro_gamma_U238 + macro_gamma_O)*(tt_vol_UO2)) +
                       (macro_abs_H2O * tt_vol_H2O) + (macro_gamma_Fe * tt_vol_Fe))/(tt_act_core_vol * (n_UO2 + n_H2O + n_Fe))

##Fission
micro_fission_U235 = 590.64465
micro_fission_U238 = 1.86321*10**(-5)

macro_fission_U235 = micro_fission_U235 * n_U235* 10 ** (-24)
macro_fission_U238 = micro_fission_U238 * n_U238* 10 ** (-24)

macro_cs_fission = (macro_fission_U235 + macro_fission_U238) * tt_vol_UO2 / tt_act_core_vol
# print("macro_fission_U235",macro_fission_U235)
# print("macro_fission_U238",macro_fission_U238)

# print("",)
# print("",)


Na = 6.02214076 * 10**(23)

micro_cs_fission = macro_cs_fission / n_UO2

##Scattering
micro_scattering_U235 = 14.110209 
micro_scattering_U238 = 9.240251
micro_scattering_O = 3.9152284 
micro_scattering_Fe = 12.191882
micro_scattering_H2O = 103 * 10**(-24)

macro_scattering_U235 = micro_scattering_U235 * n_U235
macro_scattering_U238 = micro_scattering_U238 * n_U238
macro_scattering_O = micro_scattering_O * n_O
macro_scattering_Fe = micro_scattering_Fe * n_Fe
macro_scattering_H2O  = micro_scattering_H2O * n_H2O

macro_cs_scattering = (((macro_scattering_U235 + macro_scattering_U238 + macro_scattering_O)*(tt_vol_UO2)) +
                       (macro_scattering_H2O * tt_vol_H2O) + (macro_scattering_Fe * tt_vol_Fe))/tt_act_core_vol
micro_cs_scattering = (((macro_scattering_U235 + macro_scattering_U238 + macro_scattering_O)*(tt_vol_UO2)) +
                       (macro_scattering_H2O * tt_vol_H2O) + (macro_scattering_Fe * tt_vol_Fe))/(tt_act_core_vol * (n_UO2 + n_H2O + n_Fe))
# print("micro_cs_scattering", micro_cs_scattering)
##Absorption
micro_abs_H2O = 0.66 * 10**(-24)
macro_cs_absorption = macro_cs_gamma + macro_cs_fission
micro_cs_absorption = (macro_cs_absorption/(n_UO2 + n_H2O + n_Fe))
# print("macro_cs_gamma", macro_cs_gamma)
# print("macro_cs_fission", macro_cs_fission)
# print("micro_cs_absorption", micro_cs_absorption)
print("macro_cs_absorption", macro_cs_absorption)
# macro_cs_gamma 0.8205873192283825
# macro_cs_fission 2.0560876547678343e+23
# micro_cs_absorption 1.450667024580102e-24
# macro_cs_absorption macro_cs_absorption 1.0261960847051659
# print("n_UO2",n_UO2)
# print("n_H2O",n_H2O)
# print("n_Fe",n_Fe)
micro_cs_absorptiona = (macro_cs_absorption * tt_vol_UO2) / (tt_act_core_vol * (n_UO2 + n_H2O + n_Fe))
# print("oii",micro_cs_absorptiona )