finite_dif_one_dim = [ 278456, 131233,  61433,   27875,
  10762]

import numpy as np

# Definição dos vetores
monte_carlo_one_dim = np.array([7475, 2058, 142, 9, 1])
python_one_dim = np.array([3782, 143, 4, 0, 0])

# Cálculo da diferença absoluta
absolute_difference = np.abs(monte_carlo_one_dim - python_one_dim)

# Cálculo da diferença percentual
percent_difference = (absolute_difference / monte_carlo_one_dim) * 100

print("Diferença Absoluta:", absolute_difference)
print("Diferença Percentual:", percent_difference)