import numpy as np


#creating class
class One_d_discr_one:
    def __init__(self, num_samples, discretizations):
        self.num_samples = num_samples
        self.discretizations = discretizations

    def n_neutrons_cross(self, num_samples, discretizations):
        self.discretizations = discretizations
        self.num_samples = num_samples
        cant_cross_amount = np.array([])
        cross_amount = np.array([])
        cant_cross_array = np.array([])
        cross_array = np.array([])
        cross_matrix = np.matrix([])
        r_samples_array = np.random.rand(num_samples).round(3)
        cross_prob_array = np.random.rand(discretizations).round(3)
        print("samples array:   ", r_samples_array)
        print("probability array:     ", cross_prob_array)
        aux_array = r_samples_array
        # initial_discretizations = discretizations
        for e in range(discretizations):
            for i in range(num_samples):
                if len(cant_cross_amount) != 0:
                    if cross_prob_array[e] > aux_array[i]:
                        aux = cant_cross_amount[-1] + 1
                        cant_cross_amount = np.append(cant_cross_amount, aux)
                        cant_cross_array = np.append(
                            cant_cross_array, aux_array[i])
                        cross_amount = np.append(
                            cross_amount, cross_amount[-1])
                        cross_array = np.append(
                            cross_array, 0.000
                        )
                        print("sample:", aux_array[i])
                        print("probability of crossing:", cross_prob_array[e])
                        print("cant cross array:  ", cant_cross_array)
                        print("amount that didnt crossed:   ", cant_cross_amount)
                        print("can cross array:  ", cross_array)
                        print("amount that crossed:   ", cross_amount)

                        num_samples = num_samples - 1
                        
                    else:
                        aux = cross_amount[-1] + 1
                        cross_amount = np.append(cross_amount, aux)
                        cross_array = np.append(cross_array, aux_array[i])
                        cant_cross_amount = np.append(
                            cant_cross_amount, cant_cross_amount[-1])
                        cant_cross_array = np.append(
                            cant_cross_array, 0.000
                        )
                        print("sample:", aux_array[i])
                        print("probability of crossing:", cross_prob_array[e])
                        print("cant cross array:  ", cant_cross_array)
                        print("amount that didnt crossed:   ", cant_cross_amount)
                        print("can cross array:  ", cross_array)
                        print("amount that crossed:   ", cross_amount)

                        num_samples = num_samples - 1
                        
                else:
                    if cross_prob_array[e] > aux_array[i]:
                        cant_cross_amount = np.append(cant_cross_amount, 1)
                        cant_cross_array = np.append(
                            cant_cross_array, aux_array[0])
                        cross_amount = np.append(cross_amount, 0)
                        cross_array = np.append(
                            cross_array, 0.000
                        )
                        print("sample:", aux_array[i])
                        print("probability of crossing:", cross_prob_array[e])
                        print("cant cross array:  ", cant_cross_array)
                        print("amount that didnt crossed:   ", cant_cross_amount)
                        print("can cross array:  ", cross_array)
                        print("amount that crossed:   ", cross_amount)

                        num_samples = num_samples - 1
                        

                    else:
                        cross_amount = np.append(cross_amount, 1)
                        cross_array = np.append(cross_array, aux_array[i])
                        cant_cross_amount = np.append(
                            cant_cross_amount, 0)
                        cant_cross_array = np.append(
                            cant_cross_array, 0.000
                        )
                        print("sample:", aux_array[i])
                        print("probability of crossing:", cross_prob_array[e])
                        print("cant cross array:  ", cant_cross_array)
                        print("amount that didnt crossed:   ", cant_cross_amount)
                        print("can cross array:  ", cross_array)
                        print("amount that crossed:   ", cross_amount)
                        num_samples = num_samples - 1
                        
            aux_array=cross_array
            print("aux array pos a analise de todas samples:    ",aux_array)
            num_samples = len(cross_array)
            discretizations = discretizations - 1
        
        #incrementing matrix soon 
            # cross_matrix = np.vstack([cross_matrix, cross_array])
            # print("matrix: ",cross_matrix)  # Decrementa a variável auxiliar
        return cross_amount, cant_cross_amount


# calling class
initial_num_samples = int(input('Choose a initial number of samples:   '))
initial_num_discr = int(input('Choose a initial number of discretization:   '))
aux = One_d_discr_one(initial_num_samples, initial_num_discr)
can_cross, cant_cross = aux.n_neutrons_cross(
    initial_num_samples, initial_num_discr)
print("cant cross:   ", cant_cross)
print("can cross:    ", can_cross)

# total_int = range(len(cant_cross))
# aux = np.array(total_int)
# total_int = aux + 1
# print("total interections:   ", total_int)
