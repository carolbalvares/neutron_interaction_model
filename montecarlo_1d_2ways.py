import numpy as np

# setting number of samples and probability of it to cross
num_samples = 10
cross_prob_left = 0.6
cross_prob_right = 0.7

# if bigger than 0.7 probability of crossing to the right discretization
s_cross_prob_right = 0.45


# resseting initial parameters
samp_cross_left_array = []
samp_cross_right_array = []
samp_dont_cross_array = []
two_ways_samples = []
random_samples_array = np.random.rand(num_samples).round(3)
# print(random_samples_array)

for i in range(num_samples):
    if random_samples_array[i] < cross_prob_left:
        samp_dont_cross_array.append(random_samples_array[i])
    elif cross_prob_right > random_samples_array[i] >= cross_prob_left:
        samp_cross_left_array.append(random_samples_array[i])
    else:
        two_ways_samples.append(random_samples_array[i])

for e in range(len(two_ways_samples)):
    random_prob = np.random.rand(1).round(3)
    # print("random prob:         ",random_prob)
    if random_prob >= s_cross_prob_right:
        samp_cross_left_array.append(two_ways_samples[e])
    else:
        samp_cross_right_array.append(two_ways_samples[e])
    # print("sample:          ",two_ways_samples[e])


# print("samp_dont_cross_array:          ",samp_dont_cross_array)
# print("samp_cross_left_array:          ", samp_cross_left_array)
# print("samp_cross_right_array:          ", samp_cross_right_array)
