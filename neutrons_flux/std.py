import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



row1_python = np.array([ 11758 , 23554,  31080,  23261 , 11653 ])
row2_python = np.array( [ 23193,  50619 , 77453,  50230,  23195 ])
row3_python = np.array(  [  30994,  77276, 176874 , 76907 , 30932])
row4_python = np.array([23243 , 50009,  76400,  49547,  22835])
row5_python = np.array( [  11690 , 23129,  30467 , 22808,  11201])
total_python = np.array(
   [  11758 , 23554,  31080,  23261 , 11653,
 23193,  50619 , 77453,  50230,  23195,
 30994,  77276, 176874 , 76907 , 30932,
 23243 , 50009,  76400,  49547,  22835,
 11690,  23129 , 30467 , 22808,  11201
]
)


df_py = pd.DataFrame(
    {
        "Coluna1": row1_python,
        "Coluna2": row2_python,
        "Coluna3": row3_python,
        "Coluna4": row4_python,
        "Coluna5": row5_python,
    }
)

fig = plt.figure()
plt.imshow(df_py, origin="lower", cmap="viridis", extent=(-50, 50, -50, 50))
plt.colorbar(label="Fluxo de Nêutrons Python lado 1")
plt.title("Fluxo de Nêutrons Python lado 50")
plt.xlabel("X [cm]")
plt.ylabel("Y [cm]")
plt.show()


####lado 5 ###
### total 25#####


row1_openmc = np.array([	   523 	,
2.169 	,
3.572 	,
2.185 	,
526 	

])
row2_openmc = np.array([
2.198 	,
12.661 	,
24.161 	,
12.596 	,
2.174 	
])
row3_openmc = np.array([
    3.606 	,
24.215 	,
49.360 	,
24.187 	,
3.568 	

   	])
row4_openmc = np.array([
2.171 	,
12.650 	,
24.268 	,
12.612 	,
2.196 	
])
row5_openmc = np.array([ 
513 	,
2.158 	,
3.632 	,
2.171 	,
527 	

])
total_openmc = np.array(
    [
    523 	,
2.169 	,
3.572 	,
2.185 	,
526 	,
2.198 	,
12.661 	,
24.161 	,
12.596 	,
2.174 	,
3.606 	,
24.215 	,
49.360 	,
24.187 	,
3.568 	,
2.171 	,
12.650 	,
24.268 	,
12.612 	,
2.196 	,
513 	,
2.158 	,
3.632 	,
2.171 	,
527 	
   
    ]
)


df_mc_ = pd.DataFrame(
    {
        "Coluna1": row1_openmc,
        "Coluna2": row2_openmc,
        "Coluna3": row3_openmc,
        "Coluna4": row4_openmc,
        "Coluna5": row5_openmc,
    }
)
fig = plt.figure()
plt.imshow(df_mc_, origin="lower", cmap="viridis", extent=(-50, 50, -50, 50))
plt.colorbar(label="Fluxo de Nêutrons OpenMC lado50")
plt.title("Fluxo de Nêutrons OpenMC lado50")
plt.xlabel("X [cm]")
plt.ylabel("Y [cm]")
plt.show()

np_array_10 = np.array([])
for i in range(25):
    aux = (abs(total_python[i] - total_openmc[i])) * 100 / total_python[i]
    np_array_10 = np.append(np_array_10, aux)
    # print("np_array1", np_array_50)
sum_1 = np.sum(np_array_10)
# print("sum", sum_1 / 25)
reshapes = np_array_10.reshape((5, 5))


print("std:  ", np.std(np_array_10))