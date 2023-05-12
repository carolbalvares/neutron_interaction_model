from probability import probability, free_neutrons_all, r_probability, free_neutrons_right, l_reversed_prob, free_neutrons_left
import pandas as pd
from montecarlotest import *

# setting data frame
prob_all_df = pd.DataFrame({
    "probability": probability,
    "all_n": free_neutrons_all,
})
prob_all_df.head()
# print(prob_all_df)


prob_r_df = pd.DataFrame({
    "r_probability": r_probability,
    "r_n": free_neutrons_right
})
prob_r_df.head()
# print(prob_r_df)

prob_l_df = pd.DataFrame({
    "l_probability": l_reversed_prob,
    "l_n": free_neutrons_left
})
prob_l_df.head()
# print(prob_l_df)

ff_neutrons_all = [float(i) for i in free_neutrons_all]
oned_prob_df = pd.DataFrame({
    "all_n": ff_neutrons_all,
})
prob_all_df.head()
oned_prob_df_T = oned_prob_df.T
# print(oned_prob_df_T)


#creating one dataframe that counts duplicate commission amount
frequency = results_df['Commission_Amount'].value_counts()
duplicate_count_df = results_df.pivot_table(index = ['Commission_Amount'], aggfunc='size')
df.head()

monte_carlo_test_df = pd.DataFrame({
    "Frequency": frequency,
    "Comission_Amount":duplicate_count_df,
})
monte_carlo_test_df.head()
