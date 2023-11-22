import sys
sys.path.append('../')
from homogenization.hmg_fission import macro_cs_fission
from homogenization.hmg_gamma import macro_cs_gamma_fuel, macro_gamma_Fe
from homogenization.hmg_scattering import macro_scattering_Fe
from parameters import *
# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns


class Random_array:
    def __init__(self, num_samples):
        self.num_samples = num_samples

    def random(self, num_samples):
        self.num_samples = num_samples
        r_samples_array = np.random.rand(num_samples).round(3)
        return r_samples_array


class Probability:
    def __init__(self, num_samples, tt_cross_section, row, column, r_array):
        self.num_samples = num_samples
        self.tt_cross_section = tt_cross_section
        self.row = row
        self.column = column
        self.r_array = r_array

    def probab(self, num_samples, tt_cross_section, row, column, r_array):
        self.num_samples = num_samples
        self.tt_cross_section = tt_cross_section
        self.row = row
        self.column = column
        self.r_array = r_array
        prob_matrix = np.zeros((len(row), len(column)))
        i = 0
        while i < len(r_array):
            r = 0
            while r < len(row):
                c = 0
                while c < len(column):
                    if i < len(r_array):
                        if r_array[i] != 1:
                            dist_to_collision = - \
                                np.log(1 - r_array[i]) / tt_cross_section
                            prob_matrix[r][c] = round(dist_to_collision,4)
                        else:
                            while i < len(r_array) and r_array[i] == 1:
                                r_array[i] = round(np.random.rand(), 3)
                                i += 1
                                if i < len(r_array):
                                    dist_to_collision = - \
                                        np.log(1 - r_array[i]) / \
                                        tt_cross_section
                                    prob_matrix[r][c] = round(dist_to_collision,4)
                    i += 1
                    c += 1
                r += 1
        matrix_corners = np.zeros((len(row) + 2, len(column) + 2))
        matrix_corners[1:len(row)+1, 1:len(column)+1] = prob_matrix
        # print("prob matrix", prob_matrix)
        print("matrix_prob", matrix_corners)
        return matrix_corners

class Distance:
    def __init__(self, row, column ):
        self.row = row
        self.column = column
        
    def dist(self,row,column):
        self.row = row
        self.column = column
        half_row = ((len(row))+1) // 2
        half_col = ((len(column))+1) // 2
        distance_matrix =  np.zeros((len(row), len(column)))
        for i in range(len(row)):
            for j in range(len(column)):
                distance_matrix[i][j] = round(np.sqrt((i + 1 - half_row)**2 + (j + 1 - half_col)**2), 3)
        final_dist_matrix = np.zeros((len(row) + 2, len(column) + 2))
        final_dist_matrix[1:len(row)+1, 1:len(column)+1] = distance_matrix
        print("final", final_dist_matrix)
        return final_dist_matrix

