import numpy as np
import numpy as np

# creating class


class One_d_discr:
    def __init__(self, num_samples):
        self.num_samples = num_samples

    def n_neutrons_cross(cls, num_samples):
        cls.num_samples = num_samples
        aux = []
        right_samp_cross_array = np.array(aux)
        left_samp_cross_array = np.array(aux)
        array_num_samples_left = np.array(aux)
        array_num_samples_right = np.array(aux)
        print("carol", array_num_samples_left)
        r_samples_array = np.random.rand(num_samples).round(3)
        print("random samples array:          ", r_samples_array)
        r_prob = np.random.rand(2).round(3)
        right_prob = r_prob[0]
        left_prob = r_prob[1]
        print("right prob:          ", right_prob)
        print("left prob:          ", left_prob)
        # updated_samples = r_samples_array
        while num_samples != 0:
            for i in range(num_samples):
                if r_samples_array[i] > right_prob and r_samples_array[i] < left_prob:
                    right_samp_cross_array = np.append(
                        right_samp_cross_array, r_samples_array[i])
                    array_num_samples_right = np.append(
                        array_num_samples_right, (len(array_num_samples_right)+1))
                    if len(array_num_samples_left) != 0 :
                        array_num_samples_left = np.append(
                            array_num_samples_left, (len(array_num_samples_left)-1))
                    num_samples = num_samples - 1
                elif r_samples_array[i] > left_prob and r_samples_array[i] < right_prob:
                    left_samp_cross_array = np.append(
                        left_samp_cross_array, r_samples_array[i])
                    array_num_samples_left = np.append(
                        array_num_samples_left, (len(array_num_samples_left)+1))
                    if len(array_num_samples_right) !=0:
                        array_num_samples_right = np.append(
                            array_num_samples_right, (len(array_num_samples_right)-1))
                    num_samples = num_samples - 1
                elif r_samples_array[i] < left_prob and r_samples_array[i] < right_prob:
                    if len(array_num_samples_right) != 0:
                        array_num_samples_right = np.append(
                            array_num_samples_right, (len(array_num_samples_right)-1))
                    if len(array_num_samples_left) != 0:
                        array_num_samples_left = np.append(
                            array_num_samples_left, (len(array_num_samples_left)-1))
                    num_samples = num_samples
                    print("sample to be recreated:        ",
                          r_samples_array[i])
                    r_samples_array[i] = np.random.rand(1).round(3)
                    print(
                        "new sample for _samples_array[i] < left_prob and r_samples_array[i] < right_prob:     ", r_samples_array[i])
                else:
                    num_samples = num_samples
                    if len(array_num_samples_right)!= 0:
                        array_num_samples_right = np.append(
                            array_num_samples_right, (len(array_num_samples_right)-1))
                    if len(array_num_samples_left) != 0:
                        array_num_samples_left = np.append(
                            array_num_samples_left, (len(array_num_samples_left)-1))
                    print("sample to be recreated:        ",
                          r_samples_array[i])
                    r_samples_array[i] = np.random.rand(1).round(3)
                    print(
                        "new sample for _samples_array[i] > left_prob and r_samples_array[i] > right_prob:     ", r_samples_array[i])
        print("array whith right side number of samples:          ",
              array_num_samples_right)
        print("samples that have crossed to the left side:          ",
              left_samp_cross_array)
        print("samples that have crossed to the right side:          ",
              right_samp_cross_array)
        print("array whith left side number of samples:          ",
              array_num_samples_left)
        return array_num_samples_right, array_num_samples_left


# calling class
initial_num_samples = int(input('Choose a initial number of samples:   '))
d_1d_1way = One_d_discr(initial_num_samples)
array_of_crossed = []
array_of_crossed = d_1d_1way.n_neutrons_cross(initial_num_samples)
print("return of class:     ", array_of_crossed)
