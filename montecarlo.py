import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# setting avg, std_dev, num_reps, num_simulations
avg = 1
std_dev = 0.3
num_reps = 500000
num_simulations = 10000000

# use numpy to generate a list of percentages that will replicate our historical normal distribution
pct_to_cross = np.random.normal(avg, std_dev, num_reps).round(4)

pct_to_cross_prob= []
count = 0

for i in range(len(pct_to_cross)):
    if pct_to_cross[i] >= 0.6:
        pct_to_cross_prob.append(pct_to_cross[i])
        count += 1

neutron_prob_cross_df = pd.DataFrame({
    "Cross_prob": pct_to_cross_prob
})

df2 = neutron_prob_cross_df.sort_values('Cross_prob')
l=sns.distplot(df2)
plt.show()




# print (pct_to_cross_prob)

# neutron_prob_cross_df = pd.DataFrame({
#     "Pct_to_cross": pct_to_cross
# })


# def calc_neutron_cross(x):
#     if x >= 0.6:
#         return 1
#     else:
#         return 0
    
# neutron_prob_cross_df['Binominal'] = neutron_prob_cross_df['Pct_to_cross'].apply(calc_neutron_cross)

# neutron_prob_cross_df['Cross_true_prob'] = neutron_prob_cross_df['Pct_to_cross']*

# print(neutron_prob_cross_df)

# goals to arrive neutrons. Number that starts neutrons: 10000
# neutrons_target_values = [9000, 7000, 5000, 4000, 3000, 500]
# neutrons_cross_prob = [.3, .3, .2, .1, .05, .05]
# initial_neutrons = np.random.choice(
#     neutrons_target_values, num_reps, p=neutrons_cross_prob)
# # print(neutrons_target)

# # build up a pandas dataframe
# neutrons_df = pd.DataFrame(index=range(num_reps), data={'Pct_To_Cross': pct_to_cross,
#                                                         'Initial_neutrons': initial_neutrons})

# neutrons_df['Neutrons'] = neutrons_df['Pct_To_Cross'] * neutrons_df['Initial_neutrons']
# neutrons_df.head()
# print(neutrons_df)

# necessidade de regrar as possibilidades que crescem e os que o numero de neutrons aumenta?
#os numeros gerados serao de energia de neutrons ou numero de neutrons com certa velocidade

