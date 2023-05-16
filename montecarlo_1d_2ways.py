import numpy as np

# setting number of samples and probability of it to cross
num_samples = 10
cross_prob_left = 0.6
cross_prob_right = 0.7

#if bigger than 0.7 probability of crossing
same_cross_prob_prob_right = 0.3

# resseting initial parameters 
samp_cross_left_array = []
samp_cross_rignt_array = []
samp_dont_cross_array = []
count = 0
random_samples_array = np.random.rand(num_samples).round(3)
print(random_samples_array)

for i in range(num_samples):
    if random_samples_array[i] < cross_prob_left:
        samp_dont_cross_array.append(random_samples_array[i])
    elif cross_prob_right>random_samples_array[i]>=cross_prob_left:
        samp_cross_left_array.append(random_samples_array[i])
    else:
        samp_cross_rignt_array.append(random_samples_array[i])
        
print("samp_dont_cross_array:          ",samp_dont_cross_array)
print("samp_cross_left_array:          ",samp_cross_left_array)
print("samp_cross_rignt_array:          ",samp_cross_rignt_array)