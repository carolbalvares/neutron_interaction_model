from homogenization.hmg_fission import macro_cs_fission
from homogenization.hmg_gamma import macro_cs_gamma_fuel
from parameters import *
import sys
sys.path.append('../')  # Adjust the path as needed

# material chosen: UO2
initial_neutrons = 1000

micro_scattering_U235 = 15.04 * 10 ** (-24)
micro_scattering_U238 = 9.360 * 10 ** (-24)
micro_scattering_O = 3.780 * 10 ** (-24)

macro_scattering_U235 = micro_scattering_U235 * n_U235
macro_scattering_U238 = micro_scattering_U238 * n_U238
macro_scattering_O = micro_scattering_O * n_O

macro_cs_UO2_scattering = (macro_scattering_U235 + macro_scattering_U238 +
                           macro_scattering_O)*(tt_vol_UO2) / tt_act_core_vol
# macro_cs_UO2_scattering = 0.118

macro_cs_UO2_absorption = macro_cs_gamma_fuel + macro_cs_fission
# macro_cs_UO2_absorption = 0.258

scattering = 1/macro_cs_UO2_scattering

absorption = 1/macro_cs_UO2_absorption
print(scattering)
print(absorption)


mi = 2/(3*m)
free_trn_path = 1/(macro_cs_UO2_scattering*(1-mi))
dif_coef = free_trn_path/3
sigma_s = round(macro_cs_UO2_scattering, 3)


# 1 discretization

final_neutrons = initial_neutrons * \
    (1 - macro_cs_UO2_scattering)**scattering * \
    (1-macro_cs_UO2_absorption)**absorption

print("final neutrons:", final_neutrons)

# 2 discretization


# strange value https://www.dgtresearch.com/diffusion-coefficients/
# https://www.nuclear-power.com/nuclear-power/reactor-physics/neutron-diffusion-theory/neutron-current-density/
