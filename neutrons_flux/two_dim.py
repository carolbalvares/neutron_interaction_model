from homogenization.hmg_fission import macro_cs_fission
from homogenization.hmg_gamma import macro_cs_gamma_fuel
from parameters import *
import sys
sys.path.append('../')
# Adjust the path as needed
# material chosen: UO2
initial_neutrons = 10**6

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


# 2 dimensions 1 mat
# assuming lenght = 1cm
scattering = 1/macro_cs_UO2_scattering

absorption = 1/macro_cs_UO2_absorption

direct_ab = macro_cs_UO2_absorption
diagonal_ab = np.sqrt(2) * macro_cs_UO2_absorption
direct_sc = macro_cs_UO2_scattering
diagonal_sc = np.sqrt(2) * macro_cs_UO2_scattering
initial_neutrons_2d = initial_neutrons/8
# ja que a fonte é uniforme, ela emite o mesmo tanto para a diagonal e para  reto?
final_neutrons = initial_neutrons_2d * \
    (1 - macro_cs_UO2_scattering)**diagonal_sc * \
    (1-macro_cs_UO2_absorption)**diagonal_ab
final_neutrons_2d_direct = np.round(final_neutrons)
final_neutrons = final_neutrons_2d_direct * \
    (1 - macro_cs_UO2_scattering)**direct_sc * \
    (1-macro_cs_UO2_absorption)**direct_ab
final_neutrons_2d_diagonal = np.round(final_neutrons)
print("final_neutrons_2d_direct:", final_neutrons_2d_direct)
print("final_neutrons_2d_diagonal", final_neutrons_2d_diagonal)
print(4*final_neutrons_2d_direct + 4 * final_neutrons_2d_diagonal)
