import numpy as np
import pandas as pd

# creating class
class One_d_discr: 
    def __init__(self, num_samples):
        self.num_samples = num_samples
    def n_neutrons_cross(cls, num_samples):
        cls.num_samples = num_samples
        samp_cross_array = []
        array_num_samples = []
        r_prob = np.random.rand(1).round(3)
        r_samples_array = np.random.rand(num_samples).round(3)
        while num_samples !=  0:
            for i in range(num_samples):
                if r_samples_array[i] >= r_prob:
                    samp_cross_array.append(r_samples_array[i])
                    num_samples = num_samples - 1
            array_num_samples.append(num_samples)
            if num_samples != 0:
                r_prob = np.random.rand(1).round(3)
                r_samples_array = np.random.rand(num_samples).round(3)
            else:
                break  
        return array_num_samples


#calling class
initial_num_samples = int(input('Choose a initial number of samples:   '))
d_1d_1way = One_d_discr(initial_num_samples)
print(d_1d_1way.n_neutrons_cross(initial_num_samples))





