import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import random

sys.path.append("../")
from homogenization.cross_sections import *
from parameters import *

class Probability:
    def __init__(self, num_samples, tt_cross_section, row, column):
        self.num_samples = num_samples
        self.tt_cross_section = tt_cross_section
        self.row = row
        self.column = column

    def probab(self,num_samples, tt_cross_section, row, column ):
        self.num_samples = num_samples
        self.tt_cross_section = tt_cross_section
        self.row = row
        self.column = column
        r_array = np.random.rand(self.num_samples).round(3)
        prob_matrix = np.zeros((self.row, self.column))

        prob_matrix = np.zeros((row, column))

        i = 0
        while i < len(r_array):
            r = 0
            while r < row:
                c = 0
                while c < column:
                    if i < len(r_array):
                        if r_array[i] != 1:
                            dist_to_collision = (
                                -np.log(1 - r_array[i]) / tt_cross_section
                            )
                            prob_matrix[r][c] = round(dist_to_collision, 4)
                        else:
                            while i < len(r_array) and r_array[i] == 1:
                                r_array[i] = round(np.random.rand(), 3)
                                i += 1
                                if i < len(r_array):
                                    dist_to_collision = (
                                        -np.log(1 - r_array[i]) / tt_cross_section
                                    )
                                    prob_matrix[r][c] = round(dist_to_collision, 4)
                    i += 1
                    c += 1
                r += 1
        print("prob matriz", prob_matrix)
        return prob_matrix

def create_distance_matrix(row, column):
    center_x, center_y = (row // 2, column // 2)
    distance_matrix = np.zeros((row, column))
    for i in range(row):
        for j in range(column):
            distance = np.sqrt((center_x - i) ** 2 + (center_y - j) ** 2)
            distance_matrix[i, j] = distance
    print("DISTANCE MATRIZ", distance_matrix)
    return distance_matrix

def initialize_grid(grid_size, fuel_size):
    grid = np.zeros((grid_size, grid_size), dtype=int)
    start = (grid_size - fuel_size) // 2
    end = start + fuel_size
    grid[start:end, start:end] = 1
    return grid

def initialize_interaction_probabilities(grid_size, num_samples, tt_cross_section, row, column):
    prob_aux = Probability(num_samples, tt_cross_section, row, column)
    probs = prob_aux.probab(num_samples, tt_cross_section, row, column)
    return probs.reshape(grid_size, grid_size)

def simulate_neutrons(grid, start_position, num_particles, interaction_probs, distance_matrix):
    grid_size = len(grid)
    neutron_count_grid = np.zeros_like(grid)
    interaction_positions = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for _ in range(num_particles):
        x, y = start_position
        while 0 <= x < grid_size and 0 <= y < grid_size:
            neutron_count_grid[x, y] += 1
            if (x, y) != start_position and distance_matrix[x, y] < interaction_probs[x, y]:
                interaction_positions.append((x, y))
                break
            dx, dy = random.choice(directions)
            x, y = x + dx, y + dy
    return neutron_count_grid, interaction_positions

def plot_grid(neutron_count_grid):
    plt.figure(figsize=(10, 8))
    plt.imshow(neutron_count_grid, cmap='viridis', interpolation='nearest')
    plt.colorbar(label='Neutron Count')
    plt.title('Neutron Transport Simulation')
    plt.show()

def main():
    grid_size = 5
    fuel_size = 1
    num_particles = 100000
    row, column = 5, 5
    start_position = (grid_size // 2, grid_size // 2)


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

    grid = initialize_grid(grid_size, fuel_size)
    probs = initialize_interaction_probabilities(grid_size, num_particles, macro_tt_UO2, row, column)
    distance_matrix = create_distance_matrix(row, column)
    neutron_count_grid, interaction_positions = simulate_neutrons(grid, start_position, num_particles, probs, distance_matrix)
    
    plot_grid(neutron_count_grid)
    if interaction_positions:
        print(f"Primeira interação ocorreu na posição: {interaction_positions[0]}")
    else:
        print("Nenhuma interação ocorreu.")

if __name__ == "__main__":
    main()
