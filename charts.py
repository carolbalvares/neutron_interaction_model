from dataframe import *
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from montecarlo_1d_1way import *

# heatmap
fig, ax = plt.subplots(figsize=(10, 2.5))
sns.heatmap(n_cross_df_T, annot=True, fmt="g", cmap='viridis')
plt.show()

# sns.jointplot(data=prob_all_df, x='all_n', y='probability',
#               palette='Set2',  kind='scatter')
# # plt.show()

# sns.jointplot(data=prob_l_df, x='l_n', y='l_probability',
#               palette='Set3',  kind='scatter')
# # plt.show()

# sns.jointplot(data=prob_r_df, x='r_n', y='r_probability',
#               palette='Set1',  kind='scatter')
# # plt.show()

# firt chart montecarlo
# df = neutron_prob_cross_df.sort_values('Cross_prob')
# l=sns.distplot(df)
# plt.show()

# sns.jointplot(data=neutron_prob_cross_df, x='Cross_prob', y='Pct_prob',
#               palette='Set1',  kind='scatter')
# plt.show()


