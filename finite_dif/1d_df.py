import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

size = 100  # Tamanho do espaço unidimensional
total_neutrons = 10000  # Número total de nêutrons
source_size = 10  # Tamanho da fonte de nêutrons

# Dicionário de seções de choque
sigma = {
    "H1_n_el": 30.0683,
    "O16_n_el": 3.91335,
    "H1_n_g": 0.332587,
    "U235_n_el": 14.0979,
    "U238_n_el": 9.23954,
    "U235_n_g": 99.4178,
    "U238_n_g": 2.68282,
    "U235_n_f": 586.691,
    "U238_n_f": 1.85034E-05,
}

# Calculando probabilidades
prob = {k: v / sum(sigma.values()) for k, v in sigma.items()}

# Mapa de nêutrons inicial
neutron_map = np.zeros(size)

# Mapa de materiais
material_map = np.full(size, "water")
center = size // 2
source_start = center - source_size // 2
source_end = source_start + source_size
material_map[source_start:source_end] = "fuel"
neutron_map[source_start:source_end] = total_neutrons / source_size

# Simulação de nêutrons
for step in range(100):
    new_map = np.zeros_like(neutron_map)
    for i in range(size):
        neutrons = neutron_map[i]
        if neutrons > 0:
            for reaction, p in prob.items():
                if ("fuel" in reaction and material_map[i] == "fuel") or \
                   ("water" in material_map[i] and ("H1" in reaction or "O16" in reaction)):
                    absorbed = neutrons * p
                    new_map[i] -= absorbed

    # Gaussian smoothing para simular a difusão
    neutron_map = gaussian_filter(new_map + neutron_map, sigma=1)

# Visualização como "heatmap" horizontal
plt.figure(figsize=(10, 2))
heatmap = plt.imshow([neutron_map], aspect='auto', cmap='hot', interpolation='nearest')
plt.colorbar(heatmap, label='Neutron Density')
plt.yticks([])
plt.xlabel('Position (cm)')
plt.title('Neutron Distribution in a 1D Line as Heatmap')
plt.show()
