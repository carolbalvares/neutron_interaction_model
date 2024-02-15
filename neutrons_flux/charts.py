import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# row1_1 = np.array([2412, 2815, 2561, 4353, 2308])
# row2_1 = np.array([3220, 4975, 1482, 5915, 2924])
# row3_1 = np.array([2341, 2948, 7670, 4620, 4072])
# row4_1 = np.array([3573, 5661, 4268, 7867, 4756])
# row5_1 = np.array([2613, 2265, 2817, 5420, 6144])
# total_1 = np.array(
#     [
#         2412,
#         2815,
#         2561,
#         4353,
#         2308,
#         3220,
#         4975,
#         1482,
#         5915,
#         2924,
#         2341,
#         2948,
#         7670,
#         4620,
#         4072,
#         3573,
#         5661,
#         4268,
#         7867,
#         4756,
#         2613,
#         2265,
#         2817,
#         5420,
#         6144,
#     ]
# )
# df_1 = pd.DataFrame(
#     {
#         "Coluna1": row1_1,
#         "Coluna2": row2_1,
#         "Coluna3": row3_1,
#         "Coluna4": row4_1,
#         "Coluna5": row5_1,
#     }
# )
# fig = plt.figure()
# plt.imshow(df_1, origin="lower", cmap="viridis", extent=(-5, 5, -5, 5))
# plt.colorbar(label="Fluxo de Nêutrons python 1")
# plt.title("Distribuição de Fluxo de Nêutrons 1")
# plt.xlabel("X [cm]")
# plt.ylabel("Y [cm]")
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
plt.title("Distribuição de Fluxo de Nêutrons 10")
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

###vacuum
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
plt.title("Distribuição de Fluxo de Nêutrons openmc")
plt.xlabel("X [cm]")
plt.ylabel("Y [cm]")
plt.show()

###reflective
# row1_openmc2 = np.array([945, 1011, 1043, 1022, 953])
# row2_openmc2 = np.array([1017, 1076, 1109, 1080, 1020])
# row3_openmc2 = np.array([1047, 1115, 1144, 1112, 74982])
# row4_openmc2 = np.array([1025, 1089, 1111, 1073, 1014])
# row5_openmc2 = np.array([965, 1026, 1048, 1019, 955])
# total_openmc2 = np.array(
#     [
#         945,
#         1011,
#         1043,
#         1022,
#         953,
#         1017,
#         1076,
#         1109,
#         1080,
#         1020,
#         1047,
#         1115,
#         1144,
#         1112,
#         74982,
#         1025,
#         1089,
#         1111,
#         1073,
#         1014,
#         965,
#         1026,
#         1048,
#         1019,
#         955,
#     ]
# )


# df_mc_2 = pd.DataFrame(
#     {
#         "Coluna1": row1_openmc2,
#         "Coluna2": row2_openmc2,
#         "Coluna3": row3_openmc2,
#         "Coluna4": row4_openmc2,
#         "Coluna5": row5_openmc2,
#     }
# )
# fig = plt.figure()
# plt.imshow(df_mc_2, origin="lower", cmap="viridis", extent=(-50, 50, -50, 50))
# plt.colorbar(label="Fluxo de Nêutrons python 10")
# plt.title("Distribuição de Fluxo de Nêutrons openmc2")
# plt.xlabel("X [cm]")
# plt.ylabel("Y [cm]")
# plt.show()

# ###reflective side 50
# row1_openmc_refl_50 = np.array([3900, 3978, 3925, 3956, 3849])
# row2_openmc_refl_50 = np.array([3946, 4116, 4103, 3976, 3928])
# row3_openmc_refl_50 = np.array([4013, 4137, 4141, 3985, 3938])
# row4_openmc_refl_50 = np.array([3879, 4006, 4082, 3980, 3900])
# row5_openmc_refl_50 = np.array([4078, 4222, 4079, 3909, 3974])
# total_openmc_refl_50 = np.array(
#     [
#         3900,
#         3978,
#         3925,
#         3956,
#         3849,
#         3946,
#         4116,
#         4103,
#         3976,
#         3928,
#         4013,
#         4137,
#         4141,
#         3985,
#         3938,
#         4078,
#         4222,
#         4079,
#         3909,
#         3974,
#         3879,
#         4006,
#         4082,
#         3980,
#         3900,
#     ]
# )


# df_mc_2_0 = pd.DataFrame(
#     {
#         "Coluna1": row1_openmc_refl_50,
#         "Coluna2": row2_openmc_refl_50,
#         "Coluna3": row3_openmc_refl_50,
#         "Coluna4": row4_openmc_refl_50,
#         "Coluna5": row5_openmc_refl_50,
#     }
# )
# fig = plt.figure()
# plt.imshow(df_mc_2_0, origin="lower", cmap="viridis", extent=(-50, 50, -50, 50))
# plt.colorbar(label="Fluxo de Nêutrons python 10")
# plt.title("Distribuição de Fluxo de Nêutrons openmc_refl_50")
# plt.xlabel("X [cm]")
# plt.ylabel("Y [cm]")
# plt.show()

