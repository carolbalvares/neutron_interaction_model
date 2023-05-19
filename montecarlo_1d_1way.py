import numpy as np

# creating class
class One_d_discr: 
    def __init__(self, num_samples):
        self.num_samples = num_samples
        samp_cross_array = []
        r_prob = np.random.rand(1).round(3)
        print(r_prob)
        r_samples_array = np.random.rand(num_samples).round(3)
        print(r_samples_array)
        while num_samples !=  0:
            for i in range(num_samples):
                if r_samples_array[i] >= r_prob:
                    samp_cross_array.append(r_samples_array[i])
                    num_samples = num_samples - 1
                print(num_samples)
                print(samp_cross_array)
            if num_samples != 0:
                r_prob = np.random.rand(1).round(3)
                print(r_prob)
                r_samples_array = np.random.rand(num_samples).round(3)
                print(r_samples_array)
            else:
                break
       
            
#calling class
initial_num_samples = int(input('Choose a initial number of samples:   '))
d_1d_1way = One_d_discr(initial_num_samples)
print(d_1d_1way)




