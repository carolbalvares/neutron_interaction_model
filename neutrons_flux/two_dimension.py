import numpy as np
import matplotlib.pyplot as plt
import random

def initialize_grid(grid_size, fuel_size):
    """ Initialize the grid with fuel in the center and water around. """
    grid = np.zeros((grid_size, grid_size), dtype=int)  # water
    start = (grid_size - fuel_size) // 2
    end = start + fuel_size
    grid[start:end, start:end] = 1  # fuel
    return grid

def simulate_neutrons(grid, start_position, num_particles):
    """ Simulate neutrons starting from the center, tracking each square they pass through. """
    grid_size = len(grid)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    neutron_count_grid = np.zeros_like(grid)

    for _ in range(num_particles):
        x, y = start_position
        while 0 <= x < grid_size and 0 <= y < grid_size:
            neutron_count_grid[x, y] += 1  # Count neutron in the current square
            if random.random() < 0.01:  # Assuming a small chance to interact and stop
                break
            dx, dy = random.choice(directions)
            x += dx
            y += dy

    return neutron_count_grid

def plot_grid(neutron_count_grid):
    """ Plot the grid showing neutron distribution as a heatmap. """
    plt.figure(figsize=(10, 8))
    plt.imshow(neutron_count_grid, cmap='viridis', interpolation='nearest')
    plt.colorbar(label='Neutron Count')
    plt.title('Neutron Transport Simulation')
    plt.show()

# Parameters
grid_size = 5  # 12x12 cm grid
fuel_size = 1 # 2x2 cm fuel at the center
num_particles = 100000  # Number of neutrons to simulate
start_position = (grid_size // 2, grid_size // 2)  # Neutron source at the center

# Initialize grid and simulate neutrons
grid = initialize_grid(grid_size, fuel_size)
neutron_count_grid = simulate_neutrons(grid, start_position, num_particles)


print(neutron_count_grid)


# Plot results
plot_grid(neutron_count_grid)
