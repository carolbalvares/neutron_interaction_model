import sys
sys.path.append('../')
from parameters import *
from homogenization.cross_sections import *
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

    def n_neutrons_cross(self):
        cross_amount_array = np.array([])
        # Gera amostras aleatórias apenas uma vez para todos os nêutrons
        r_samples_array = np.random.rand(self.num_samples)
        distances_to_collision = -np.log(1 - r_samples_array) / self.tt_cross_section

        # Itera sobre cada distância especificada
        for distance in self.distance_array:
            # Conta quantos nêutrons conseguem atravessar essa distância
            cross_amount = np.sum(distances_to_collision >= distance)
            cross_amount_array = np.append(cross_amount_array, cross_amount)

        return cross_amount_array


num_particles = 100000



macro_scattering_U235 = micro_scattering_U235 * n_U235
macro_scattering_U238 = micro_scattering_U238 * n_U238
macro_scattering_O = micro_scattering_O * n_O

macro_cs_UO2_scattering = (
        (macro_scattering_U235 + macro_scattering_U238 + macro_scattering_O)
        * (tt_vol_UO2)
        / tt_act_core_vol
    )

micro_cs_UO2_scattering = macro_cs_UO2_scattering / (6.02214076 * 10 ** (23))

macro_cs_UO2_absorption = macro_cs_gamma + macro_cs_fission

macro_tt_UO2 = (macro_cs_UO2_absorption + macro_cs_UO2_scattering) * 10 ** (-23)


print("macro_tt_UO2", macro_tt_UO2)

initial_neutrons = num_particles
distance = 10

mesh = 5


    
     
distance_array = np.array([])
for i in range(distance):
    distance_array = np.append(distance_array, i+1)

aux = One_d_one_material(
    initial_neutrons, distance_array, macro_tt_UO2)

# Chamada correta do método sem passar argumentos adicionais
cross_amount_array = aux.n_neutrons_cross()
print("amount that crosses:       ", cross_amount_array)



aggregated_cross_amount = [0, 0, 0, 0, 0]

for i in range(0, len(cross_amount_array), 5):
    sum_cross = np.sum(cross_amount_array[i:i+5])
    group_index = i // 5
    aggregated_cross_amount[group_index] = sum_cross

mesh_array = [1, 2, 3, 4, 5]

cross_df = pd.DataFrame({
    'Distance': mesh_array,
    'CrossAmount': aggregated_cross_amount
})

cross_df['CrossAmount'] = cross_df['CrossAmount'].round().astype(int)
cross_df['Distance'] = cross_df['Distance'].round().astype(int)
new_df = pd.DataFrame(cross_df['CrossAmount'].values.reshape(1, -1), 
                      index=[1], 
                      columns=cross_df['Distance'])

# Criando o heatmap
plt.figure(figsize=(8, 4))
sns.heatmap(new_df, cmap='viridis', annot=True, fmt='d')
plt.xlabel('Distance')
plt.ylabel('Constant Index (1)')
plt.title('Neutron Cross Amount Heatmap')
plt.show()






# strange value https://www.dgtresearch.com/diffusion-coefficients/
# https://www.nuclear-power.com/nuclear-power/reactor-physics/neutron-diffusion-theory/neutron-current-density/
# Não há uma regra específica da comunidade científica para arredondamento de nêutrons além do arredondamento para o número inteiro mais próximo.
