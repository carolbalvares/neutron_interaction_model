import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


row1_python50 = np.array([19268, 43654, 48772, 43654, 19268])
row2_python50 = np.array([40945, 90022, 98154, 90022, 40945])
row3_python50 = np.array([43354, 92736, 173415, 92736, 43354])
row4_python50 = np.array([40945, 90022, 98154, 90022, 40945])
row5_python50 = np.array([19268, 43654, 48772, 43654, 19268])
total_python50 = np.array(
    [
        19268,
        43654,
        48772,
        43654,
        19268,
        40945,
        90022,
        98154,
        90022,
        40945,
        43354,
        92736,
        173415,
        92736,
        43354,
        40945,
        90022,
        98154,
        90022,
        40945,
        19268,
        43654,
        48772,
        43654,
        19268,
    ]
)


df_py_50 = pd.DataFrame(
    {
        "Coluna1": row1_python50,
        "Coluna2": row2_python50,
        "Coluna3": row3_python50,
        "Coluna4": row4_python50,
        "Coluna5": row5_python50,
    }
)

fig = plt.figure()
plt.imshow(df_py_50, origin="lower", cmap="viridis", extent=(-50, 50, -50, 50))
plt.colorbar(label="Fluxo de Nêutrons Python lado 50")
plt.title("Fluxo de Nêutrons Python lado 50")
plt.xlabel("X [cm]")
plt.ylabel("Y [cm]")
plt.show()

row1_openmc50 = np.array([3900, 3978, 3925, 3956, 3849])
row2_openmc50 = np.array([3946, 4116, 4103, 3976, 3928])
row3_openmc50 = np.array([4013, 4137, 4141, 3985, 3938])
row4_openmc50 = np.array([4078, 4222, 4079, 3909, 3974])
row5_openmc50 = np.array([3879, 4006, 4082, 3980, 3900])
total_openmc50 = np.array(
    [
        3900,
        3978,
        3925,
        3956,
        3849,
        3946,
        4116,
        4103,
        3976,
        3928,
        4013,
        4137,
        4141,
        3985,
        3938,
        4078,
        4222,
        4079,
        3909,
        3974,
        3879,
        4006,
        4082,
        3980,
        3900,
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
    aux = (abs(total_python50[i] - total_openmc50[i])) * 100 / total_python50[i]
    np_array_10 = np.append(np_array_10, aux)
    # print("np_array1", np_array_50)
sum_1 = np.sum(np_array_10)
# print("sum", sum_1 / 25)
reshapes = np_array_10.reshape((5, 5))


for i in range(1):
    df_10 = pd.DataFrame(
        {
            "Coluna1": reshapes[i],
            "Coluna2": reshapes[i + 1],
            "Coluna3": reshapes[i + 2],
            "Coluna4": reshapes[i + 3],
            "Coluna5": reshapes[i + 4],
        }
    )
fig = plt.figure()
plt.imshow(df_10, origin="lower", cmap="viridis", extent=(-5, 5, -5, 5))
plt.colorbar(label="Fluxo de Nêutrons python 1")
plt.title("STD")
plt.xlabel("X [cm]")
plt.ylabel("Y [cm]")
plt.show()

print("para lado 10 do python e lado 10 openmc:  ", np.std(np_array_10))