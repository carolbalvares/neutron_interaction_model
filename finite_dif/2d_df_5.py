import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# Parâmetros iniciais
size = 50  # Tamanho da matriz original
cell_size = 10  # Tamanho da célula (não usado diretamente neste script)
total_neutrons = 1000000  # Total de nêutrons inicialmente no combustível
source_size = 10  # Tamanho da fonte de nêutrons no centro

# Dicionário de seções de choque atualizadas
sigma = {
    "H1_n_el": 30.173471,
    "O16_n_el": 3.9152284,
    "H1_n_g": 0.3346708,
    "U235_n_el": 14.110209,
    "U238_n_el": 9.240251,
    "U235_n_g": 100.135796,
    "U238_n_g": 2.7003825,
    "U235_n_f": 590.64465,
    "U238_n_f": 1.85034E-05,
}

# Probabilidade de cada reação
prob = {k: v / sum(sigma.values()) for k, v in sigma.items()}

# Inicialização da matriz de nêutrons
neutron_map = np.zeros((size, size))

# Configuração da matriz de materiais
material_map = np.full((size, size), "water")
center = size // 2
source_start = center - source_size // 2
source_end = source_start + source_size
material_map[source_start:source_end, source_start:source_end] = "fuel"
neutron_map[source_start:source_end, source_start:source_end] = total_neutrons / (source_size ** 2)

# Simulação de absorção e dispersão de nêutrons
for step in range(100):
    new_map = np.copy(neutron_map)
    for i in range(size):
        for j in range(size):
            neutrons = neutron_map[i, j]
            if neutrons > 0:
                absorbed_total = 0
                for reaction, p in prob.items():
                    if ("fuel" in reaction and material_map[i, j] == "fuel") or \
                       ("water" in material_map[i, j] and ("H1" in reaction or "O16" in reaction)):
                        absorbed = neutrons * p
                        absorbed_total += absorbed
                new_map[i, j] -= absorbed_total
    neutron_map = gaussian_filter(new_map, sigma=1)

# Redução da matriz de nêutrons para uma matriz 5x5
final_size = 5
neutron_map_ = np.zeros((final_size, final_size))
stride = 10  # Calculando um stride para cobrir toda a matriz

for i in range(final_size):
    for j in range(final_size):
        start_i = i * stride
        start_j = j * stride
        end_i = start_i + stride
        end_j = start_j + stride
        # Garante que não ultrapasse os limites da matriz
        end_i = min(end_i, size)
        end_j = min(end_j, size)
        neutron_map_[i, j] = np.sum(neutron_map[start_i:end_i, start_j:end_j])



neutron_map_ = neutron_map_.astype(int)

print("neutron_map_", neutron_map_)

# Visualização da matriz final
plt.figure(figsize=(8, 6))
plt.imshow(neutron_map_, interpolation='none', cmap='hot')
plt.colorbar(label='Neutron Density')
plt.title('Reduced Neutron Distribution in 10x10 cm Grid')
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.grid(True)
plt.show()
