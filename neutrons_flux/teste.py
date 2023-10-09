from parameters import *
from homogenization.hmg_scattering import macro_scattering_Fe
from homogenization.hmg_gamma import macro_cs_gamma_fuel, macro_gamma_Fe
from homogenization.hmg_fission import macro_cs_fission
import sys
sys.path.append('../')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Adjust the path as needed
# material chosen: UO2

# mi = 2/(3*m)
# free_trn_path = 1/(macro_cs_UO2_scattering*(1-mi))
# dif_coef = free_trn_path/3
# sigma_s = round(macro_cs_UO2_scattering, 3)


class One_d_one_material:
    def __init__(self, num_samples, distance_array, tt_cross_section):
        self.num_samples = num_samples
        self.distance_array = distance_array
        self.tt_cross_section = tt_cross_section

    def n_neutrons_cross(self, num_samples, distance_array, tt_cross_section):
        self.distance_array = distance_array
        self.num_samples = num_samples
        self.tt_cross_section = tt_cross_section
        # cant_cross_array = np.array([])
        cross_array = np.array([])
        cross_amount_array = np.array([])
        dist_to_collision = 0
        aux_array = np.array([])
        r_samples_array = np.random.rand(num_samples).round(3)
        # print("samples array:   ", r_samples_array)
        aux_array = r_samples_array
        for e in range(len(distance_array)):
            cross_array = np.array([])
            cross_amount = 0
            cant_cross_amount = 0
            cant_cross_amount = False
            num_samples_aux = num_samples
            for i in range(num_samples_aux):
                if aux_array[i] != 1:
                    dist_to_collision = -np.log(1 - aux_array[i]) / tt_cross_section
                else:
                    while aux_array[i] == 1:
                        aux_array[i] = round(np.random.rand(), 3)
                    dist_to_collision = -np.log(1 - aux_array[i]) / tt_cross_section
                # print("dist to collision", dist_to_collision)
                if cant_cross_amount != False:
                    if dist_to_collision < distance_array[e] :
                        cant_cross_amount += 1
                        cross_array = np.append(
                            cross_array, 0.000
                        )

                        num_samples_aux = num_samples_aux - 1

                    else:
                        cross_amount += 1
                        cross_array = np.append(cross_array, aux_array[i])

                        num_samples_aux = num_samples_aux - 1

                else:
                    if dist_to_collision < distance_array[e] :
                        cant_cross_amount = 1
                        cross_amount = 0
                        cross_array = np.append(cross_array, 0.000)
                        num_samples_aux = num_samples_aux - 1

                    else:
                        cross_amount = 1
                        cross_array = np.append(cross_array, aux_array[i])
                        cant_cross_amount = 0
                        num_samples_aux = num_samples_aux - 1

            # discretizations = discretizations - 1
            cross_amount_array = np.append(cross_amount_array, cross_amount)
            aux_array = cross_array
            non_zero_indices = aux_array != 0
            new_random_values = np.random.rand(non_zero_indices.sum()).round(3)
            aux_array[non_zero_indices] = new_random_values
            # print("discretization:  ", discretizations)
            # print("aux_array", aux_array)
            

        return cross_amount_array


micro_scattering_U235 = 15.04 * 10 ** (-24)
micro_scattering_U238 = 9.360 * 10 ** (-24)
micro_scattering_O = 3.780 * 10 ** (-24)

macro_scattering_U235 = micro_scattering_U235 * n_U235
macro_scattering_U238 = micro_scattering_U238 * n_U238
macro_scattering_O = micro_scattering_O * n_O

macro_cs_UO2_scattering = (macro_scattering_U235 + macro_scattering_U238 +
                           macro_scattering_O)*(tt_vol_UO2) / tt_act_core_vol

macro_cs_UO2_absorption = macro_cs_gamma_fuel + macro_cs_fission


macro_tt_UO2 = macro_cs_UO2_scattering + macro_cs_UO2_absorption

# print("macro tt cross section", macro_tt_UO2)


macro_cs_Fe_absorption = macro_gamma_Fe
macro_tt_Fe = macro_cs_Fe_absorption + macro_scattering_Fe


initial_neutrons = int(input("Choose initial number of neutrons:    "))
distance = int(input("Distance:     "))


distance_array = np.array([])
for i in range(distance):
    distance_array = np.append(distance_array, i+1)

aux = One_d_one_material(
    initial_neutrons, distance_array, macro_tt_UO2)
cross_amount_array = aux.n_neutrons_cross(
    initial_neutrons, distance_array, macro_tt_UO2)
print("amount that crosses:       ", cross_amount_array)

aux = 1

cross_df = pd.DataFrame({'Distance': distance_array, 'CrossAmount': cross_amount_array, 'Index': aux})


# Criar um heatmap
heatmap_data = cross_df.pivot( index = 'Index', columns='Distance', values='CrossAmount')
sns.heatmap(heatmap_data, cmap='viridis', annot=True, fmt='.1f', cbar_kws={'label': 'Cross Amount'})
plt.xlabel('Distance')
plt.ylabel('Sample')
plt.title('Neutron Cross Amount Heatmap')
plt.show()

# strange value https://www.dgtresearch.com/diffusion-coefficients/
# https://www.nuclear-power.com/nuclear-power/reactor-physics/neutron-diffusion-theory/neutron-current-density/
# Não há uma regra específica da comunidade científica para arredondamento de nêutrons além do arredondamento para o número inteiro mais próximo.
