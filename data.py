import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Dados unidimensionais para comparação entre Python e OpenMC
python_1d = [89900, 9087, 911, 85, 15]
openmc_1d = [7481, 2054, 139, 8, 0]

# Dados de duas dimensões com Python
# Dados com um combustível
one_fuel_python_two_dim =  np.array(
[[ 11394,  22933,  30612 , 23134,  11570],
 [ 23016,  50114 , 77020 , 50163 , 23018],
 [ 30740 , 77200 ,177295  ,77117 , 30575],
 [ 22957  ,50256 , 77136 , 50189,  23134],
 [ 11500 , 23445 , 30971 , 23231 , 11728]

])

total = np.sum(one_fuel_python_two_dim)
percentage_matrix = (one_fuel_python_two_dim / total) * 100

# Criando um gráfico heatmap usando seaborn e matplotlib
plt.figure(figsize=(10, 8))
sns.heatmap(percentage_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Heatmap de porcentagem da simulação de python para um combustível')
plt.show()

# Dados com dois combustíveis
two_fuels_python_two_dim = np.array([
    [9283, 15110, 15800, 15245, 16059, 15569, 9183],
    [21110, 35514, 32865, 29044, 33536, 36355, 21140],
    [39413, 74297, 52175, 33378, 51977, 74558, 39659],
    [62055, 170364, 69048, 51196, 68636, 170178, 62228],
    [39611, 74723, 52501, 33311, 52293, 74432, 39655],
    [21244, 35980, 33334, 28770, 32985, 35830, 20945],
    [9149, 15232, 15899, 15052, 15843, 15388, 8955]
])

total = np.sum(one_fuel_python_two_dim)
percentage_matrix = (one_fuel_python_two_dim / total) * 100

# Criando um gráfico heatmap usando seaborn e matplotlib
plt.figure(figsize=(10, 8))
sns.heatmap(percentage_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Heatmap de porcentagem da simulação de python para dois combustíveis')
plt.show()

# Dados de duas dimensões para OpenMC
# Dados para um combustível, já transformados em inteiros e organizados em uma matriz 5x5
dados_openmc_1_fuel = np.array([
[523, 2169, 3572, 2185, 526],
[2198, 12661, 24161, 12596, 2174],
[3606, 24215, 49360, 24187, 3568],
[2171, 12650, 24268, 12612, 2196],
[513, 2158, 3632, 2171, 527]
])

total = np.sum(one_fuel_python_two_dim)
percentage_matrix = (one_fuel_python_two_dim / total) * 100

# Criando um gráfico heatmap usando seaborn e matplotlib
plt.figure(figsize=(10, 8))
sns.heatmap(percentage_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Heatmap de porcentagem da simulação OpenMC para um combustível')
plt.show()


# Dados de contagem de nêutrons arredondados e transformados em uma matriz 7x7
dados_openmc_2_fuels= np.array([  154,   249,   162,    97,   152,   232,   141],
 [ 1317,  2143,  1123,   504,  1095,  2052,  1237],
 [ 6386, 10407,  4739,  1558,  4546, 10022,  6146],
 [10686, 16642,  7847,  2324,  7487, 15926, 10183],
 [ 6437, 10398,  4749,  1574,  4564,  9972,  6166],
 [ 1304,  2133,  1107,   518,  1092,  2067,  1243],
 [  152,   252,   157,    96,   153,   225,   144])

total = np.sum(one_fuel_python_two_dim)
percentage_matrix = (one_fuel_python_two_dim / total) * 100

# Criando um gráfico heatmap usando seaborn e matplotlib
plt.figure(figsize=(10, 8))
sns.heatmap(percentage_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Heatmap de porcentagem da simulação OpenMC para dois combustíveis')
plt.show()

