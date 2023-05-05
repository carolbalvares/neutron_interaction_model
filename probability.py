# import seaborn as sns
# import pandas as pd
import numpy as np


## probability using all indices
#setting vars
probability = [0.7, 0.1, 0.9, 0.1, 0.6, 0.7, 0.6, 1, 0.45, 0.9]
free_neutrons = [100000]
short_prob = []
#looping
for e in (range(10)):
    free_neutrons.append(free_neutrons[e] * probability[e])
#converting floar into int
int_free_neutrons = ['%i' % elem for elem in free_neutrons]
#print("neutrons amount for each interaction: ", int_free_neutrons)


#choosing input for second and third probability
discr_input = int(input('Choose a start from 0 to 9:   '))


##second probability: from specific discretization for the discr_input :10
#reseting vars
probability = [0.7, 0.1, 0.9, 0.1, 0.6, 0.7, 0.6, 1, 0.45, 0.9]
free_neutrons = [100000]
indices = []
int_free_neutrons = []
#setting vars values
del probability[0:discr_input]
indices = range(10-discr_input)
#looping
for e in indices:
    free_neutrons.append(free_neutrons[e] * probability[e])
#converting floar into int
int_free_neutrons = ['%i' % elem for elem in free_neutrons]
#print("neutrons amount for each interaction: ", int_free_neutrons)


##third probability: from specific discretization for the 0 : discr_input
probability = np.array([0.7, 0.1, 0.9, 0.1, 0.6, 0.7, 0.6, 1, 0.45, 0.9])
free_neutrons = [100000]
indices = []
int_free_neutrons = []
#setting vars values
indices = range(discr_input)
probability = np.take(probability, indices)
#reversing probabilty array
reversed_prob = probability[::-1]
#looping
for e in indices:
    free_neutrons.append(free_neutrons[e] * reversed_prob[e])
#converting floar into int
int_free_neutrons = ['%i' % elem for elem in free_neutrons]
#print("neutrons amount for each interaction: ", int_free_neutrons)


# settingg data frame
# prob_df = pd.DataFrame({"probability": probability})
