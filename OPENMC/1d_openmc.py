import openmc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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

# Definição da geometria
# Planos genéricos de limitação em y e z
surf_bottom_y = openmc.YPlane(y0=-5, boundary_type='vacuum')
surf_top_y    = openmc.YPlane(y0=5 , boundary_type='vacuum')
surf_bottom_z = openmc.ZPlane(z0=-5, boundary_type='vacuum')
surf_top_z    = openmc.ZPlane(z0=5 , boundary_type='vacuum')
# Definição das superfícies do combustível para a propagação unidirecional
surf_fuel_xmin = openmc.XPlane(x0=-25, boundary_type='vacuum')
surf_fuel_xmax = openmc.XPlane(x0=-15)
#surf_fuel_ymin = openmc.YPlane(y0=-5)
#surf_fuel_ymax = openmc.YPlane(y0=5)
#surf_fuel_zmin = openmc.ZPlane(z0=-5)
#surf_fuel_zmax = openmc.ZPlane(z0=5)

# Redefinição das superfícies de água para garantir a correta configuração
surf_water_xmin = openmc.XPlane(x0=-15)
surf_water_xmax = openmc.XPlane(x0=25, boundary_type="vacuum")
#surf_water_ymin = openmc.YPlane(y0=-5, boundary_type="vacuum")
#surf_water_ymax = openmc.YPlane(y0=5, boundary_type="vacuum")
#surf_water_zmin = openmc.ZPlane(z0=-5, boundary_type="vacuum")
#surf_water_zmax = openmc.ZPlane(z0=5, boundary_type="vacuum")

# Definição da célula de combustível
cell_fuel = openmc.Cell(
    region=+surf_fuel_xmin & -surf_fuel_xmax & +surf_bottom_y & -surf_top_y & +surf_bottom_z & -surf_top_z,
    fill=fuel,
    name="Fuel Cell"
)


cell_water = openmc.Cell(
    region=(
        +surf_water_xmin & -surf_water_xmax & +surf_bottom_y & -surf_top_y & +surf_bottom_z & -surf_top_z
    ) & ~cell_fuel.region,
    fill=water,
    name="Water Surrounding Fuel"
)

fuel_universe = openmc.Universe(cells=[cell_fuel, cell_water])

geometry = openmc.Geometry()
geometry.root_universe = fuel_universe
geometry.export_to_xml()

# Definição das configurações
settings = openmc.Settings()


energy_distribution = openmc.stats.Discrete([0.000000025], [1.0])

# Define a distribuição angular para orientar as partículas ao longo do eixo x positivo
angle_distribution = openmc.stats.Monodirectional()
angle_distribution.reference_uvw = [1.0, 0.0, 0.0]  # Direção ao longo do eixo x positivo

# Configura a fonte
settings.source = openmc.Source(
    space=openmc.stats.Point(xyz=(-20.0, 0.0, 0.0)),  # Posicionamento da fonte
    angle=angle_distribution,
    energy=energy_distribution
)



# source.angle = openmc.stats.MonoDirectional(openmc.stats.Discrete([1], [1]))  # Direção para o eixo x positivo
settings.particles = 100000
settings.batches = 100
settings.inactive = 40
settings.export_to_xml()

# Definição da malha e do tally para calcular o fluxo
mesh = openmc.RegularMesh()
mesh.dimension = [5, 1, 1]
mesh.lower_left = [-25, -0.5, -0.5]
mesh.upper_right = [25, 0.5, 0.5]

mesh_filter = openmc.MeshFilter(mesh)
tally = openmc.Tally(name="flux_tally")
tally.filters = [mesh_filter]
tally.scores = ["flux"]
tallies = openmc.Tallies([tally])
tallies.export_to_xml()

# Configuração de um objeto de plotagem
plot = openmc.Plot()
plot.filename = 'plot'
plot.origin = [-20, 0, 0]  # Centro do plot
plot.width = [100, 100]  # Largura do plot em unidades de cm
plot.pixels = [400, 400]  # Resolução da imagem
plot.color_by = 'material'  # Colorir por material

# Exportar configuração de plotagem
plots = openmc.Plots([plot])
plots.export_to_xml()

# Executar o comando de plotagem
openmc.plot_geometry()  
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




