import numpy as np

class One_d_discr_one:
    def __init__(self, num_samples, discretizations):
        self.num_samples = num_samples
        self.discretizations = discretizations

    def n_neutrons_cross(self, num_samples, discretizations):
        self.num_samples = num_samples
        cant_cross_amount = np.array([])
        left_amount = np.array([])
        right_amount = np.array([])
        tt_amount = np.array([])
        cant_cross_array = np.array([])
        left_array = np.array([])
        right_array = np.array([])
        cross_matrix = np.zeros((1, num_samples))
        r_samples_array = np.random.rand(num_samples).round(3)
        auxx = discretizations * 2
        cross_prob_array = np.random.rand(auxx).round(3)
        left_prob_array = np.array([0.2, 0.95])
        right_prob_array = np.array([0.1, 0.2])
        
        for i in range(auxx):
            if (i % 2) == 0:
                left_prob_array = np.append(left_prob_array, cross_prob_array[i])
            else:
                right_prob_array = np.append(right_prob_array, cross_prob_array[i])
        
        aux_array = r_samples_array
        for i in range(num_samples):
            discretizations = self.discretizations
            right_prob = 0.2
            left_prob = 0.1
            prob_else = True
            
            while prob_else:
                if len(left_amount) != 0:
                    if left_prob > aux_array[i] > right_prob:
                        aux = right_amount[-1] + 1
                        right_amount = np.append(right_amount, aux)
                        right_array = np.append(right_array, aux_array[i])
                        left_amount = np.append(left_amount, left_amount[-1])
                        left_array = np.append(left_array, 0.000)
                        cant_cross_amount = np.append(cant_cross_amount, cant_cross_amount[-1])
                        cant_cross_array = np.append(cant_cross_array, 0.000)
                        prob_else = False
                    elif left_prob < aux_array[i] < right_prob:
                        aux = left_amount[-1] + 1
                        left_amount = np.append(left_amount, aux)
                        left_array = np.append(left_array, aux_array[i])
                        right_amount = np.append(right_amount, right_amount[-1])
                        right_array = np.append(right_array, 0.000)
                        cant_cross_amount = np.append(cant_cross_amount, cant_cross_amount[-1])
                        cant_cross_array = np.append(cant_cross_array, 0.000)
                        prob_else = False
                    elif left_prob > aux_array[i] and right_prob > aux_array[i]:
                        aux = cant_cross_amount[-1] + 1
                        cant_cross_amount = np.append(cant_cross_amount, aux)
                        cant_cross_array = np.append(cant_cross_array, aux_array[i])
                        left_amount = np.append(left_amount, left_amount[-1])
                        left_array = np.append(left_array, 0.000)
                        right_amount = np.append(right_amount, right_amount[-1])
                        right_array = np.append(right_array, 0.000)
                        aux_array[i] = 0
                        prob_else = False
                    else:
                        cross_prob_array = np.random.rand(2).round(3)
                        left_prob = cross_prob_array[0]
                        right_prob = cross_prob_array[1]
                        prob_else = True
                else:
                    if left_prob > aux_array[i] > right_prob:
                        right_amount = np.append(right_amount, 1)
                        right_prob_array = np.append(right_prob_array, aux_array[0])
                        right_array = np.append(right_array, aux_array[i])
                        left_amount = np.append(left_amount, 0)
                        left_array = np.append(left_array, 0.000)
                        cant_cross_amount = np.append(cant_cross_amount, 0)
                        cant_cross_array = np.append(cant_cross_array, 0.000)
                        prob_else = False
                    elif left_prob < aux_array[i] < right_prob:
                        left_amount = np.append(left_amount, 1)
                        left_array = np.append(left_array, aux_array[0])
                        right_amount = np.append(right_amount, 0)
                        right_array = np.append(right_array, 0.000)
                        cant_cross_amount = np.append(cant_cross_amount, 0)
                        cant_cross_array = np.append(cant_cross_array, 0.000)
                        prob_else = False
                    elif left_prob > aux_array[i] and right_prob > aux_array[i]:
                        cant_cross_amount = np.append(cant_cross_amount, 1)
                        cant_cross_array = np.append(cant_cross_array, aux_array[0])
                        left_amount = np.append(left_amount, 0)
                        left_array = np.append(left_array, 0.000)
                        right_amount = np.append(right_amount, 0)
                        right_array = np.append(right_array, 0.000)
                        aux_array[i] = 0
                        prob_else = False
                    else:
                        cross_prob_array = np.random.rand(2).round(3)
                        left_prob = cross_prob_array[0]
                        right_prob = cross_prob_array[1]
                        prob_else = True
        
        return cross_matrix

# calling class
initial_num_samples = int(input('Choose an initial number of samples: '))
initial_num_discr = int(input('Choose an initial number of discretizations: '))
aux = One_d_discr_one(initial_num_samples, initial_num_discr)
cross_matrix = aux.n_neutrons_cross(initial_num_samples, initial_num_discr)
