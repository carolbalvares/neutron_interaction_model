import sys
sys.path.append('../')
from parameters import *
from homogenization.hmg_gamma import macro_cs_gamma_fuel
from homogenization.hmg_fission import macro_cs_fission
  # Adjust the path as needed
# material chosen: UO2
initial_neutrons = 100000

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


mi = 2/(3*m)
free_trn_path = 1/(macro_cs_UO2_scattering*(1-mi))
dif_coef = free_trn_path/3
sigma_s = round(macro_cs_UO2_scattering, 3)


# 1 discretization 1 mat
final_neutrons = initial_neutrons * \
    (1 - macro_cs_UO2_scattering)**scattering * \
    (1-macro_cs_UO2_absorption)**absorption
final_neutrons_1d_1m = np.round(final_neutrons)
print("final final_neutrons_1d_1m:", final_neutrons_1d_1m)

# multiple discretization 1 mat
num_discr = int(input('Choose a number of discretization:   '))
final_neutrons = initial_neutrons * \
    ((1-macro_cs_UO2_scattering)**scattering)**num_discr * \
    ((1-macro_cs_UO2_absorption)**absorption)**num_discr
final_neutrons_mult_discr_2m = np.round(final_neutrons)
print("final_neutrons_mult_discr_2m", final_neutrons_mult_discr_2m)


# 2  discretizations with 2 mat
macro_cs_mt2_scattering = 0.0987
macro_cs_mt2_absorption = 0.2205
scattering_mt2 = 1/macro_cs_mt2_scattering
absorption_mt2 = 1/macro_cs_mt2_absorption
final_neutrons = initial_neutrons * \
    (1 - macro_cs_UO2_scattering)**scattering * \
    (1-macro_cs_UO2_absorption)**absorption * \
    (1-macro_cs_mt2_scattering)**scattering_mt2 * \
    (1-macro_cs_mt2_absorption)**absorption_mt2
final_neutrons_2d_2m = np.round(final_neutrons)
print("final_neutrons_2d_2m",final_neutrons_2d_2m)
# strange value https://www.dgtresearch.com/diffusion-coefficients/
# https://www.nuclear-power.com/nuclear-power/reactor-physics/neutron-diffusion-theory/neutron-current-density/
# Não há uma regra específica da comunidade científica para arredondamento de nêutrons além do arredondamento para o número inteiro mais próximo.
