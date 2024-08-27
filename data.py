import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Dados unidimensionais para comparação entre Python e OpenMC
python_1d = [89900, 9087, 911, 85, 15]
openmc_1d = [7481, 2054, 139, 8, 0]

# Dados de duas dimensões com Python
# Dados com um combustível
one_fuel_python_two_dim =  np.array([
    [523, 2169, 3572, 2185, 526],
    [2198, 12661, 24161, 12596, 2174],
    [3606, 24215, 49360, 24187, 3568],
    [2171, 12650, 24268, 12612, 2196],
    [513, 2158, 3632, 2171, 527]
])


# Dados com dois combustíveis
two_fuels_python_two_dim = np.array([
])

# Dados de duas dimensões para OpenMC
# Dados para um combustível, já transformados em inteiros e organizados em uma matriz 5x5
dados_openmc_1_fuel = np.array([
[523, 2169, 3572, 2185, 526],
[2198, 12661, 24161, 12596, 2174],
[3606, 24215, 49360, 24187, 3568],
[2171, 12650, 24268, 12612, 2196],
[513, 2158, 3632, 2171, 527]
])

# Dados de contagem de nêutrons arredondados e transformados em uma matriz 7x7
dados_openmc_2_fuels= np.array([  154,   249,   162,    97,   152,   232,   141],
 [ 1317,  2143,  1123,   504,  1095,  2052,  1237],
 [ 6386, 10407,  4739,  1558,  4546, 10022,  6146],
 [10686, 16642,  7847,  2324,  7487, 15926, 10183],
 [ 6437, 10398,  4749,  1574,  4564,  9972,  6166],
 [ 1304,  2133,  1107,   518,  1092,  2067,  1243],
 [  152,   252,   157,    96,   153,   225,   144])



