from homogenization.hmg_fission import macro_cs_fission
from scipy.special import jn
from parameters import *
import sys
sys.path.append('../')  # Adjust the path as needed
import matplotlib.pyplot as plt


# from mpl_toolkits import mplot3d



# given data
r_o = active_core_diameter/2
z_o = general_height

def pos(j_0):
    return [x for x in j_0 if x > 0] 


def matrix_flux(flux, index):
    matriz = []
    for i in range(0, len(flux), index):
        sublista = flux[i:i+index]
        matriz.append(sublista)
    return matriz

auxiliar = 2.405/r_o
radius_array = np.arange(0.5*-np.pi, 0.5*np.pi, 0.1)
radius_array_polar = []
for r in radius_array:
    radius_array_polar = np.append(radius_array_polar, r_o*np.cos(r))
j_0 = jn(0, auxiliar*radius_array_polar)  # Calculate J_0(x)  Bessel Function

j_positive = pos(j_0)

# e_r = the average recoverable energy per fission (MeV / fission)  U235 = 200,7
e_r = 200.7

aux = 3.63 * power / (tt_act_core_vol * e_r * macro_cs_fission)
height_array = np.arange(0.5*-np.pi,0.5* np.pi, 0.1)
height_array_polar = []
for h in radius_array:
    height_array_polar = np.append(height_array_polar, z_o*np.sin(h))


flux = np.empty((len(radius_array_polar), len(height_array)))

for i, h in enumerate(height_array):
    for j, r in enumerate(radius_array_polar):
        auxx = aux * r * np.cos(np.pi * h / z_o)
        flux[i, j] = auxx
        
  
max = np.max(flux)
print(np.cos(np.pi * h / z_o))


fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(radius_array, height_array, flux, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');
ax.view_init(60, 35)
plt.title('flux in function of radius and height')

plt.show()


# data
# https://docs.scipy.org/doc/scipy-1.0.0/reference/generated/scipy.special.jn.html
#https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html
