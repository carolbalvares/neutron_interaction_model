import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Dados unidimensionais para comparação entre Python e OpenMC
python_1d = [89900, 9087, 911, 85, 15]
openmc_1d = [7481, 2054, 139, 8, 0]

# Dados de duas dimensões com Python
# Dados com um combustível
one_fuel_python_two_dim = np.array([
    [11271, 22950, 30757, 22721, 11430],
    [22615, 49536, 76601, 49285, 22983],
    [30242, 76126, 177070, 76686, 30819],
    [23034, 49810, 77296, 49792, 23231],
    [11572, 23041, 30808, 22822, 11557]
])

# Dados com dois combustíveis
two_fuels_python_two_dim = np.array([
    [13879, 11858, 5982, 2642, 950],
    [43584, 27423, 9309, 3656, 1327],
    [132899, 46128, 14229, 1161, 708],
    [42741, 25028, 6960, 374, 297],
    [13086, 10366, 2682, 805, 76]
])

# Dados de duas dimensões para OpenMC
# Dados para um combustível, já transformados em inteiros e organizados em uma matriz 5x5
dados_openmc_1_fuel = np.array([
[4, 18, 62, 92, 68, 19, 4],
 [22, 172, 920, 1766, 914, 166, 22],
 [62, 908, 9463, 22699, 9576, 918, 64],
 [98, 1768, 22521, 49546, 22563, 1744, 101],
 [61, 904, 9524, 22469, 9455, 896, 65],
 [19, 162, 912, 1756, 899, 170, 21],
 [4, 18, 64, 95, 66, 20, 3]
])

# Dados de contagem de nêutrons arredondados e transformados em uma matriz 7x7
dados_openmc_2_fuels= np.array([  154,   249,   162,    97,   152,   232,   141],
 [ 1317,  2143,  1123,   504,  1095,  2052,  1237],
 [ 6386, 10407,  4739,  1558,  4546, 10022,  6146],
 [10686, 16642,  7847,  2324,  7487, 15926, 10183],
 [ 6437, 10398,  4749,  1574,  4564,  9972,  6166],
 [ 1304,  2133,  1107,   518,  1092,  2067,  1243],
 [  152,   252,   157,    96,   153,   225,   144])




# # Função para plotar uma matriz como gráfico de calor
# def plot_heatmap(data, title, xlabel, ylabel):
#     plt.figure(figsize=(10, 8))
#     sns.heatmap(data, annot=True, cmap='viridis', fmt='d')
#     plt.title(title)
#     plt.xlabel(xlabel)
#     plt.ylabel(ylabel)
#     plt.show()

# # Execução da função de plotagem para os dados de um combustível
# plot_heatmap(dados_openmc_1_fuel_int, "Distribuição de Nêutrons - OpenMC, Um Combustível", "Posição X", "Posição Y")
