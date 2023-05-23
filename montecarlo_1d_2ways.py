import numpy as np


class One_d_discr:
    def __init__(self, num_samples):
        self.num_samples = num_samples

    def n_neutrons_cross(self, num_samples):
        right_samp_cross_array = np.array([])
        left_samp_cross_array = np.array([])
        array_num_samples_left = np.array([])
        array_num_samples_right = np.array([])
        aux = 0
        r_samples_array = np.random.rand(num_samples).round(3)
        updated_samples = np.array([])
        updated_samples = r_samples_array
        print("random samples array:          ", r_samples_array)
        r_prob = np.random.rand(2).round(3)
        right_prob = r_prob[0]
        left_prob = r_prob[1]
        print("right prob:          ", right_prob)
        print("left prob:          ", left_prob)
        while num_samples != 0:
            if num_samples == 0:
                    break
            for i in range(len(updated_samples)-1, -1, -1):
                if len(array_num_samples_left) != 0 or len(array_num_samples_right) != 0:
                    if updated_samples[i] >= right_prob and updated_samples[i] < left_prob:
                        right_samp_cross_array = np.append(
                            right_samp_cross_array, updated_samples[i])
                        aux = array_num_samples_right[-1] + 1
                        array_num_samples_right = np.append(
                            array_num_samples_right, aux)
                        array_num_samples_left = np.append(
                            array_num_samples_left, array_num_samples_left[-1])
                        num_samples = num_samples- 1
                        print("crossed right side:      ", updated_samples[i])
                        updated_samples = np.delete(updated_samples, i, axis=0)
                        print("updated_sample:      ", updated_samples)
                        break
                    elif updated_samples[i] >= left_prob and updated_samples[i] < right_prob:
                        left_samp_cross_array = np.append(
                            left_samp_cross_array, updated_samples[i])
                        aux = array_num_samples_left[-1]+1
                        array_num_samples_left = np.append(
                            array_num_samples_left, aux)
                        array_num_samples_right = np.append(
                            array_num_samples_right, array_num_samples_right[-1])
                        num_samples = num_samples - 1
                        print("crossed left side:      ", updated_samples[i])
                        updated_samples = np.delete(updated_samples, i, axis=0)
                        print("updated_sample:      ", updated_samples)
                        break
                    else:
                        array_num_samples_right = np.append(
                            array_num_samples_right, array_num_samples_right[-1])
                        array_num_samples_left = np.append(
                            array_num_samples_left, array_num_samples_left[-1])
                        print("sample to be recreated:        ",
                              updated_samples[i])
                        updated_samples[i] = np.random.rand(1).round(3)
                        print(
                            "new sample for _samples_array[i] < left_prob and updated_samples[i] < right_prob:     ", updated_samples[i])
                        print("updated_sample:      ", updated_samples)

                else:
                    if updated_samples[i] > right_prob and updated_samples[i] < left_prob:
                        right_samp_cross_array = np.append(
                            right_samp_cross_array, updated_samples[i])
                        array_num_samples_right = np.append(
                            array_num_samples_right, 1)
                        array_num_samples_left = np.append(
                            array_num_samples_left, 0)
                        num_samples = num_samples - 1
                        print("i:      ", i)
                        print("crossed right side:      ", updated_samples[i])
                        updated_samples = np.delete(updated_samples, i, axis=0)
                        print("updated_sample:      ", updated_samples)
                        break
                    elif updated_samples[i] > left_prob and updated_samples[i] < right_prob:
                        left_samp_cross_array = np.append(
                            left_samp_cross_array, updated_samples[i])
                        array_num_samples_left = np.append(
                            array_num_samples_left, 1)
                        array_num_samples_right = np.append(
                            array_num_samples_right, 0)
                        num_samples = num_samples - 1
                        print("i:      ", i)
                        print("crossed left side:      ", updated_samples[i])
                        updated_samples = np.delete(updated_samples, i, axis=0)
                        print("updated_sample:      ", updated_samples)
                        break
                    else:
                        array_num_samples_right = np.append(
                            array_num_samples_right, 0)
                        array_num_samples_left = np.append(
                            array_num_samples_left, 0)
                        print("sample to be recreated:        ",
                              updated_samples[i])
                        updated_samples[i] = np.random.rand(1).round(3)
                        print(
                            "new sample for _samples_array[i] > left_prob and updated_samples[i] > right_prob:     ", updated_samples[i])
                        print("updated_sample:      ", updated_samples)
        
        left_samp_cross_array = np.transpose(left_samp_cross_array)
        right_samp_cross_array = np.transpose(right_samp_cross_array)

        print("array with left side number of samples:          ",
              array_num_samples_left)
        print("array with right side number of samples:          ",
              array_num_samples_right)
        print("samples that have crossed to the left side:          ",
              left_samp_cross_array)
        print("samples that have crossed to the right side:          ",
              right_samp_cross_array)

        return array_num_samples_right, array_num_samples_left


initial_num_samples = int(input('Choose an initial number of samples:   '))
d_1d_1way = One_d_discr(initial_num_samples)
array_of_crossed = d_1d_1way.n_neutrons_cross(initial_num_samples)
print("return of class:     ", array_of_crossed)
