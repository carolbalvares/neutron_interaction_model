import numpy as np

## core homogenization


## considering all cross section gama irradiation

micro_gam_cs_U235 = 101
micro_gam_cs_U238 = 2.73

#atomic_density : N = (density*Na)/m 
Na =  6.02214076 * 10**(23)
dens = 10.5 #convention
m = ((0.0495/235.04393 + 0.9505/238.05078)**(-1)+15.999*2)
N = dens * Na / m

# # parameters
macro_gam_cs_U235 = N *  micro_gam_cs_U235
macro_gam_cs_U238 = N *  micro_gam_cs_U238

macro_abs_cs_oxy = 0
# v_tt_UO2 = 
macrco_abs_cs_H2O = 0.022
# v_H2O = 
macro_abs_cs_Fe = 0.222
# v_Fe = 

# # calculation
# cs_g_V_t = ((cs_U235 + cs_U238 + cs_oxy)*(v_tt_UO2)) + (cs_H2O * v_H2O) + (cs_Fe * v_Fe)

# ## dictionary: 

# ## source: