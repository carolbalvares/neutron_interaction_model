
import sys
sys.path.append('../')
from parameters import *
from homogenization.cross_sections import *
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as numpy


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



macro_cs_UO2_scattering = (
        (macro_scattering_U235 + macro_scattering_U238 + macro_scattering_O)
        * (tt_vol_UO2)
        / tt_act_core_vol
    )

micro_cs_UO2_scattering = macro_cs_UO2_scattering / (6.02214076 * 10 ** (23))

macro_cs_UO2_absorption = macro_cs_gamma + macro_cs_fission

#barns para cm²
macro_tt_UO2 = (macro_cs_UO2_absorption + macro_cs_UO2_scattering) * 10 ** (-24)

initial_neutrons = num_particles
distance = 10


distance_array = np.array([])
for i in range(distance):
    distance_array = np.append(distance_array, i+1)
    print("distance_array", distance_array)

aux = One_d_one_material(
    initial_neutrons, distance_array, macro_tt_UO2)

# Chamada correta do método sem passar argumentos adicionais
cross_amount_array = aux.n_neutrons_cross()
print("amount that crosses:       ", cross_amount_array)


if len(cross_amount_array) % 2 != 0:
    print("O vetor precisa ter um número par de elementos.")
else:
    # Redimensionando o vetor para uma matriz de duas colunas
    cross_amount_array_reshaped = cross_amount_array.reshape(-1, 2)

    # Somando os pares de elementos
    cross_amount_array_sum = np.sum(cross_amount_array_reshaped, axis=1)

aux = 10
cross_df = pd.DataFrame({
        'Distance': range(5),
        'CrossAmount': cross_amount_array_sum,
        'Index': np.ones(5)
    })

print("DataFrame:\n", cross_df)

    # Criando o heatmap
heatmap_data = cross_df.pivot("Index", "Distance", "CrossAmount")
# Criando o heatmap
plt.figure(figsize=(10, 5))
sns.heatmap(heatmap_data, annot=True, cmap='viridis', fmt=".2f")
plt.title('Neutron Cross Amount Heatmap')
plt.xlabel('Distance')
plt.ylabel('Index')
plt.show()

print("Numero de amostras que passa:", cross_amount_array_sum)
# strange value https://www.dgtresearch.com/diffusion-coefficients/
# https://www.nuclear-power.com/nuclear-power/reactor-physics/neutron-diffusion-theory/neutron-current-density/
# Não há uma regra específica da comunidade científica para arredondamento de nêutrons além do arredondamento para o número inteiro mais próximo.
