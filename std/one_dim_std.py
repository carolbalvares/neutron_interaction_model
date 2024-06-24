finite_dif_one_dim =  [56387 , 5389 ,  515   , 49  ,   5]

import numpy as np

# Definição dos vetores
monte_carlo_one_dim = np.array([7475, 2058, 142, 9, 1])


python_one_dim = np.array([3782, 143, 4, 0, 0])
one_dim_mc= [124074, 64476, 33520,  17682,  9267]
one_dim_fin_dif = [491631, 393305, 294979, 196653,  98326]

 
root_square_error = math.sqrt(sum((mc - fd) ** 2 for mc, fd in zip(one_dim_mc, one_dim_fin_dif)))
root_square_error
592916.1766160543

# Cálculo da diferença absoluta
absolute_difference = np.abs(monte_carlo_one_dim - python_one_dim)

# Cálculo da diferença percentual
percent_difference = (absolute_difference / monte_carlo_one_dim) * 100

print("Diferença Absoluta:", absolute_difference)
print("Diferença Percentual:", percent_difference)