from hmg_fission import macro_cs_fission
from scipy.special import jn
from parameters import *
import sys
sys.path.append('../')  # Adjust the path as needed
import pandas as pd
import matplotlib.pyplot as plt


from mpl_toolkits import mplot3d



# given data
r_o = active_core_diameter/2
z_o = general_height

def pos(j_0):
    return [x for x in j_0 if x > 0] 


def matrix_flow(flow, index):
    matriz = []
    for i in range(0, len(flow), index):
        sublista = flow[i:i+index]
        matriz.append(sublista)
    return matriz

auxiliar = 2.405/r_o
radius_array = np.arange(-0.5*np.pi, 0.5*np.pi, 0.1)
j_0 = jn(0, auxiliar*radius_array)  # Calculate J_0(x)  Bessel Function

j_positive = pos(j_0)

# e_r = the average recoverable energy per fission (MeV / fission)  U235 = 200,7
e_r = 200.7

aux = 3.63 * power / (tt_act_core_vol * e_r * macro_cs_fission)
height_array = np.arange(-0.5*np.pi, 0.5*np.pi, 0.1)

data = {}


flow = np.empty((len(radius_array), len(height_array)))

for i, h in enumerate(height_array):
    for j, r in enumerate(radius_array):
        auxx = aux * j * np.cos(np.pi * h / z_o)
        flow[i, j] = auxx
        
  
max = np.max(flow)
print(max)


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(radius_array, height_array, flow, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');
ax.view_init(60, 35)
plt.title('Flow in function of radius and height')

plt.show()


# poltar funcao de bessel e de altura de 0 a pi/2
# fcs total = abs + scattering
# ver documento que ele mandou, fazer densidade dos uranios juntos

# data
# https://docs.scipy.org/doc/scipy-1.0.0/reference/generated/scipy.special.jn.html
#https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html