import numpy as np

# setting number of samples and probability of it to cross
num_samples = 10
f_cross_prob = 0.6
s_cross_prob = 0.4
t_cross_prob = 0.35


##First discretization
# resseting initial parameters 
samp_cross_array = []
count = 0
random_samples_array = np.random.rand(num_samples).round(3)
# print(random_samples_array)

for i in range(num_samples):
    if random_samples_array[i] >= f_cross_prob:
        samp_cross_array.append(random_samples_array[i])
        count += 1
        
num_samples = count
# print(samp_cross_array)
# print(count)

##Second discretization
# resseting initial parameters 
samp_cross_array = []
count = 0
random_samples_array = np.random.rand(num_samples).round(3)
# print(random_samples_array)

for i in range(num_samples):
    if random_samples_array[i] >= s_cross_prob:
        samp_cross_array.append(random_samples_array[i])
        count += 1
        
num_samples = count
# print(samp_cross_array)
# print(count)

##Third discretization
# resseting initial parameters 
samp_cross_array = []
count = 0
random_samples_array = np.random.rand(num_samples).round(3)
# print(random_samples_array)

for i in range(num_samples):
    if random_samples_array[i] >= t_cross_prob:
        samp_cross_array.append(random_samples_array[i])
        count += 1
        
num_samples = count
# print(samp_cross_array)
# print(count)









# pct_to_cross_prob= []
# count = 0

# for i in range(len(pct_to_cross)):
#     if pct_to_cross[i] >= 0.6:
#         pct_to_cross_prob.append(pct_to_cross[i])
#         count += 1
# div = np.divide(1,len(pct_to_cross_prob))
# pct_prob = np.arange(0.0,1.0,div)
# neutron_prob_cross_df = pd.DataFrame({
#     "Cross_prob": pct_to_cross_prob,
#     "Pct_prob": pct_prob
# })






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

