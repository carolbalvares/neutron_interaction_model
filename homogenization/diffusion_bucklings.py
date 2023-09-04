import numpy as np
import sys
sys.path.append('../')  # Adjust the path as needed
from parameters import *
from hmg_scattering import macro_cs_scattering
from hmg_fission import macro_cs_fission
from hmg_absorption import macro_cs_absorption
from scipy.special import jn



# core homogenization

# given data
r_o = active_core_diameter/2
z_o = general_height

#diffusion
mi_d = 2/(3*18) #18 = Water molecular mass
avg_free_path_transp = 1 / (macro_cs_scattering*(1-mi_d))
dif_coef = avg_free_path_transp / 3

dif_lenght = dif_coef / macro_cs_absorption


#buckling
radial_buckling = (2.405/r_o)**2  # where r_o is the active core radius 
buckling = radial_buckling + (np.pi/z_o)**2


#flow
z = 8.9  # The argument of the Bessel function
j_0 = jn(0, z)  # Calculate J_0(x)  Bessel Function
power =  1000*(10**6) # MWt (335 MWe)
radius_array  = np.arange(-np.pi, 0.1, 0.1) #arrange excludes the last element
height_array = np.arange(-np.pi, 0.1, 0.1)
e_r = 200.7

print (height_array)
aux = 3.63 * power / (tt_act_core_vol * e_r * macro_cs_fission) #e_r = the average recoverable energy per fission (MeV / fission)  U235 = 200,7

flow = aux * j_0 * (2.405*radius_array/r_o)*np.cos(np.pi*height_array/z_o)  #height e igual a z?
