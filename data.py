import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

##ONE DIMENSION

python_1d = [89900, 9087, 911, 85, 15]
openmc_1d=[7481, 2054, 139, 8, 0]


## TWO DIMENSIONS PYTHON
#ONE FUEL
one_fuel_python_two_dim = np.array(
[[ 11271,  22950,  30757,  22721,  11430],
 [ 22615,  49536,  76601,  49285,  22983],
 [ 30242,  76126, 177070,  76686,  30819],
 [ 23034,  49810,  77296,  49792,  23231],
 [ 11572,  23041,  30808,  22822,  11557]])


#TWO FUELS
two_fuels_python_two_dim = np.array([
    [13879, 11858, 5982, 2642, 950],
    [43584, 27423, 9309, 3656, 1327],
    [132899, 46128, 14229, 1161, 708],
    [42741, 25028, 6960, 374, 297],
    [13086, 10366, 2682, 805, 76]
])



## TWO DIMENSIONS OPENMC
#ONE FUEL
dados_1_fuel = [
    523.279004, 2168.936060, 3571.512504, 2185.006363, 525.697360,
    2197.683749, 12661.421117, 24161.207437, 12595.640454, 2173.572822,
    3605.617669, 24215.271718, 49360.123614, 24187.019510, 3568.238635,
    2170.938314, 12650.431384, 24268.280515, 12612.123250, 2195.513602,
    513.449598, 2157.760072, 3631.601986, 2171.109212, 526.930728
]

dados_arredondados = [round(num) for num in dados_1_fuel]
array_5x5 = np.array(dados_arredondados).reshape(5, 5)
dados_openmc_1_fuel = array_5x5
print("array_5x5", array_5x5)

#[  523  2169  3572  2185   526]
#[ 2198 12661 24161 12596  2174]
#[ 3606 24215 49360 24187  3568]
#[ 2171 12650 24268 12612  2196]
#[  513  2158  3632  2171   527]


#TWO FUEL

import matplotlib.pyplot as plt
import numpy as np

# Dados da contagem de nêutrons
neutron_count_data = [
    154.296755, 248.654716, 162.416725, 97.017701, 151.805467, 232.432938, 141.320686,
    1317.152938, 2143.269191, 1122.724266, 504.250580, 1095.267562, 2051.546448, 1237.214166,
    6386.441436, 10407.463775, 4738.546517, 1558.353397, 4545.791608, 10022.281368, 6145.666243, 10685.897103, 16641.625137, 7847.271076,
    2323.861223, 7487.261480, 15925.691608, 10183.015271, 6436.618149, 10398.128644, 4749.030859, 1573.594470,
    4563.551286, 9971.905661, 6165.691177, 1304.066889, 2133.196767, 1106.685375, 517.570215, 1091.913929, 2066.837452, 1243.343589,
    152.432225, 251.928326, 156.888182, 96.494780, 153.436496, 224.517845, 144.070805
]

# Reshape dos dados para uma matriz 7x7
neutron_count_grid = np.array(neutron_count_data).reshape(7, 7)

# Função para plotar o gráfico
def plot_grid(neutron_count_grid):
    plt.figure(figsize=(10, 8))
    im = plt.imshow(neutron_count_grid, cmap='viridis', interpolation='nearest')
    plt.colorbar(im, label='Neutron Count')
    plt.title('Neutron Transport Simulation')
    plt.show()

# Executando a função de plotagem
plot_grid(neutron_count_grid)

#[
#    [  154,  249,  162,   97,  152,  232,  141],
#   [ 1317, 2143, 1123,  504, 1095, 2052, 1237],
#    [ 6386, 10407, 4739, 1558, 4546, 10022, 6146],
#   [10686, 16642, 7847, 2324, 7487, 15926, 10183],
#   [ 6437, 10398, 4749, 1574, 4564, 9972, 6166],
#   [ 1304, 2133, 1107,  518, 1092, 2067, 1243],
#   [  152,  252,  157,   96,  153,  225,  144]
#]

#ERRO PERCENTUAL ABSOLUTO

# Calculando o erro percentual absoluto
erro_percentual_absoluto = np.abs((dados_openmc_1_fuel - one_fuel_python_two_dim) / dados_openmc_1_fuel) * 100
erro_percentual_absoluto_int = erro_percentual_absoluto.astype(int) 
# Imprimindo o erro percentual absoluto
print("Erro Percentual Absoluto:")
print(erro_percentual_absoluto_int)

###[[  55   79   61  130  558]
 ###[  81   98   45   20  310]
 ###[  63   45  149   90  378]
 ###[ 124   17   90  134  503]
 ###[ 573  303  371  511 1151]]

