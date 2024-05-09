import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


row1_python = np.array([ 10394,  20930,  28445,  20711,  10337])
row2_python = np.array( [ 20829,  46065,  72324,  46096,  21339])
row3_python = np.array( [ 28314,  72135, 171527 , 72222,  28880])
row4_python = np.array([ 21010,  46415,  73140,  46308,  21254])
row5_python = np.array([ 10347 , 21232,  28629 , 21249 , 10474])
total_python = np.array(
    [
   10394,  20930,  28445,  20711,  10337,  20829,  46065,  72324,  46096,  21339, 28314,  72135, 171527 , 72222,  28880,  21010,  46415,  73140,  46308,  21254, 10347 , 21232,  28629 , 21249 , 10474
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




row1_openmc50 = np.array([523 	,
2169 	,
3572 	,
2185 	,
526 	
])
row2_openmc50 = np.array([2198 	,
12661 	,
24161 	,
12596 	,
2174 	

])
row3_openmc50 = np.array([
    3606 	,
24215 	,
49360 	,
24187 	,
3568 	])
row4_openmc50 = np.array([2171 	,
12650 	,
24268 	,
12612 	,
2196 	

])
row5_openmc50 = np.array([ 
                          513 	,
2158 	,
3632 	,
2171 	,
527 	

])
total_openmc50 = np.array(
    [
        523 	,
2169 	,
3572 	,
2185 	,
526 	,
2198 	,
12661 	,
24161 	,
12596 	,
2174 	,
3606 	,
24215 	,
49360 	,
24187 	,
3568 	,
2171 	,
12650 	,
24268 	,
12612 	,
2196 	,
513 	,
2158 	,
3632 	,
2171 	,
527 	,


    ]
)


df_mc_50 = pd.DataFrame(
    {
        "Coluna1": row1_openmc50,
        "Coluna2": row2_openmc50,
        "Coluna3": row3_openmc50,
        "Coluna4": row4_openmc50,
        "Coluna5": row5_openmc50,
    }
)
fig = plt.figure()
plt.imshow(df_mc_50, origin="lower", cmap="viridis", extent=(-50, 50, -50, 50))
plt.colorbar(label="Fluxo de Nêutrons OpenMC lado50")
plt.title("Fluxo de Nêutrons OpenMC lado50")
plt.xlabel("X [cm]")
plt.ylabel("Y [cm]")
plt.show()

np_array_10 = np.array([])
for i in range(25):
    aux = (abs(total_python[i] - total_openmc50[i])) * 100 / total_python[i]
    np_array_10 = np.append(np_array_10, aux)
    # print("np_array1", np_array_50)
sum_1 = np.sum(np_array_10)
# print("sum", sum_1 / 25)
reshapes = np_array_10.reshape((5, 5))


print("std:  ", np.std(np_array_10))