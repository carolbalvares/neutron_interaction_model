import numpy as np


## probability using all index
#setting vars
probability = [0.7, 0.1, 0.9, 0.1, 0.6, 0.7, 0.6, 1, 0.45, 0.9]
free_neutrons = [100000]
short_prob = []
#looping
for e in (range(10)):
    free_neutrons.append(free_neutrons[e] * probability[e])
free_neutrons.remove(100000)
#converting floar into int
free_neutrons_all = ['%i' % elem for elem in free_neutrons]
# print("neutrons amount for each interaction: ", free_neutrons_all)


#choosing input for second and third probability
discr_input = int(input('Choose a start from 0 to 9:   '))


##second probability: from specific discretization for the discr_input :10
#reseting vars
r_probability = [0.7, 0.1, 0.9, 0.1, 0.6, 0.7, 0.6, 1, 0.45, 0.9]
free_neutrons = [100000]
index = []
#setting vars values
del r_probability[0:discr_input]
r_index = range(10-discr_input)
#looping
for e in r_index:
    free_neutrons.append(free_neutrons[e] * r_probability[e])
free_neutrons.remove(100000)
#converting floar into int
free_neutrons_right = ['%i' % elem for elem in free_neutrons]
# print("neutrons amount for each interaction: ", free_neutrons_right)
# print(r_index)


##third probability: from specific discretization for the 0 : discr_input
l_probability = np.array([0.7, 0.1, 0.9, 0.1, 0.6, 0.7, 0.6, 1, 0.45, 0.9])
free_neutrons = [100000]
l_index = []
#setting vars values
l_index = range(discr_input)
l_probability = np.take(l_probability, l_index)
#reversing probabilty array
l_reversed_prob = l_probability[::-1]
# print(l_index)
#looping
for e in l_index:
    free_neutrons.append(free_neutrons[e] * l_reversed_prob[e])
free_neutrons.remove(100000)
#converting floar into int
free_neutrons_left = ['%i' % elem for elem in free_neutrons]
#print("neutrons amount for each interaction: ", free_neutrons_left)



    