class Two_dimensions:
    def __init__(self, row, column, prob_matrix, initial_neutrons):
        self.row = row
        self.column = column
        self.prob_matrix = prob_matrix
        self.initial_neutrons = initial_neutrons

    def quadrants(self, row, column, prob_matrix, initial_neutrons):
        self.row = row
        self.column = column
        self.initial_neutrons = initial_neutrons
        self.prob_matrix = prob_matrix
        cross_amount_matrix = np.zeros(((len(row)+2), (len(column)+2)))
        aux_matrix = np.zeros((3, 3))
        half_row = (len(row) + 2) // 2
        half_col = (len(column) + 2) // 2
        neutrons = initial_neutrons
        distance = Distance(row, column)
        dist_matrix = distance.dist(row, column)

        # Part 1 
        aux_array = [1, 0, 2]
        aux_array2 = [1, 2, 0]
        cross_amount_matrix[half_row][half_col] = neutrons/4
        hc = half_col
        while hc >= 0:
            hr = half_row
            while hr >= 0:
                center_aux_array2_r = [hr, hr + 1, hr - 1]
                center_aux_array_c = [hc, hc + 1, hc - 1]
                center_aux_array2_c = [hc, hc - 1]
                aux_matrix = np.zeros((3, 3))
                i = 0
                while i < 3:
                    j = 0
                    while j < 3:
                        # Verificar limites da matriz
                        if (
                            center_aux_array2_r[i] >= 0
                            and center_aux_array2_r[i] <= len(prob_matrix)
                            and center_aux_array_c[j] >= 0
                            and center_aux_array_c[j] <= len(prob_matrix[0])
                        ):
                            aux_matrix[aux_array[i]][aux_array[j]] = prob_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]
                            if not np.all(aux_matrix == 0):
                                if aux_matrix[aux_array[i]][aux_array2[j]] >= dist_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]:
                                    neutrons_part = 0
                                    if(hr-1<len(row) and hc-1<len(column)):
                                        neutrons_part = cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] / 9
                                        cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] = round(cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] * 1/9, 0)
                                        for t in range(2):
                                            for k in range(2):
                                                if (
                                                    center_aux_array2_r[t] < len(cross_amount_matrix)
                                                    and center_aux_array_c[k] < len(cross_amount_matrix[0])
                                                ):
                                                    cross_amount_matrix[center_aux_array2_r[t]][center_aux_array_c[k]] += round(neutrons_part, 0)
                            elif hr == 0 or hr == len(row) - 1 or hc == 0 or hc == len(column) - 1:
                                prob_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] = 0
                            print("cross amount", cross_amount_matrix)

                        j = j + 1
                    i = i + 1
                hr = hr - 1
            hc = hc - 1
            
        # Part 2 
        aux_array = [1, 0, 2]
        aux_array2 = [1, 2, 0]
        cross_amount_matrix[half_row][half_col] = neutrons/4
        hc = half_col
        while hc <= len(column):
            hr = half_row
            while hr >= 0:
                center_aux_array2_r = [hr, hr + 1, hr - 1]
                center_aux_array_c = [hc, hc + 1, hc - 1]
                aux_matrix = np.zeros((3, 3))
                i = 0
                while i < 3:
                    j = 0
                    while j < 3:
                        # Verificar limites da matriz
                        if (
                            center_aux_array2_r[i] >= 0
                            and center_aux_array2_r[i] <= len(prob_matrix)
                            and center_aux_array_c[j] >= 0
                            and center_aux_array_c[j] <= len(prob_matrix[0])
                        ):
                            aux_matrix[aux_array[i]][aux_array[j]] = prob_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]
                            if not np.all(aux_matrix == 0):
                                if aux_matrix[aux_array[i]][aux_array2[j]] >= dist_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]:
                                    neutrons_part = 0
                                    if(hr-1<len(row) and hc+1>0):
                                        neutrons_part = cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] / 9
                                        cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] = round(cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] * 1/9, 0)
                                        for t in range(2):
                                            for k in range(2):
                                                if (
                                                    center_aux_array2_r[t] < len(cross_amount_matrix)
                                                    and center_aux_array_c[k] < len(cross_amount_matrix[0])
                                                ):
                                                    cross_amount_matrix[center_aux_array2_r[t]][center_aux_array_c[k]] += round(neutrons_part, 0)
                            elif hr == 0 or hr == len(row) - 1 or hc == 0 or hc == len(column) - 1:
                                prob_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] = 0
                            print("cross amount", cross_amount_matrix)

                        j = j + 1
                    i = i + 1
                hr = hr - 1
            hc = hc + 1
            
        # Part 3 
        aux_array = [1, 0, 2]
        aux_array2 = [1, 2, 0]
        cross_amount_matrix[half_row][half_col] = neutrons/4
        hc = half_col
        while hc >= 0:
            hr = half_row
            while hr <= len(row):
                center_aux_array2_r = [hr, hr + 1, hr - 1]
                center_aux_array_c = [hc, hc + 1, hc - 1]
                aux_matrix = np.zeros((3, 3))
                i = 0
                while i < 3:
                    j = 0
                    while j < 3:
                        # Verificar limites da matriz
                        if (
                            center_aux_array2_r[i] >= 0
                            and center_aux_array2_r[i] <= len(prob_matrix)
                            and center_aux_array_c[j] >= 0
                            and center_aux_array_c[j] <= len(prob_matrix[0])
                        ):
                            aux_matrix[aux_array[i]][aux_array[j]] = prob_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]
                            if not np.all(aux_matrix == 0):
                                if aux_matrix[aux_array[i]][aux_array2[j]] >= dist_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]:
                                    neutrons_part = 0
                                    if(hr-1<len(row) and hc+1>0):
                                        neutrons_part = cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] / 9
                                        cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] = round(cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] * 1/9, 0)
                                        for t in range(2):
                                            for k in range(2):
                                                if (
                                                    center_aux_array2_r[t] < len(cross_amount_matrix)
                                                    and center_aux_array_c[k] < len(cross_amount_matrix[0])
                                                ):
                                                    cross_amount_matrix[center_aux_array2_r[t]][center_aux_array_c[k]] += round(neutrons_part, 0)
                            elif hr == 0 or hr == len(row) - 1 or hc == 0 or hc == len(column) - 1:
                                prob_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] = 0
                            print("cross amount", cross_amount_matrix)

                        j = j + 1
                    i = i + 1
                hr = hr + 1
            hc = hc - 1
            
        # Part 4
        aux_array = [1, 0, 2]
        aux_array2 = [1, 2, 0]
        cross_amount_matrix[half_row][half_col] = neutrons/4
        hc = half_col
        while hc <= len(column):
            hr = half_row
            while hr <= len(row):
                center_aux_array2_r = [hr, hr + 1, hr - 1]
                center_aux_array_c = [hc, hc + 1, hc - 1]
                aux_matrix = np.zeros((3, 3))
                i = 0
                while i < 3:
                    j = 0
                    while j < 3:
                        # Verificar limites da matriz
                        if (
                            center_aux_array2_r[i] >= 0
                            and center_aux_array2_r[i] <= len(prob_matrix)
                            and center_aux_array_c[j] >= 0
                            and center_aux_array_c[j] <= len(prob_matrix[0])
                        ):
                            aux_matrix[aux_array[i]][aux_array[j]] = prob_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]
                            if not np.all(aux_matrix == 0):
                                if aux_matrix[aux_array[i]][aux_array2[j]] >= dist_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]:
                                    neutrons_part = 0
                                    if(hr-1<len(row) and hc+1>0):
                                        neutrons_part = cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] / 9
                                        cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] = round(cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] * 1/9, 0)
                                        for t in range(2):
                                            for k in range(2):
                                                if (
                                                    center_aux_array2_r[t] < len(cross_amount_matrix)
                                                    and center_aux_array_c[k] < len(cross_amount_matrix[0])
                                                ):
                                                    cross_amount_matrix[center_aux_array2_r[t]][center_aux_array_c[k]] += round(neutrons_part, 0)
                            elif hr == 0 or hr == len(row) - 1 or hc == 0 or hc == len(column) - 1:
                                prob_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] = 0
                            print("cross amount", cross_amount_matrix)

                        j = j + 1
                    i = i + 1
                hr = hr + 1
            hc = hc + 1



