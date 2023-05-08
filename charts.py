from dataframe import *
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# sns.jointplot(data=prob_all_df, x='all_n', y='probability',
            #   palette='Set2',  kind='scatter')
# plt.show()

# sns.jointplot(data=prob_l_df, x='l_n', y='l_probability',
#               palette='Set3',  kind='scatter')
# # plt.show()

# sns.jointplot(data=prob_r_df, x='r_n', y='r_probability',
#               palette='Set1',  kind='scatter')
# # plt.show()

# heatmap
column = ["1"]
# x = oned_prob_df.pivot(index='9', values='all_n', columns='0')
# x = oned_prob_df.pivot(index=oned_prob_df.index[0], columns=oned_prob_df.columns(), values=oned_prob_df.values())
#one_d_heat_map = oned_prob_df.pivot(index = 'oned_prob_df.index', columns ='oned_prob_df.columns', values = 'free_neutrons')
fig, ax = plt.subplots(figsize=(10, 2.5))
sns.heatmap(oned_prob_df_T, annot=True, fmt="g", cmap='viridis')
plt.show()
