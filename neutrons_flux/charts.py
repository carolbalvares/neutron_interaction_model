import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

row1_1 = np.array([2412, 2815, 2561, 4353, 2308])
row2_1 = np.array([3220, 4975, 1482, 5915, 2924])
row3_1 = np.array([2341, 2948, 7670, 4620, 4072])
row4_1 = np.array([3573, 5661, 4268, 7867, 4756])
row5_1 = np.array([2613, 2265, 2817, 5420, 6144])
total_1 = np.array(
    [
        2412,
        2815,
        2561,
        4353,
        2308,
        3220,
        4975,
        1482,
        5915,
        2924,
        2341,
        2948,
        7670,
        4620,
        4072,
        3573,
        5661,
        4268,
        7867,
        4756,
        2613,
        2265,
        2817,
        5420,
        6144,
    ]
)
df_1 = pd.DataFrame(
    {
        "Coluna1": row1_1,
        "Coluna2": row2_1,
        "Coluna3": row3_1,
        "Coluna4": row4_1,
        "Coluna5": row5_1,
    }
)
fig = plt.figure()
plt.imshow(df_1, origin="lower", cmap="viridis", extent=(-5, 5, -5, 5))
plt.colorbar(label="Fluxo de Nêutrons python 1")
plt.title("Distribuição de Fluxo de Nêutrons")
plt.xlabel("X [cm]")
plt.ylabel("Y [cm]")
# plt.show()

row1_10 = np.array([1272, 2882, 3220, 2882, 1272])
row2_10 = np.array([2703, 5942, 6479, 5942, 2703])
row3_10 = np.array([2862, 6121, 11445, 6121, 2862])
row4_10 = np.array([2703, 5942, 6479, 5942, 2703])
row5_10 = np.array([1272, 2882, 3220, 2882, 1272])
total_10 = np.array(
    [
        1272,
        2882,
        3220,
        2882,
        1272,
        2703,
        5942,
        6479,
        5942,
        2703,
        2862,
        6121,
        11445,
        6121,
        2862,
        2703,
        5942,
        6479,
        5942,
        2703,
        1272,
        2882,
        3220,
        2882,
        1272,
    ]
)

df_10 = pd.DataFrame(
    {
        "Coluna1": row1_10,
        "Coluna2": row2_10,
        "Coluna3": row3_10,
        "Coluna4": row4_10,
        "Coluna5": row5_10,
    }
)

fig = plt.figure()
plt.imshow(df_10, origin="lower", cmap="viridis", extent=(-5, 5, -5, 5))
plt.colorbar(label="Fluxo de Nêutrons python 10")
plt.title("Distribuição de Fluxo de Nêutrons")
plt.xlabel("X [cm]")
plt.ylabel("Y [cm]")
# plt.show()

row1_openmc = np.array([3642, 3896, 4003, 3885, 3641])
row2_openmc = np.array([3910, 4143, 4260, 4125, 3885])
row3_openmc = np.array([4009, 4277, 4434, 4277, 4052])
row4_openmc = np.array([3896, 4148, 4306, 4146, 3909])
row5_openmc = np.array([3662, 3917, 4035, 3905, 3638])
total_openmc = np.array(
    [
        3642,
        3896,
        4003,
        3885,
        3641,
        3910,
        4143,
        4260,
        4125,
        3885,
        4009,
        4277,
        4434,
        4277,
        4052,
        3896,
        4148,
        4306,
        4146,
        3909,
        3662,
        3917,
        4035,
        3905,
        3638,
    ]
)


df_mc = pd.DataFrame(
    {
        "Coluna1": row1_openmc,
        "Coluna2": row2_openmc,
        "Coluna3": row3_openmc,
        "Coluna4": row4_openmc,
        "Coluna5": row5_openmc,
    }
)
fig = plt.figure()
plt.imshow(df_mc, origin="lower", cmap="viridis", extent=(-5, 5, -5, 5))
plt.colorbar(label="Fluxo de Nêutrons python 10")
plt.title("Distribuição de Fluxo de Nêutrons")
plt.xlabel("X [cm]")
plt.ylabel("Y [cm]")
# plt.show()
# =(|valor openmc - valor seu|x100%/valor openmc


np_array_1 = np.array([])
for i in range(25):
    aux = (abs(total_openmc[i] - total_1[i]))*100/total_openmc[i]
    np_array_1 = np.append(np_array_1, aux)
    #print("np_array1", np_array_1)
sum_1 = np.sum(np_array_1)
print("sum", sum_1/25)

np_array_10 = np.array([])
for i in range(25):
    aux = (abs(total_openmc[i] - total_10[i]))*100/total_openmc[i]
    np_array_10 = np.append(np_array_10, aux)
    #print("np_array1", np_array_10)
sum_10 = np.sum(np_array_10)
print("sum", sum_10/25)