###reflective side 50
# row1_openmc_refl_50 = np.array([998	,
# 1996	,
# 1999	,
# 1992	,
# 1999	,
# 996	])
# row2_openmc_refl_50 = np.array([2004	,
# 4004	,
# 3994	,
# 4004	,
# 3995	,
# 1988	])
# row3_openmc_refl_50 = np.array([2005	,
# 4013	,
# 3993	,
# 3992	,
# 4003	,
# 1997	])
# row4_openmc_refl_50 = np.array([1998	,
# 3994	,
# 3999	,
# 4006	,
# 3995	,
# 1996	])
# row5_openmc_refl_50 = np.array([2005	,
# 4007	,
# 4008	,
# 4002	,
# 3994	,
# 2005	])
# row6_openmc_refl_50 = np.array([1002	,
# 2000	,
# 2005	,
# 2008	,
# 2003	,
# 1002	])
# total_openmc_refl_50 = np.array(
#     [
#         3900,
#         3978,
#         3925,
#         3956,
#         3849,
#         3946,
#         4116,
#         4103,
#         3976,
#         3928,
#         4013,
#         4137,
#         4141,
#         3985,
#         3938,
#         4078,
#         4222,
#         4079,
#         3909,
#         3974,
#         3879,
#         4006,
#         4082,
#         3980,
#         3900,
#     ]
# )


# df_mc_2_0 = pd.DataFrame(
#     {
#         "Coluna1": row1_openmc_refl_50,
#         "Coluna2": row2_openmc_refl_50,
#         "Coluna3": row3_openmc_refl_50,
#         "Coluna4": row4_openmc_refl_50,
#         "Coluna5": row5_openmc_refl_50,
#         "Coluna6": row6_openmc_refl_50,
#     }
# )
# fig = plt.figure()
# plt.imshow(df_mc_2_0, origin="lower", cmap="viridis", extent=(-50, 50, -50, 50))
# plt.colorbar(label="Fluxo de Nêutrons python 10")
# plt.title("Distribuição de Fluxo de Nêutrons openmc_refl_50")
# plt.xlabel("X [cm]")
# plt.ylabel("Y [cm]")
# plt.show()


row1_python50 = np.array([1272, 2882, 3220, 2882, 1272])
row2_python50 = np.array([2703, 5942, 6479, 5942, 2703])
row3_python50 = np.array([2862, 6121, 11445, 6121, 2862])
row4_python50 = np.array([2703, 5942, 6479, 5942, 2703])
row5_python50 = np.array([1272, 2882, 3220, 2882, 1272])
total_python50 = np.array(
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
plt.colorbar(label="Fluxo de Nêutrons python 10")
plt.title("Distribuição de Fluxo de Nêutrons python50")
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
plt.colorbar(label="Fluxo de Nêutrons python 10")
plt.title("Distribuição de Fluxo de Nêutrons open50")
plt.xlabel("X [cm]")
plt.ylabel("Y [cm]")
plt.show()

# =(|valor openmc - valor seu|x100%/valor openmc


np_array_50 = np.array([])
for i in range(25):
    aux = (abs(total_openmc50[i] - total_10[i])) * 100 / total_openmc50[i]
    np_array_50 = np.append(np_array_50, aux)
    print("np_array1", np_array_50)
sum_1 = np.sum(np_array_50)
print("sum", sum_1 / 25)
reshapes = np_array_50.reshape((5, 5))


for i in range(1):
    df_1_error = pd.DataFrame(
        {
            "Coluna1": reshapes[i],
            "Coluna2": reshapes[i + 1],
            "Coluna3": reshapes[i + 2],
            "Coluna4": reshapes[i + 3],
            "Coluna5": reshapes[i + 4],
        }
    )
fig = plt.figure()
plt.imshow(df_1_error, origin="lower", cmap="viridis", extent=(-5, 5, -5, 5))
plt.colorbar(label="Fluxo de Nêutrons python 1")
plt.title("Distribuição de Fluxo de Nêutrons_erro")
plt.xlabel("X [cm]")
plt.ylabel("Y [cm]")
plt.show()

print("para lado 50 do python e lado 50 openmc", np.std(np_array_50))

np_array_10 = np.array([])
for i in range(25):
    aux = (abs(total_10[i] - total_openmc[i])) * 100 / total_openmc[i]
    np_array_10 = np.append(np_array_10, aux)
    print("np_array1", np_array_50)
sum_1 = np.sum(np_array_10)
print("sum", sum_1 / 25)
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
plt.title("Distribuição de Fluxo de Nêutrons_erro")
plt.xlabel("X [cm]")
plt.ylabel("Y [cm]")
plt.show()

print("para lado 10 do python e lado 10 openmc", np.std(np_array_10))
