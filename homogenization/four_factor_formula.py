from hmg_gamma import *
from hmg_scattering import macro_cs_scattering, macro_scattering_H2O, micro_scattering_U238
from hmg_fission import macro_cs_fission
from hmg_absorption import macro_cs_absorption, micro_abs_H2O
from parameters import *
import sys
sys.path.append('../')  # Adjust the path as needed
# given data
v = 2.4355  # for thermal 235U

# Reproduction Factor ############
rpd_fact = v * macro_cs_fission/macro_cs_absorption
print("rpd_fact", rpd_fact)

# Fast Fission Factor
total_cs = macro_cs_fission + macro_cs_gamma + macro_cs_absorption + macro_cs_scattering
typical_value = 1.04
fast_fis_fact = 1 + (power/(1-power*((v*macro_cs_fission+macro_cs_scattering)/(total_cs)))) * \
    (macro_cs_fission/(total_cs)) * \
    (v-1-(macro_cs_gamma/macro_cs_fission))
print("fast_fis_fact",fast_fis_fact)
#problema na cross section total

# Thermal Utilization Factor
ther_utiliz_fact = macro_cs_gamma_fuel/(macro_cs_gamma_fuel+macro_abs_H2O)
print("ther_utiliz_fact", ther_utiliz_fact)

# Resonance Escape Probability
density = n_U235
mass_num_target_nucleus = 235.04393
fuel_rod_diameter = 21.4 / 17
log_energy_decrease = 2/(mass_num_target_nucleus+2/3)
# the effective resonance integral
# ieff = 4.45 + 26.6 * np.sqrt(4/(density*fuel_rod_diameter))
# ress_esc_prob = np.e**((-1)*(n_UO2*tt_vol_UO2*ieff*10**(-24)) /
#                        (log_energy_decrease*macro_scattering_H2O*tt_vol_H2O))
N = 0.9505 * n_UO2
auxx = n_H2O/N
ress_esc_prob =  auxx*micro_abs_H2O*10**(24)
print("ress_esc_prob", ress_esc_prob)

kinf = rpd_fact *fast_fis_fact*ther_utiliz_fact* ress_esc_prob
print("kinf", kinf)
# Data:
# https://www.nuclear-power.com/nuclear-power/reactor-physics/nuclear-fission-chain-reaction/resonance-escape-probability/
# http://dspace.mit.edu/bitstream/handle/1721.1/74136/22-05-fall-2006/contents/lecture-notes/lecture04.pdf