micro_scattering_U235 = 15.04 * 10 ** (-24)
micro_scattering_U238 = 9.360 * 10 ** (-24)
micro_scattering_O = 3.780 * 10 ** (-24)

macro_scattering_U235 = micro_scattering_U235 * n_U235
macro_scattering_U238 = micro_scattering_U238 * n_U238
macro_scattering_O = micro_scattering_O * n_O

macro_cs_UO2_scattering = (macro_scattering_U235 + macro_scattering_U238 +
                           macro_scattering_O)*(tt_vol_UO2) / tt_act_core_vol

macro_cs_UO2_absorption = macro_cs_gamma_fuel + macro_cs_fission


macro_tt_UO2 = macro_cs_UO2_scattering + macro_cs_UO2_absorption


macro_cs_Fe_absorption = macro_gamma_Fe
macro_tt_Fe = macro_cs_Fe_absorption + macro_scattering_Fe

max_dist = 1/macro_tt_UO2


initial_neutrons = int(input("Choose initial number of neutrons:    "))
rowcol = int(input("Choose your matrix dimension:     "))

rowcol_array = np.array([])
column = np.array([])
row = np.array([])
for x in range(rowcol):
    column = np.append(column, int(x+1))
    row = np.append(row, int(x+1))


obj = Random_array(initial_neutrons)
r_array_result = obj.random(initial_neutrons)
item = Probability(initial_neutrons, macro_tt_UO2, row, column, r_array_result)
prob_matrix = item.probab(
    initial_neutrons, macro_tt_UO2, row, column, r_array_result)
aux = Two_dimensions(row, column, prob_matrix, initial_neutrons)
cross_amount_matrix = aux.quadrants(
    row, column, prob_matrix, initial_neutrons)



# sns.heatmap(cross_amount_matrix, annot=True, cmap="viridis")
# plt.show()

