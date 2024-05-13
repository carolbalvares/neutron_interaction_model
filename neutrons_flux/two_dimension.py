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

    def probab(self, num_samples, tt_cross_section, row, column):
        self.num_samples = num_samples
        self.tt_cross_section = tt_cross_section
        self.row = row
        self.column = column
        
        r_array = np.random.rand(num_samples).round(3)
        # creates one prob_matrix that will be completed, but now it has only zeros
        prob_matrix = np.zeros((len(range(row)), len(range(column))))
        # creates condition using i as aux for while i < len(r_array):
        i = 0
        while i < len(r_array):
            # creates condition using r as aux for while r < len(row):
            r = 0
            while r < len(range(row)):
                # creates condition using c as aux for while c < len(column):
                # using these 3 conditions, we complete every window of our prob_matrix with the probability definied as dist_to_collision
                c = 0
                while c < len(range(column)):
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



        print("prob_matrix", prob_matrix)
        return prob_matrix




def initialize_grid(grid_size, fuel_size):
    """ Initialize the grid with fuel in the center and water around. """
    grid = np.zeros((grid_size, grid_size), dtype=int)  # water
    start = (grid_size - fuel_size) // 2
    end = start + fuel_size
    grid[start:end, start:end] = 1  # fuel
    return grid

def initialize_interaction_probabilities(grid_size, num_samples, tt_cross_section, row, column):
    """ Initialize a grid of interaction probabilities for each cell. """
    prob_aux = Probability(num_samples, tt_cross_section, row, column)
    probs = prob_aux.probab(num_samples, tt_cross_section, row, column)

    # probs = np.array([
    #     0.1 , 0.2, 0.03, 0.01, 0.2,
    #     0.1, 0.022, 0.33, 0.12, 0.21,
    #     0.12, 0.12, 0.12, 0.13, 0.01,
    #     0.11, 0.12, 0.111, 0.12, 0.25,
    #     0.87, 0.56, 0.43, 0.34, 0.23
    # ])
    return probs.reshape(grid_size, grid_size)

def simulate_neutrons(grid, start_position, num_particles, interaction_probs):
    """ Simulate neutrons starting from the center, tracking each square they pass through and capturing interaction events. """
    grid_size = len(grid)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    neutron_count_grid = np.zeros_like(grid)
    interaction_positions = []  # List to store interaction positions

    for _ in range(num_particles):
        x, y = start_position
        while 0 <= x < grid_size and 0 <= y < grid_size:
            neutron_count_grid[x, y] += 1  # Count neutron in the current square
            if random.random() < interaction_probs[x, y]:  # Use position-dependent interaction probability
                interaction_positions.append((x, y))
                break
            dx, dy = random.choice(directions)
            x += dx
            y += dy

    return neutron_count_grid, interaction_positions

def plot_grid(neutron_count_grid):
    """ Plot the grid showing neutron distribution as a heatmap. """
    plt.figure(figsize=(10, 8))
    plt.imshow(neutron_count_grid, cmap='viridis', interpolation='nearest')
    plt.colorbar(label='Neutron Count')
    plt.title('Neutron Transport Simulation')
    plt.show()

# Parameters
grid_size = 5  # 5x5 grid for simplicity, adjust as needed
fuel_size = 1  # 2x2 cm fuel at the center
num_particles = 100000  # Number of neutrons to simulate
row=5
column = 5
start_position = (grid_size // 2, grid_size // 2)  # Neutron source at the center

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

# Initialize grid and interaction probabilities
grid = initialize_grid(grid_size, fuel_size)
interaction_probs =  initialize_interaction_probabilities(grid_size, num_particles, macro_tt_UO2, row, column)

# Simulate neutrons
neutron_count_grid, interaction_positions = simulate_neutrons(grid, start_position, num_particles, interaction_probs)

# Plot results
plot_grid(neutron_count_grid)

# Display interaction positions for verification
if interaction_positions:  # Check if the list is not empty
    first_interaction = interaction_positions[0]
    print(f"Primeira interação ocorreu na posição: {first_interaction}")
else:
    print("Nenhuma interação ocorreu.")
