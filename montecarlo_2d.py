import numpy as np

# considering only vertical and horizontal crossing first

# setting number of samples and probability of it to cross
# assuming it starts to cross from center
# num_samples = 15

# creating samples to analyse
samples = [0.2, 0.25, 0.3, 0.39, 0.45, 0.65, 0.75, 0.8, 0.87, 0.95]
updated_samples = np.array(samples)

# cross probability to first crossing
cross_prob_left = 0.3
cross_prob_right = 0.4
cross_prob_up = 0.6
cross_prob_down = 0.8

# if prob<0.8
s_cross_prob_left = 0.3
s_cross_prob_right = 0.5
s_cross_prob_up = 0.2
# samp_cross_three_prob = np.array([])

# if prob<0.6
s_cross_prob_right = 0.3
s_cross_prob_left = 0.7
# samp_cross_two_prob = np.array([])

#if prob<0.7
s_cross_prob_right = 0.7

# setting arrays to contain samples
samp_cross_left_array = np.array([])
samp_cross_right_array = np.array([])
samp_cross_up_array = np.array([])
samp_cross_down_array = np.array([])
samp_dont_cross_array = np.array([])

#don't cross or prob >= 0.8
del_index = []
for i in range(len(samples)):
    if samples[i] < cross_prob_left:
        samp_dont_cross_array=  np.append(samp_dont_cross_array,samples[i])
        del_index.append(i)
    elif samples[i] >= cross_prob_down:
        samp_cross_down_array = np.append(samp_cross_down_array, samples[i])
        del_index.append(i)

updated_samples= np.delete(updated_samples, del_index)

for e in range(len(updated_samples)):
    updated_samples = np.random.rand(len(updated_samples)).round(2)  

#0.6 <= prob < 0.8
del_index = []
for i in range(len(updated_samples)):
    if  updated_samples[i] >=  s_cross_prob_right:
        samp_cross_right_array=  np.append(samp_cross_right_array,updated_samples[i])
        del_index.append(i)
    elif samples[i] < s_cross_prob_up:
            samp_cross_down_array = np.append(samp_cross_down_array, samples[i])
            del_index.append(i)

updated_samples = np.delete(updated_samples, del_index)

