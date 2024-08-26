import openmc
import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET
import os
import urllib.request

# Definição dos materiais
fuel = openmc.Material(name="fuel")
fuel.add_nuclide("U235", 1.0)
fuel.set_density("g/cm3", 10.5)

water = openmc.Material(name="water")
water.add_nuclide("H1", 2.0)
water.add_nuclide("O16", 1.0)
water.set_density("g/cm3", 1.0)

materials = openmc.Materials([fuel, water])
materials.export_to_xml()

# Definição dos planos para o combustível 1 e 2
surf_fuel1_xmin = openmc.XPlane(x0=-25)
surf_fuel1_xmax = openmc.XPlane(x0=-15)
surf_fuel1_ymin = openmc.YPlane(y0=-5)
surf_fuel1_ymax = openmc.YPlane(y0=5)
surf_fuel1_zmin = openmc.ZPlane(z0=-5)
surf_fuel1_zmax = openmc.ZPlane(z0=5)

surf_fuel2_xmin = openmc.XPlane(x0=15)
surf_fuel2_xmax = openmc.XPlane(x0=25)
surf_fuel2_ymin = openmc.YPlane(y0=-5)
surf_fuel2_ymax = openmc.YPlane(y0=5)
surf_fuel2_zmin = openmc.ZPlane(z0=-5)
surf_fuel2_zmax = openmc.ZPlane(z0=5)

# Definição das células de combustível 1 e 2
cell_fuel_1 = openmc.Cell(
    region=+surf_fuel1_xmin & -surf_fuel1_xmax & +surf_fuel1_ymin & -surf_fuel1_ymax & +surf_fuel1_zmin & -surf_fuel1_zmax,
    fill=fuel,
    name="Fuel Cell 1"
)

cell_fuel_2 = openmc.Cell(
    region=+surf_fuel2_xmin & -surf_fuel2_xmax & +surf_fuel2_ymin & -surf_fuel2_ymax & +surf_fuel2_zmin & -surf_fuel2_zmax,
    fill=fuel,
    name="Fuel Cell 2"
)

# Definição correta da célula de água ao redor das duas células de combustível
surf_water_xmin = openmc.XPlane(x0=-30, boundary_type="vacuum")
surf_water_xmax = openmc.XPlane(x0=30, boundary_type="vacuum")
surf_water_ymin = openmc.YPlane(y0=-30, boundary_type="vacuum")
surf_water_ymax = openmc.YPlane(y0=30, boundary_type="vacuum")
surf_water_zmin = openmc.ZPlane(z0=-30, boundary_type="vacuum")
surf_water_zmax = openmc.ZPlane(z0=30, boundary_type="vacuum")

cell_water = openmc.Cell(
    region=(
        +surf_water_xmin & -surf_water_xmax & +surf_water_ymin & -surf_water_ymax & +surf_water_zmin & -surf_water_zmax
    ) & ~cell_fuel_1.region & ~cell_fuel_2.region,  # Excluindo as regiões das células de combustível
    fill=water,
    name="Water Surrounding Fuel Cells"
)

# Definição do universo e geometria
fuel_universe = openmc.Universe(cells=[cell_fuel_1, cell_fuel_2, cell_water])

geometry = openmc.Geometry()
geometry.root_universe = fuel_universe
geometry.export_to_xml()

# Definição das configurações
settings = openmc.Settings()
source1 = openmc.Source()
source1.space = openmc.stats.Point(xyz=(-20, 0, 0))  # Fonte no meio da célula 1
source1.angle = openmc.stats.Isotropic()
source1.energy = openmc.stats.Discrete([0.025], [1.0])

source2 = openmc.Source()
source2.space = openmc.stats.Point(xyz=(20, 0, 0))  # Fonte no meio da célula 2
source2.angle = openmc.stats.Isotropic()
source2.energy = openmc.stats.Discrete([0.025], [1.0])

settings.particles = 100000
settings.sources = [source1, source2]
settings.batches = 100
settings.inactive = 40
settings.export_to_xml()

# Definição da malha e do tally para calcular o fluxo
mesh = openmc.RegularMesh()
mesh.dimension = [6, 6, 1]
mesh.lower_left = [-30, -30, -0.5]
mesh.upper_right = [30, 30, 0.5]

mesh_filter = openmc.MeshFilter(mesh)
tally = openmc.Tally(name="flux_tally")
tally.filters = [mesh_filter]
tally.scores = ["flux"]
tallies = openmc.Tallies([tally])
tallies.export_to_xml()

# Execução da simulação
openmc.run()

# Carregamento dos resultados e análise
sp = openmc.StatePoint("statepoint.100.h5")
flux_tally = sp.get_tally(name="flux_tally")
df = flux_tally.get_pandas_dataframe()
print(df)

n_neutrons_flux = df["mean"] * settings.particles
print("Neutron Flux Data Frame:")
print(pd.DataFrame({'Neutron_Flux': n_neutrons_flux}))

# Salvando os dados de fluxo em um arquivo Excel
nome_arquivo = "matriz_excel_openmc.xlsx"
n_neutrons_flux.to_excel(nome_arquivo, index=False)
