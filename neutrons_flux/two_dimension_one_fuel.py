import sys
import numpy as np
import matplotlib.pyplot as plt
import random

class Probability:
    def __init__(self, num_samples, tt_cross_section, row, column):
        self.num_samples = num_samples
        self.tt_cross_section = tt_cross_section
        self.row = row
        self.column = column

    def calculate_probabilities(self):
        r_array = np.random.rand(self.num_samples).round(3)
        prob_matrix = np.zeros((self.row, self.column))

        i = 0
        while i < len(r_array):
            for r in range(self.row):
                for c in range(self.column):
                    if i < len(r_array):
                        if r_array[i] != 1:
                            dist_to_collision = -np.log(1 - r_array[i]) / self.tt_cross_section
                            prob_matrix[r][c] = round(dist_to_collision, 4)
                        else:
                            while i < len(r_array) and r_array[i] == 1:
                                r_array[i] = round(np.random.rand(), 3)
                                i += 1
                                if i < len(r_array):
                                    dist_to_collision = -np.log(1 - r_array[i]) / self.tt_cross_section
                                    prob_matrix[r][c] = round(dist_to_collision, 4)
                    i += 1
        print("prob_matrix", prob_matrix)
        return prob_matrix

def create_distance_matrix(row, column):
    center_x, center_y = (row // 2, column // 2)
    distance_matrix = np.zeros((row, column))
    for i in range(row):
        for j in range(column):
            distance = np.sqrt((center_x - i) ** 2 + (center_y - j) ** 2)
            distance_matrix[i, j] = distance
    return distance_matrix

def initialize_grid(grid_size, fuel_size):
    grid = np.zeros((grid_size, grid_size), dtype=int)
    start = (grid_size - fuel_size) // 2
    end = start + fuel_size
    grid[start:end, start:end] = 1
    return grid

def initialize_interaction_probabilities(grid_size, num_samples, tt_cross_section, row, column):
    prob_aux = Probability(num_samples, tt_cross_section, row, column)
    probs = prob_aux.calculate_probabilities()
    print("probs.reshape(grid_size, grid_size)", probs.reshape(grid_size, grid_size))
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
    fuel_size = 1  # Um único combustível no centro
    num_particles = 50
    row, column = 5, 5
    start_position = (grid_size // 2, grid_size // 2)

    # Inicializando as variáveis antes de usá-las

    # Calculando a seção transversal total
    tt_cross_section =3.25107788

    grid = initialize_grid(grid_size, fuel_size)
    probs = initialize_interaction_probabilities(grid_size, num_particles, tt_cross_section, row, column)
    distance_matrix = create_distance_matrix(row, column)
    neutron_count_grid, interaction_positions = simulate_neutrons(grid, start_position, num_particles, probs, distance_matrix)
    
    plot_grid(neutron_count_grid)
    
    if interaction_positions:
        print(f"Primeira interação ocorreu na posição: {interaction_positions[0]}")
    else:
        print("Nenhuma interação ocorreu.")

if __name__ == "__main__":
    main()
