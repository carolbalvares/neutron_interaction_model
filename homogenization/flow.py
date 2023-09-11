from hmg_fission import macro_cs_fission
from scipy.special import jn
from parameters import *
import sys
sys.path.append('../')  # Adjust the path as needed
import pandas as pd
import matplotlib.pyplot as plt


# given data
r_o = active_core_diameter/2
z_o = general_height

def pos(j_0):
    return [x for x in j_0 if x > 0] 

auxiliar = 2.405/r_o
radius_array = np.arange(-0.5*np.pi, 0.5*np.pi, 0.1)
j_0 = jn(0, auxiliar*radius_array)  # Calculate J_0(x)  Bessel Function

j_positive = pos(j_0)

# e_r = the average recoverable energy per fission (MeV / fission)  U235 = 200,7
e_r = 200.7

aux = 3.63 * power / (tt_act_core_vol * e_r * macro_cs_fission)
height_array = np.arange(-0.5*np.pi, 0.5*np.pi, 0.1)



flow = [0.0]
for h in height_array:
    for j in j_positive:
        auxx = aux * j*np.cos(np.pi*h/z_o)
        flow = np.append(flow, auxx)



plt.plot(flow)
plt.show()

# poltar funcao de bessel e de altura de 0 a pi/2
# fcs total = abs + scattering
# ver documento que ele mandou, fazer densidade dos uranios juntos

# data
# https://docs.scipy.org/doc/scipy-1.0.0/reference/generated/scipy.special.jn.html
