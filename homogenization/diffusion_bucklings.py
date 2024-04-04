import numpy as np
import sys
sys.path.append('../')  # Adjust the path as needed
from parameters import *
from hmg_scattering import macro_cs_scattering
from hmg_absorption import macro_cs_absorption
from hmg_fission import macro_cs_fission

# core homogenization

# given data
r_o = active_core_diameter/2
z_o = general_height
tt_nt_yield = 2.4355

#diffusion
mi_d = 2/(3*18) #18 = Water molecular mass
avg_free_path_transp = 1 / (macro_cs_scattering*(1-mi_d))
dif_coef = avg_free_path_transp / 3
# print("dif", dif_coef)
dif_lenght = dif_coef / macro_cs_absorption
# print("difll",dif_lenght)

#buckling  
radial_buckling = (2.405/r_o)**2  # where r_o is the active core radius 
geo_buckling = (2.405/r_o)**2 + (np.pi/z_o)**2
mat_buckling = (tt_nt_yield * macro_cs_fission - macro_cs_absorption)/dif_coef  # tt_nt_yield =  Total-neutron Yield
#####tt_nt_yield so paraa U235?
####consertar malha quadrada

#https://www-nds.iaea.org/sgnucdat/a6.htm