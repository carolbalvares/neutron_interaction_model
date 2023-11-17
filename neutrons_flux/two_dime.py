import sys
sys.path.append('../')
from homogenization.hmg_fission import macro_cs_fission
from homogenization.hmg_gamma import macro_cs_gamma_fuel, macro_gamma_Fe
from homogenization.hmg_scattering import macro_scattering_Fe
from parameters import *
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


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
        print("matrix_corners", matrix_corners)
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
        print("dist", distance_matrix)
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
        distance = Distance(row,column)
        dist_matrix = distance.dist(row,column)
        # Part 1 - First Quadrant
        aux_array = [1, 0, 2]
        aux_array2 = [1, 2, 0]
        cross_amount_matrix[half_row][half_col]=neutrons
        hc = half_col
        while hc >= 0: 
            hr = half_row 
            while hr >= 0:
                    center_aux_array2_r = [hr, hr - 1]
                    center_aux_array_c = [hc, hc+1]
                    center_aux_array2_c = [hc, hc - 1]
                    ii = [hr-1, hr, hr - 1]
                    jj = [hc-1, hc, hc+1]
                    ########### first quadrant ##############
                    i = 0
                    while i < 2:
                        j = 0
                        while j < 2:
                                aux_matrix[aux_array[i]][aux_array2[j]] = prob_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]
                                if i!= len(row) or j!= len(column) or i!= 0 or j!=0:
                                    if aux_matrix[i][j] >= dist_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]:
                                                neutrons_part = 0
                                                array_neutrons = [0,1,-1]
                                                array_neutrons2 = [-1,0,1]
                                                neutrons_part =  cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]/9
                                                cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] = round(cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]*1/9,0)
                                                for t in range(3):
                                                    for k in range(3):
                                                        if ii[t] < len(cross_amount_matrix) and jj[k] < len(cross_amount_matrix[0]):  
                                                            ####mudar o nome da variavel ou uniformizar e tratar as corners de outra maneira
                                                            cross_amount_matrix[ii[t]][jj[k]] += round(neutrons_part, 0)
                                    print(cross_amount_matrix)
                                else: 
                                    print("ops")
                                
                                j = j + 1
                        i = i + 1
                    
                    ########### second quadrant ##############
                    total_neutrons_part = 0
                    i = 0
                    while i < 2:
                        j = 0
                        while j < 2:
                            aux_matrix[aux_array[i]][aux_array[j]] = prob_matrix[center_aux_array2_r[-i]][center_aux_array2_c[j]]
                            if i!= len(row) or j!= len(column) or i!= 0 or j!=0:
                                if aux_matrix[i][j] >= dist_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]:
                                            neutrons_part = 0
                                            array_neutrons = [0,1,-1]
                                            array_neutrons2 = [-1,0,1]
                                            neutrons_part =  cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]/9
                                            cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] = round(cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]*1/9,0)
                                            for t in range(3):
                                                for k in range(3):
                                                    if ii[t] < len(cross_amount_matrix) and jj[k] < len(cross_amount_matrix[0]):  
                                                        ####mudar o nome da variavel ou uniformizar e tratar as corners de outra maneira
                                                        cross_amount_matrix[ii[t]][jj[k]] += round(neutrons_part, 0)
                                print(cross_amount_matrix)
                            else: 
                                    print("ops")
                            
                            j = j + 1
                        i = i + 1
                    
                    ########### third and fourth quadrant ##############
                    row_aux_array3 = [0, 1, 2]
                    column_aux_array3 = [hc - 1, hc, hc+1]
                    i = 0
                    auxx = hr+1
                    while auxx != len(row):
                        
                        while i <= 2:
                            aux_matrix[2][row_aux_array3[i]] = prob_matrix[auxx][column_aux_array3[i]]
                            if aux_matrix[2][row_aux_array3[i]] >=dist_matrix[auxx][column_aux_array3[i]]:
                                    cross_amount_matrix[auxx][column_aux_array3[i]] += 1
                            i = i + 1
                        auxx = auxx+1     
                               
                    # print("aux matriz 1", aux_matrix)
                    # print("cross_matrix", cross_amount_matrix)
                    # aux_matrix[1][1] = neutrons
                    # div_neutrons = np.floor(neutrons/8)
  
                    hr = hr - 1
            hc = hc - 1
       
       
        aux_array = [1, 0, 2]
        aux_array2 = [2, 1, 0]
        hc = half_col + 1
        while hc < len(column): 
            hr = half_row 
            while hr < len(row):
                    center_aux_array2_r = [hr, hr - 1]
                    center_aux_array_c = [hc-1, hc]
                    center_aux_array2_c = [hc, hc - 1]
                    ########### first quadrant ##############
                    i = 0
                    while i < 2:
                        j = 0
                        while j < 2:
                            if hc + 1> len(column) or hr + 1 > len(row):
                                aux_matrix[aux_array[i]][aux_array2[j]]= 0
                            else:
                                aux_matrix[aux_array[i]][aux_array2[j]] = prob_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]
                                if i!= len(row) or j!= len(column) or i!= 0 or j!=0:
                                    if aux_matrix[i][j] >= dist_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]:
                                                neutrons_part = 0
                                                array_neutrons = [0,1,-1]
                                                array_neutrons2 = [-1,0,1]
                                                neutrons_part =  cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]/9
                                                cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] = round(cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]*1/9,0)
                                                for t in range(3):
                                                    for k in range(3):
                                                        if ii[t] < len(cross_amount_matrix) and jj[k] < len(cross_amount_matrix[0]):  
                                                            ####mudar o nome da variavel ou uniformizar e tratar as corners de outra maneira
                                                            cross_amount_matrix[ii[t]][jj[k]] += round(neutrons_part, 0)
                                    print(cross_amount_matrix)
                                else: 
                                    print("ops")
                                
                            j = j + 1
                        i = i + 1
                    ########### second quadrant ##############
                    i = 0
                    while i < 2:
                        j = 0
                        while j < 2:
                            aux_matrix[aux_array[i]][aux_array[j]] = prob_matrix[center_aux_array2_r[-i]][center_aux_array2_c[j]]
                            if i!= len(row) or j!= len(column) or i!= 0 or j!=0:
                                if aux_matrix[i][j] >= dist_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]:
                                            neutrons_part = 0
                                            array_neutrons = [0,1,-1]
                                            array_neutrons2 = [-1,0,1]
                                            neutrons_part =  cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]/9
                                            cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] = round(cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]*1/9,0)
                                            for t in range(3):
                                                for k in range(3):
                                                    if ii[t] < len(cross_amount_matrix) and jj[k] < len(cross_amount_matrix[0]):  
                                                        ####mudar o nome da variavel ou uniformizar e tratar as corners de outra maneira
                                                        cross_amount_matrix[ii[t]][jj[k]] += round(neutrons_part, 0)
                                print(cross_amount_matrix)
                            else: 
                                    print("ops")
                                    
                            j = j + 1
                        i = i + 1
                    ########### third and fourth quadrant ##############
                    row_aux_array3 = [0, 1, 2]
                    column_aux_array3 =[hc - 1, hc, hc+1]
                    i = 0
                    auxx = hr+1
                    while auxx != len(row):
                        
                        while i <= 2:
                            aux_matrix[2][row_aux_array3[i]] = prob_matrix[auxx][column_aux_array3[i]]
                            if aux_matrix[2][row_aux_array3[i]] >=dist_matrix[auxx][column_aux_array3[i]]:
                                    cross_amount_matrix[auxx][column_aux_array3[i]] += 1
                            i = i + 1
                        auxx = auxx+1   
                    # print("cross_matrix", cross_amount_matrix)             
                    # print("aux matriz 2", aux_matrix)
                    hr = hr + 1
            hc = hc + 1
       
       
       # Part 3 - Third Quadrant
        aux_array = [0, 1, 2]
        aux_array2 = [1, 0, 2]
        hc = half_col + 1
        while hc < len(column): 
            hr = half_row - 1
            while 0 <= hr:
                    center_aux_array2_r = [hr, hr - 1]
                    center_aux_array_c = [hc-1, hc]
                    center_aux_array2_c = [hc, hc - 1]
                    ########### first quadrant ##############
                    i = 0
                    while i < 2:
                        j = 0
                        while j < 2:
                            if hc + 1> len(column):
                                aux_matrix[aux_array[i]][aux_array2[j]]= 0
                            else:
                                aux_matrix[aux_array[i]][aux_array2[j]] = prob_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]
                                if i!= len(row) or j!= len(column) or i!= 0 or j!=0:
                                    if aux_matrix[i][j] >= dist_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]:
                                                neutrons_part = 0
                                                array_neutrons = [0,1,-1]
                                                array_neutrons2 = [-1,0,1]
                                                neutrons_part =  cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]/9
                                                cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] = round(cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]*1/9,0)
                                                for t in range(3):
                                                    for k in range(3):
                                                        if ii[t] < len(cross_amount_matrix) and jj[k] < len(cross_amount_matrix[0]):  
                                                            ####mudar o nome da variavel ou uniformizar e tratar as corners de outra maneira
                                                            cross_amount_matrix[ii[t]][jj[k]] += round(neutrons_part, 0)
                                    print(cross_amount_matrix)
                                else: 
                                        print("ops")
                                
                            j = j + 1
                        i = i + 1
                    ########### second quadrant ##############
                    i = 0
                    while i < 2:
                        j = 0
                        while j < 2:
                            aux_matrix[aux_array[i]][aux_array[j]] = prob_matrix[center_aux_array2_r[-i]][center_aux_array2_c[j]]
                            if i!= len(row) or j!= len(column) or i!= 0 or j!=0:
                                    if aux_matrix[i][j] >= dist_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]:
                                                neutrons_part = 0
                                                array_neutrons = [0,1,-1]
                                                array_neutrons2 = [-1,0,1]
                                                neutrons_part =  cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]/9
                                                cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] = round(cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]*1/9,0)
                                                for t in range(3):
                                                    for k in range(3):
                                                        if ii[t] < len(cross_amount_matrix) and jj[k] < len(cross_amount_matrix[0]):  
                                                            ####mudar o nome da variavel ou uniformizar e tratar as corners de outra maneira
                                                            cross_amount_matrix[ii[t]][jj[k]] += round(neutrons_part, 0)
                                    print(cross_amount_matrix)
                            else: 
                                        print("ops")
                            
                            j = j + 1
                        i = i + 1
                    ########### third and fourth quadrant ##############
                    row_aux_array3 = [0, 1, 2]
                    column_aux_array3 = [hc - 1, hc, hc+1]
                    i = 0
                    auxx = hr+1
                    while auxx != len(row):
                        
                        while i <= 2:
                            aux_matrix[2][row_aux_array3[i]] = prob_matrix[auxx][column_aux_array3[i]]
                            if aux_matrix[2][row_aux_array3[i]] >=dist_matrix[auxx][column_aux_array3[i]]:
                                    cross_amount_matrix[auxx][column_aux_array3[i]] += 1
                            i = i + 1
                        auxx = auxx+1 
                    # print("cross_matrix", cross_amount_matrix)                     
                    # print("aux matriz 3", aux_matrix)
                    hr = hr - 1
            hc = hc + 1
                
                
         # Part 4 - Fourth Quadrant
        aux_array = [0, 1, 2]
        aux_array2 = [2, 1, 0]
        hc = half_col
        while 0 <= hc: 
            hr = half_row
            while hr<len(row):
                    center_aux_array2_r = [hr, hr - 1]
                    center_aux_array_c = [hc-1, hc]
                    center_aux_array2_c = [hc, hc - 1]
                    ########### first quadrant ##############
                    i = 0
                    while i < 2:
                        j = 0
                        while j < 2:
                            if hr> len(row):
                                aux_matrix[aux_array[i]][aux_array2[j]]= 0
                            else:
                                aux_matrix[aux_array[i]][aux_array2[j]] = prob_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]
                            if aux_matrix[i][j] >= dist_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]:
                                    cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] += 1
                            j = j + 1
                        i = i + 1
                    ########### second quadrant ##############
                    i = 0
                    while i < 2:
                        j = 0
                        while j < 2:
                            aux_matrix[aux_array[i]][aux_array[j]] = prob_matrix[center_aux_array2_r[-i]][center_aux_array2_c[j]]
                            if i!= len(row) or j!= len(column) or i!= 0 or j!=0:
                                    if aux_matrix[i][j] >= dist_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]:
                                                neutrons_part = 0
                                                array_neutrons = [0,1,-1]
                                                array_neutrons2 = [-1,0,1]
                                                neutrons_part =  cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]/9
                                                cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]] = round(cross_amount_matrix[center_aux_array2_r[i]][center_aux_array_c[j]]*1/9,0)
                                                for t in range(3):
                                                    for k in range(3):
                                                        if ii[t] < len(cross_amount_matrix) and jj[k] < len(cross_amount_matrix[0]):  
                                                            ####mudar o nome da variavel ou uniformizar e tratar as corners de outra maneira
                                                            cross_amount_matrix[ii[t]][jj[k]] += round(neutrons_part, 0)
                                    print(cross_amount_matrix)
                            else: 
                                    print("ops")
                            
                            j = j + 1
                        i = i + 1
                    ########### third and fourth quadrant ##############
                    row_aux_array3 = [0, 1, 2]
                    column_aux_array3 =[hc - 1, hc, hc+1]
                    i = 0
                    auxx = hr+1
                    while auxx != len(row):
                        
                        while i <= 2:
                            aux_matrix[2][row_aux_array3[i]] = prob_matrix[auxx][column_aux_array3[i]]
                            if aux_matrix[2][row_aux_array3[i]] >=dist_matrix[auxx][column_aux_array3[i]]:
                                    cross_amount_matrix[auxx][column_aux_array3[i]] += 1
                            i = i + 1
                        auxx = auxx+1
                    # print("cross_matrix", cross_amount_matrix)
                    # print("aux matriz 4", aux_matrix)
                    hr = hr + 1
            hc = hc - 1  
        print("cross amount matrix", cross_amount_matrix)
        return cross_amount_matrix     



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



sns.heatmap(cross_amount_matrix, annot=True, cmap="viridis")
plt.show()

