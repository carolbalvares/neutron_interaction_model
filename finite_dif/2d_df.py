import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

size = 10  
cell_size = 1  
total_neutrons = 100000  
source_size = 3  

# Dicionário de seções de choque atualizadas
sigma = {
    "H1_n_el": 30.173471,
    "O16_n_el": 3.9152284,
    "H1_n_g": 0.3346708,
    "U235_n_el": 14.110209,
    "U238_n_el": 9.240251,
    "U235_n_g": 100.135796,
    "U238_n_g": 2.7003825,
    "U235_n_f":  590.64465,
    "U238_n_f": 1.85034E-05,
}

prob = {k: v / sum(sigma.values()) for k, v in sigma.items()}

neutron_map = np.zeros((size, size))

material_map = np.full((size, size), "water")
center = size // 2
source_start = center - source_size // 2
source_end = source_start + source_size
material_map[source_start:source_end, source_start:source_end] = "fuel"
neutron_map[source_start:source_end, source_start:source_end] = total_neutrons / (source_size**2)

for step in range(100):
    new_map = np.zeros_like(neutron_map)
    for i in range(size):
        for j in range(size):
            neutrons = neutron_map[i, j]
            if neutrons > 0:
                for reaction, p in prob.items():
                    if ("fuel" in reaction and material_map[i, j] == "fuel") or \
                       ("water" in material_map[i, j] and ("H1" in reaction or "O16" in reaction)):
                        absorbed = neutrons * p
                        new_map[i, j] -= absorbed

    # Gaussian smoothing to simulate diffusion
    neutron_map = gaussian_filter(new_map + neutron_map, sigma=1)

plt.figure(figsize=(8, 6))
plt.imshow(neutron_map, interpolation='bilinear', cmap='hot')
plt.colorbar(label='Neutron Density')
plt.title('Final Neutron Distribution in 10x10 cm Grid')
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.grid(True) 
plt.show()
