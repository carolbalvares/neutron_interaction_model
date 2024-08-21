import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

##ONE DIMENSION

python_1d = [89900, 9087, 911, 85, 15]
openmc_1d=[7481, 2054, 139, 8, 0]


## TWO DIMENSIONS PYTHON
#ONE FUEL
one_fuel_python_two_dim = np.array([
    [231, 454, 1384, 5030, 3464],
    [409, 219, 35056, 15129, 8914],
    [1304, 35119, 123185, 46146, 17078],
    [4874, 14858, 46224, 29601, 13255],
    [3456, 8713, 17107, 13265, 6593]
])

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

vetor_open_mc_2_fuels = [
    417.277881, 568.303584, 328.082992, 309.428923, 537.547924, 395.725026,
    3830.096881, 4741.876118, 1858.099379, 1824.086267, 4517.616617, 3658.592061,
    15360.686992, 18188.617726, 5435.373847, 5239.025079, 17428.737828, 14784.437258,
    15459.564036, 18189.189634, 5399.159350, 5214.448501, 17402.764544, 14801.381269,
    3856.860364, 4763.051403, 1887.989268, 1823.572185, 4527.080067, 3658.616315,
    413.811241, 561.672496, 317.545459, 320.884645, 526.441665, 395.762879
]

# Convertendo os números para inteiros
vetor_open_mc_2_fuels = [int(x) for x in vetor_open_mc_2_fuels]

# Transformando o vetor em uma matriz 6x6 usando numpy
matriz_numpy = np.array(vetor_open_mc_2_fuels).reshape(6, 6)

# Exibindo a matriz em numpy
print(matriz_numpy)
# [[  417   568   328   309   537   395]
#  [ 3830  4741  1858  1824  4517  3658]
#  [15360 18188  5435  5239 17428 14784]
#  [15459 18189  5399  5214 17402 14801]
#  [ 3856  4763  1887  1823  4527  3658]
#  [  413   561   317   320   526   395]]

plt.figure(figsize=(10, 8))
plt.imshow(matriz_numpy, cmap='viridis', interpolation='nearest')
plt.colorbar(label='Two Dimension Matrix with Two Fuels')  # Corrigido o rótulo do colorbar
plt.title('Two Dimension Matrix with Two Fuels')  # Corrigido o título
plt.show()

#ERRO PERCENTUAL ABSOLUTO

# Calculando o erro percentual absoluto
erro_percentual_absoluto = np.abs((dados_openmc_1_fuel - one_fuel_python_two_dim) / dados_openmc_1_fuel) * 100
erro_percentual_absoluto_int = erro_percentual_absoluto.astype(int) 
# Imprimindo o erro percentual absoluto
# print("Erro Percentual Absoluto:")
# print(erro_percentual_absoluto_int)

###[[  55   79   61  130  558]
 ###[  81   98   45   20  310]
 ###[  63   45  149   90  378]
 ###[ 124   17   90  134  503]
 ###[ 573  303  371  511 1151]]

