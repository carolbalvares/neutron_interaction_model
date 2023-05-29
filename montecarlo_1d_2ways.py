import numpy as np


class One_d_discr:
    def __init__(self, num_samples):
        self.num_samples = num_samples

    def n_neutrons_cross(self, num_samples):
        right_samp = np.array([])
        left_samp = np.array([])
        dont_cross_samp = np.array([])
        amount_samples_left = np.array([])
        amount_samples_right = np.array([])
        amount_samples_dont_cross = np.array([])
        aux = 0
        auxx = np.array([])
        r_samples = np.random.rand(num_samples).round(3)
        updated_samples = np.array([])
        updated_samples = r_samples
        print("random samples array:          ", r_samples)
        r_prob = np.random.rand(2).round(3)
        right_prob = r_prob[0]
        left_prob = r_prob[1]
        print("right prob:          ", right_prob)
        print("left prob:          ", left_prob)
        while num_samples != 0:
            if num_samples == 0:
                break
            for i in range(len(updated_samples)-1, -1, -1):
                if len(amount_samples_left) != 0 or len(amount_samples_right) != 0:
                    # 2nd case
                    if updated_samples[i] > right_prob and updated_samples[i] < left_prob:
                        right_samp = np.append(
                            right_samp, updated_samples[i])
                        aux = amount_samples_right[-1] + 1
                        amount_samples_right = np.append(
                            amount_samples_right, aux)
                        amount_samples_left = np.append(
                            amount_samples_left, amount_samples_left[-1])
                        amount_samples_dont_cross = np.append(
                            amount_samples_dont_cross, amount_samples_dont_cross[-1])
                        num_samples = num_samples - 1
                        print("crossed right side:      ", updated_samples[i])
                        updated_samples = np.delete(updated_samples, i, axis=0)
                        print("updated_sample:      ", updated_samples)
                        break
                    # 1st case
                    elif updated_samples[i] > left_prob and updated_samples[i] < right_prob:
                        left_samp = np.append(
                            left_samp, updated_samples[i])
                        aux = amount_samples_left[-1]+1
                        amount_samples_left = np.append(
                            amount_samples_left, aux)
                        amount_samples_right = np.append(
                            amount_samples_right, amount_samples_right[-1])
                        amount_samples_dont_cross = np.append(
                            amount_samples_dont_cross, amount_samples_dont_cross[-1])
                        num_samples = num_samples - 1
                        print("crossed left side:      ", updated_samples[i])
                        updated_samples = np.delete(updated_samples, i, axis=0)
                        print("updated_sample:      ", updated_samples)
                        break
                    # 4th case
                    elif updated_samples[i] < left_prob and updated_samples[i] < right_prob:
                        dont_cross_samp = np.append(
                            dont_cross_samp, updated_samples[i])
                        aux = amount_samples_dont_cross[-1]+1
                        amount_samples_dont_cross = np.append(
                            amount_samples_dont_cross, aux)
                        amount_samples_left = np.append(
                            amount_samples_left, amount_samples_left[-1])
                        amount_samples_right = np.append(
                            amount_samples_right, amount_samples_right[-1])
                        num_samples = num_samples - 1
                        print("crossed left side:      ", updated_samples[i])
                        updated_samples = np.delete(updated_samples, i, axis=0)
                        print("updated_sample:      ", updated_samples)
                        break
                    #else:
                        # amount_samples_right = np.append(
                        #     amount_samples_right, amount_samples_right[-1])
                        # amount_samples_left = np.append(
                        #     amount_samples_left, amount_samples_left[-1])
                        # amount_samples_dont_cross = np.append(
                        #     amount_samples_dont_cross, amount_samples_dont_cross[-1])
                        # r_prob = np.random.rand(2).round(3)
                        # right_prob = r_prob[0]
                        # left_prob = r_prob[1]
                        # print("right prob:          ", right_prob)
                        # print("left prob:          ", left_prob)
                    else:
                        auxx = np.append(
                            dont_cross_samp, updated_samples[i])
                        amount_samples_dont_cross = np.append(
                            amount_samples_dont_cross, amount_samples_dont_cross[-1])
                        amount_samples_left = np.append(
                            amount_samples_left, amount_samples_left[-1])
                        amount_samples_right = np.append(
                            amount_samples_right, amount_samples_right[-1])
                else:
                    if updated_samples[0] > right_prob and updated_samples[0] < left_prob:
                        right_samp = np.append(
                            right_samp, updated_samples[i])
                        amount_samples_right = np.append(
                            amount_samples_right, 1)
                        amount_samples_left = np.append(
                            amount_samples_left, 0)
                        amount_samples_dont_cross = np.append(
                            amount_samples_dont_cross, 0)
                        num_samples = num_samples - 1
                        print("crossed right side:      ", updated_samples[0])
                        updated_samples = np.delete(updated_samples, i, axis=0)
                        print("updated_sample:      ", updated_samples)
                        break
                    # 1st case
                    elif updated_samples[0] > left_prob and updated_samples[0] < right_prob:
                        left_samp = np.append(
                            left_samp, updated_samples[0])
                        amount_samples_left = np.append(
                            amount_samples_left, 1)
                        amount_samples_right = np.append(
                            amount_samples_right, amount_samples_right[-1])
                        amount_samples_dont_cross = np.append(
                            amount_samples_dont_cross, amount_samples_dont_cross[-1])
                        num_samples = num_samples - 1
                        print("crossed left side:      ", updated_samples[i])
                        updated_samples = np.delete(updated_samples, i, axis=0)
                        print("updated_sample:      ", updated_samples)
                        break
                    # 4th case
                    elif updated_samples[i] < left_prob and updated_samples[i] < right_prob:
                        dont_cross_samp = np.append(
                            dont_cross_samp, updated_samples[i])
                        aux = amount_samples_dont_cross[-1]+1
                        amount_samples_dont_cross = np.append(
                            amount_samples_dont_cross, aux)
                        amount_samples_left = np.append(
                            amount_samples_left, amount_samples_left[-1])
                        amount_samples_right = np.append(
                            amount_samples_right, amount_samples_right[-1])
                        num_samples = num_samples - 1
                        print("crossed left side:      ", updated_samples[i])
                        updated_samples = np.delete(updated_samples, i, axis=0)
                        print("updated_sample:      ", updated_samples)
                        break

        left_samp = np.transpose(left_samp)
        right_samp = np.transpose(right_samp)

        print("array with left side number of samples:          ",
              amount_samples_left)
        print("array with right side number of samples:          ",
              amount_samples_right)
        print("samples that have crossed to the left side:          ",
              left_samp)
        print("samples that have crossed to the right side:          ",
              right_samp)

        return amount_samples_right, amount_samples_left


initial_num_samples = int(input('Choose an initial number of samples:   '))
d_1d_1way = One_d_discr(initial_num_samples)
# array_of_crossed = d_1d_1way.n_neutrons_cross(initial_num_samples)
# print("return of class:     ", array_of_crossed)

qt_right, qt_left = d_1d_1way.n_neutrons_cross(initial_num_samples)
total_int = range(len(qt_left))
aux = np.array(total_int)
total_int = aux + 1
print("total interections:   ", total_int)
