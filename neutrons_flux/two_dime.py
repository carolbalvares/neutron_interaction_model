import sys
sys.path.append('../')
from homogenization.hmg_fission import macro_cs_fission
from homogenization.hmg_gamma import macro_cs_gamma_fuel, macro_gamma_Fe
from homogenization.hmg_scattering import macro_scattering_Fe
from parameters import *



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

    def distance(self, num_samples, tt_cross_section, row, column, r_array):
        self.num_samples = num_samples
        self.tt_cross_section = tt_cross_section
        self.row = row
        self.column = column
        self.r_array = r_array
        print("rarray", r_array)
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
                            prob_matrix[r][c] = dist_to_collision
                        else:
                            while i < len(r_array) and r_array[i] == 1:
                                r_array[i] = round(np.random.rand(), 3)
                                i += 1
                                if i < len(r_array):
                                    dist_to_collision = - \
                                        np.log(1 - r_array[i]) / \
                                        tt_cross_section
                                    prob_matrix[r][c] = dist_to_collision
                    i += 1
                    c += 1
                r += 1

        print("prob matrix", prob_matrix)
        return prob_matrix


class Two_dimensions:
    def __init__(self, num_samples, tt_cross_section, row, column, prob_matrix):
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
        cross_amount_matrix = np.zeros((len(row), len(column)))
        aux_matrix = np.zeros((3, 3))
        print(aux_matrix)
        total_spaces = row * column
        half_row = len(row) // 2
        half_col = len(column) // 2
        ###########first quadrant##############
        r_aux = half_row
        while r_aux >= 0:
            c_aux = half_col
            while c_aux < len(column):
                cross_amount_matrix[r_aux][c_aux] = prob_matrix[r_aux][c_aux]
                print("cross_amount_matrix", cross_amount_matrix)
                print("raux", r_aux)
                print("caux", c_aux)
                central_spot = cross_amount_matrix[r_aux][c_aux]
                print("central spot", central_spot)
                c_aux = c_aux + 1
            r_aux = r_aux - 1
        ###########second quadrant##############
        r_aux = half_row
        while r_aux >= 0:
            c_aux = half_col
            while c_aux >= 0:
                cross_amount_matrix[r_aux][c_aux] = prob_matrix[r_aux][c_aux]
                print("cross_amount_matrix", cross_amount_matrix)
                print("raux", r_aux)
                print("caux", c_aux)
                central_spot = cross_amount_matrix[r_aux][c_aux]
                print("central spot", central_spot)
                c_aux = c_aux - 1
            r_aux = r_aux - 1
        ###########third quadrant##############
        r_aux = half_row
        while r_aux < len(row):
            c_aux = half_col
            while c_aux >= 0:
                cross_amount_matrix[r_aux][c_aux] = prob_matrix[r_aux][c_aux]
                print("cross_amount_matrix", cross_amount_matrix)
                print("raux", r_aux)
                print("caux", c_aux)
                central_spot = cross_amount_matrix[r_aux][c_aux]
                print("central spot", central_spot)
                c_aux = c_aux - 1
            r_aux = r_aux + 1
        ###########fourth quadrant##############
        r_aux = half_row
        while r_aux < len(row):
            c_aux = half_col
            while c_aux < len(column):
                cross_amount_matrix[r_aux][c_aux] = prob_matrix[r_aux][c_aux]
                print("cross_amount_matrix", cross_amount_matrix)
                print("raux", r_aux)
                print("caux", c_aux)
                central_spot = cross_amount_matrix[r_aux][c_aux]
                print("central spot", central_spot)
                c_aux = c_aux + 1
            r_aux = r_aux + 1
            


            # caso par
            # while 0 <= i < len(row) and 0 <= j < len(column):

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
item = Probability(initial_neutrons, macro_tt_UO2, row, column, r_array_result)
prob_matrix = item.distance(
    initial_neutrons, macro_tt_UO2, row, column, r_array_result)
aux = Two_dimensions(initial_neutrons, macro_tt_UO2, row, column, prob_matrix)
cross_amount_matrix = aux.cross_amount(
    macro_tt_UO2, row, column, initial_neutrons, prob_matrix)

# como fazer quando tiver numero diferente de colunas e linhas
