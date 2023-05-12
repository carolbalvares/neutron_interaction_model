from dataframe import *
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from montecarlotest import *
sns.jointplot(data=prob_all_df, x='all_n', y='probability',
              palette='Set2',  kind='scatter')
# plt.show()

sns.jointplot(data=prob_l_df, x='l_n', y='l_probability',
              palette='Set3',  kind='scatter')
# plt.show()

sns.jointplot(data=prob_r_df, x='r_n', y='r_probability',
              palette='Set1',  kind='scatter')
# plt.show()

# heatmap
fig, ax = plt.subplots(figsize=(10, 2.5))
sns.heatmap(oned_prob_df_T, annot=True, fmt="g", cmap='viridis')
# plt.show()

#create normal distribution curve with histrogram
l=sns.distplot(monte_carlo_test_df)
l.set_xlabel('Comission_Amount') 
l.set_ylabel('Frequency')
# plt.show()

#checking mean 
df2 = monte_carlo_test_df["Comission_Amount"].mean()
# print(df2)