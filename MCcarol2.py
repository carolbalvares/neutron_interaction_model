import numpy as np
import matplotlib.pyplot as plt

class Material:
    def __init__(self, components):
        # components is a dict with nuclide names as keys and (abundance, cross_section_data) as values
        self.components = components

    def get_effective_cross_section(self, reaction_type, energy):
        # Calculate the effective cross section for a given reaction and energy
        total_cross_section = 0
        for nuclide, (abundance, cross_sections) in self.components.items():
            cs = interpolate_cross_section(cross_sections, energy)
            total_cross_section += abundance * cs
        return total_cross_section

def interpolate_cross_section(cross_sections, energy):
    # Interpolate to find the cross section at the given energy
    # Here, we pick the closest energy point for simplicity
    closest_energy, closest_cs = min(cross_sections, key=lambda x: abs(x[0] - energy))
    return closest_cs

class Neutron:
    def __init__(self, position, energy):
        self.position = np.array(position, dtype=float)
        self.energy = energy
        self.alive = True

    def move(self):
        step = np.random.rand(2) - 0.5
        self.position += step

def read_cross_sections(file_path):
    materials = {}
    current_reaction = ""
    with open(file_path, 'r') as file:
        for line in file:
            if '#REACTION' in line:
                # Creating a key that matches how we will access it later
                current_reaction = line.strip().split('#REACTION')[1].strip()
                # Standardizing the key format to avoid mismatches
                current_reaction_key = ' '.join(current_reaction.split())
                materials[current_reaction_key] = []
            else:
                parts = line.strip().split()
                if len(parts) == 2:
                    energy, cross_section = map(float, parts)
                    materials[current_reaction_key].append((energy, cross_section))
    return materials

def simulate_neutron(neutron, material, counters):
    while neutron.alive:
        neutron.move()
        x, y = neutron.position
        if x < 0 or x >= counters.shape[0] or y < 0 or y >= counters.shape[1]:
            neutron.alive = False
        else:
            cell_x, cell_y = int(x), int(y)
            counters[cell_y, cell_x] += 1
            cs = material.get_effective_cross_section("N,EL", neutron.energy)  # Example reaction type
            if np.random.rand() < cs:  # Simplified interaction logic
                neutron.alive = False

def plot_neutron_counters(counters):
    plt.figure(figsize=(8, 8))
    plt.imshow(counters, cmap='viridis')
    plt.colorbar()
    plt.title('Neutron Count in Each Cell')
    plt.show()

def main():
    num_neutrons = int(input("Enter the number of neutrons to simulate: "))
    size = int(input("Enter the size of the geometry matrix (n for an nxn matrix): "))
    
    # Input for the neutron source location and size
    source_x = int(input("Enter the x-coordinate of the top-left corner of the neutron source: "))
    source_y = int(input("Enter the y-coordinate of the top-left corner of the neutron source: "))
    source_width = int(input("Enter the width of the neutron source: "))
    source_height = int(input("Enter the height of the neutron source: "))

    cross_sections = read_cross_sections("cross_sections")

    material_composition = {
        'U-235': (0.03, cross_sections['U-235(N,EL)U-235-L0']),
        'U-238': (0.97, cross_sections['U-238(N,EL)U-238-L0']),
        'O-16': (2.0 * 0.97, cross_sections['O-16(N,EL)O-16-L0']),
        'H-1': (2.0, cross_sections['H-1(N,G)H-2']),
    }

    enriched_uo2_h2o = Material(material_composition)
    counters = np.zeros((size, size), dtype=int)

    for _ in range(num_neutrons):
        # Initialize neutrons within the source area
        x_position = np.random.randint(source_x, source_x + source_width)
        y_position = np.random.randint(source_y, source_y + source_height)
        neutron_position = [x_position, y_position]
        neutron_energy = 0.0253  # Example: thermal neutron energy
        neutron = Neutron(neutron_position, neutron_energy)
        simulate_neutron(neutron, enriched_uo2_h2o, counters)

    plot_neutron_counters(counters)

if __name__ == "__main__":
    main()

