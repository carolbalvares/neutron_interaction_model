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







