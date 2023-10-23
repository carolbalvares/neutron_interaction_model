from parameters import *
from homogenization.hmg_scattering import macro_scattering_Fe
from homogenization.hmg_gamma import macro_cs_gamma_fuel, macro_gamma_Fe
from homogenization.hmg_fission import macro_cs_fission
import sys
sys.path.append('../')


class Random_array:
    def __init__(self, num_samples):
        self.num_samples = num_samples
        
    def random(self, num_samples):
        self.num_samples = num_samples
        r_samples_array = np.random.rand(num_samples).round(3)
        print("samples array:   ", r_samples_array)
        return r_samples_array


class Probability:
    def __init__(self, num_samples, tt_cross_section, row, column, r_array):
        self.num_samples = num_samples
        self.tt_cross_section = tt_cross_section
        self.row = row
        self.column = column
        self.r_array = r_array

    def distance(self, num_samples, tt_cross_section, row, column, r_array):
        self.num_samples = num_samples
        self.tt_cross_section = tt_cross_section
        self.row = row
        self.column = column
        self.r_array = r_array
        print("rarray", r_array)
        prob_matrix = np.zeros((len(row), len(column)))
        i = 0
        r = 0
        c = 0
        print("row", row)
        while i < len(r_array):
            while r < len(row):
                while c < len(column):
                    if r_array[i] != 1:
                        dist_to_collision = - \
                            np.log(1 - r_array[i]
                                   ) / tt_cross_section
                    else:
                        while r_array[i] == 1:
                            r_array[i] = round(
                                np.random.rand(), 3)
                        dist_to_collision = - \
                            np.log(1 - r_array[i]
                                   ) / tt_cross_section
                    prob_matrix[r][c] = dist_to_collision
                    c+=1
                r+=1
            i+=1
  

        return prob_matrix


class Two_dimensions:
    def __init__(self, num_samples, tt_cross_section, row, column,prob_matrix):
        self.num_samples = num_samples
        self.tt_cross_section = tt_cross_section
        self.row = row
        self.column = column
        self.prob_matrix = prob_matrix

    def cross_amount(self, tt_cross_section, row, column, num_samples, prob_matrix):
        self.tt_cross_section = tt_cross_section
        self.row = row
        self.column = column
        self.num_samples = num_samples
        self.prob_matrix = prob_matrix
        cross_amount_matrix = np.zeros((row, column))
        total_spaces = row * column
        half_row = len(row) // 2
        half_col = len(column) // 2

        # Definir direções
        directions = [
            (0, -1),  # Para a esquerda
            (0, 1),   # Para a direita
            (-1, 0),  # Para cima
            (1, 0),   # Para baixo
            (-1, 1),  # Diagonal superior direita
            (1, 1),   # Diagonal inferior direita
            (1, -1),  # Diagonal inferior esquerda
            (-1, -1)  # Diagonal superior esquerda
        ]

        for r in range(len(row)):
            for c in range(len(column)):
                for direction in directions:
                    i, j = half_row, half_col
                    cross_amount_matrix[half_row][half_col] = num_samples
                    while 0 <= i < row and 0 <= j < column:
                        if prob_matrix[i][j] >= 1:
                            print("ola")
                        else:
                            print("hello")
                        i += direction[0]
                        j += direction[1]
                        r+=1
                        c+=1

        return False


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

# print("macro tt cross section", macro_tt_UO2)


macro_cs_Fe_absorption = macro_gamma_Fe
macro_tt_Fe = macro_cs_Fe_absorption + macro_scattering_Fe

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
item = Probability( initial_neutrons, macro_tt_UO2, row, column, r_array_result)
prob_matrix = item.distance(initial_neutrons, macro_tt_UO2, row, column, r_array_result)
aux = Two_dimensions(initial_neutrons, macro_tt_UO2, row, column,prob_matrix)

# como fazer quando tiver numero diferente de colunas e linhas
