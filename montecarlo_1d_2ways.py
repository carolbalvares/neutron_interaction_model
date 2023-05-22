import numpy as np
import numpy as np

# creating class


class One_d_discr:
    def __init__(self, num_samples):
        self.num_samples = num_samples

    def n_neutrons_cross(cls, num_samples):
        cls.num_samples = num_samples
        right_samp_cross_array = []
        left_samp_cross_array = []
        array_num_samples_right = [num_samples]
        array_num_samples_left = [num_samples]
        r_samples_array = np.random.rand(num_samples).round(3)
        print("random samples array:          ",r_samples_array)
        r_prob = np.random.rand(2).round(3)
        right_prob = r_prob[0]
        left_prob = r_prob[1]
        print("right prob:          ",right_prob)
        print("left prob:          ",left_prob)
        # updated_samples = r_samples_array
        for i in range(num_samples):
            while num_samples != 0:
                if r_samples_array[i] > right_prob and r_samples_array[i] < left_prob:
                    right_samp_cross_array.append(r_samples_array[i])
                    num_samples = num_samples - 1
                elif r_samples_array[i] > left_prob and r_samples_array[i] < right_prob:
                    left_samp_cross_array.append(r_samples_array[i])
                    num_samples = num_samples - 1
                elif r_samples_array[i] < left_prob and r_samples_array[i] < right_prob:
                    num_samples = num_samples
                    r_samples_array[i] = np.random.rand(1).round(3)
                    print("new sample for _samples_array[i] < left_prob and r_samples_array[i] < right_prob:     ",r_samples_array[i])
                else:
                    num_samples = num_samples
                    r_samples_array[i] = np.random.rand(1).round(3)
                    print("new sample for _samples_array[i] > left_prob and r_samples_array[i] > right_prob:     ",r_samples_array[i])
            else:
                break
        print("samples that have crossed to the left side:          ",left_samp_cross_array)
        print("samples that have crossed to the right side:          ",right_samp_cross_array)
        array_num_samples_left = len(left_samp_cross_array)
        array_num_samples_right = len(right_samp_cross_array)
        print("array whith left side number of samples:          ",array_num_samples_left)
        print("array whith right side number of samples:          ",array_num_samples_right)
        return array_num_samples_right, array_num_samples_left


# calling class
initial_num_samples = int(input('Choose a initial number of samples:   '))
d_1d_1way = One_d_discr(initial_num_samples)
array_of_crossed = []
array_of_crossed = d_1d_1way.n_neutrons_cross(initial_num_samples)
print("return of class:     ",array_of_crossed)



