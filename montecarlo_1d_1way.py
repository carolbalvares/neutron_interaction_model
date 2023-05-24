import numpy as np

# creating class


class One_d_discr:
    def __init__(self, num_samples):
        self.num_samples = num_samples

    def n_neutrons_cross(self, num_samples):
        self.num_samples = num_samples
        cant_cross_amount = np.array([])
        cross_amount = np.array([])
        r_samples_array = np.random.rand(num_samples).round(3)
        cross_prob = np.random.rand(1).round(3)
        print(r_samples_array)
        print(cross_prob)
        for i in range(num_samples):
            if (len(cross_amount) != 0):
                if r_samples_array[i] >= cross_prob:
                    aux = cross_amount[-1] + 1
                    cross_amount = np.append(
                        cross_amount, aux)
                    cant_cross_amount = np.append(
                        cant_cross_amount, cant_cross_amount[-1])
                    num_samples = num_samples - 1
                else:
                    aux = cant_cross_amount[-1] + 1
                    cant_cross_amount = np.append(
                        cant_cross_amount, aux)
                    cross_amount = np.append(cross_amount, cross_amount[-1])
                    num_samples = num_samples - 1
            else:
                if r_samples_array[i] >= cross_prob:
                    aux = 1
                    cross_amount = np.append(
                        cross_amount, aux)
                    cant_cross_amount = np.append(cant_cross_amount, 0)
                    num_samples = num_samples - 1
                else:
                    aux = 1
                    cant_cross_amount = np.append(
                        cant_cross_amount, aux)
                    num_samples = num_samples - 1
                    cross_amount = np.append(cross_amount, 0)
        return cross_amount, cant_cross_amount


# calling class
initial_num_samples = int(input('Choose a initial number of samples:   '))
aux = One_d_discr(initial_num_samples)
can_cross, cant_cross = aux.n_neutrons_cross(initial_num_samples)
print("cant cross:   ", cant_cross)
print("can cross:    ", can_cross)

total_int = range(len(cant_cross))
aux = np.array(total_int)
total_int = aux + 1
print("total interections:   ", total_int)
