import sys
sys.path.append('../')  # Adjust the path as needed
from parameters import *
from scipy.special import jn
from hmg_fission import macro_cs_fission

# given data
r_o = active_core_diameter/2
z_o = general_height

z = 8.9  # The argument of the Bessel function
j_0 = jn(0, z)  # Calculate J_0(x)  Bessel Function
power =  1000*(10**6) # MWt (335 MWe)
radius_array  = np.arange(-np.pi, 0.1, 0) #arrange excludes the last element
height_array = np.arange(-np.pi, 0.1, 0)
# print("lenght radius array", len(radius_array))
# print("lenght height array", len(height_array))
e_r = 200.7 #e_r = the average recoverable energy per fission (MeV / fission)  U235 = 200,7

aux = 3.63 * power / (tt_act_core_vol * e_r * macro_cs_fission)

result = [i * j for i in range(3) for j in range(4)]
flow = [0.0]
for r in radius_array:
    for h in height_array:
        aux =  aux * j_0 * (2.405*r/r_o)*np.cos(np.pi*h/z_o)
        flow = np.append(flow, aux)



#fatorial ou multiplicação?
# print(len(flow))
# flow = aux * j_0 * (2.405*radius_array/r_o)*np.cos(np.pi*height_array/z_o)  #height e igual a z?