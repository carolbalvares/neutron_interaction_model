import sys
sys.path.append('../')  # Adjust the path as needed
from parameters import *
from hmg_absorption import macro_cs_absorption
from hmg_fission import macro_cs_fission
from hmg_scattering import macro_cs_scattering, macro_scattering_H2O
from hmg_gamma import *
#given data
v = 2.4355 # for thermal 235U

#Reproduction Factor
rpd_fact = v * macro_cs_fission/macro_cs_absorption
# print("rpd_fact", rpd_fact)

#Fast Fission Factor
typical_value = 1.04
# fast_fiss_fact = 1 + (power/(1-power*((v*macro_cs_fission + macro_cs_scattering)/macro_cs_tt)))*((macro_cs_fission/macro_cs_tt)*(v-1-macro_cs_gamma/macro_cs_fission))

#Thermal Utilization Factor
#posso usar o gama ou tenho que calcular o abs para os que calculei gama? e teem que ser a media? Usar so da agua?
ther_utiliz_fact = macro_cs_gamma_fuel/(macro_cs_gamma_fuel+macro_ab_H2O)
# print("ther_utiliz_fact", ther_utiliz_fact)

#Resonance Escape Probability
density = n_U235
mass_num_target_nucleus = 235.04393
fuel_rod_diameter = 21.4 / 17
print(fuel_rod_diameter)
log_energy_decrease = 2/(mass_num_target_nucleus+2/3)
print(log_energy_decrease)
ieff = 4.45 + 26.6 * np.sqrt(4/(density*fuel_rod_diameter))  #the effective resonance integral
print(ieff)
ress_esc_prob = np.e**((-1)*(n_UO2*tt_vol_UO2*ieff*10**(-24))/(log_energy_decrease*macro_scattering_H2O*tt_vol_H2O))
print("ress_esc_prob", ress_esc_prob)
##Data:
#https://www.nuclear-power.com/nuclear-power/reactor-physics/nuclear-fission-chain-reaction/resonance-escape-probability/
#http://dspace.mit.edu/bitstream/handle/1721.1/74136/22-05-fall-2006/contents/lecture-notes/lecture04.pdf 