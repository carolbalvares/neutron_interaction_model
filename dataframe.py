# from probability import probability, free_neutrons_all, r_probability, free_neutrons_right, l_reversed_prob, free_neutrons_left
from montecarlo_1d_1way import *
import pandas as pd

# setting data frame
n_cross_df = pd.DataFrame({
    "number_neutrons_crossed": array_of_crossed
})
n_cross_df.head()
n_cross_df_T = n_cross_df.T
# print(n_cross_df_T)


