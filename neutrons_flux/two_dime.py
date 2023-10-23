from parameters import *
from homogenization.hmg_scattering import macro_scattering_Fe
from homogenization.hmg_gamma import macro_cs_gamma_fuel, macro_gamma_Fe
from homogenization.hmg_fission import macro_cs_fission
import sys
sys.path.append('../')

class Random_array:
    def __init__(self, num_samples):
        self.num_samples = num_samples
        r_samples_array = np.random.rand(num_samples).round(3)
        print("samples array:   ", r_samples_array)
        return r_samples_array


class Distance:
    def __init__(self, num_samples, tt_cross_section, row, column):
        self.num_samples = num_samples
        self.tt_cross_section = tt_cross_section
        self.row = row
        self.column = column



class Two_dimensions:
    def __init__(self, num_samples, tt_cross_section, row, column, r_array):
        self.num_samples = num_samples
        self.tt_cross_section = tt_cross_section
        self.row = row
        self.column = column
        self.r_array = r_array

    def random_array(self, num_samples, r_array):
        self.num_samples = num_samples
        self.r_array = r_array
        r_samples_array = np.random.rand(num_samples).round(3)
        print("samples array:   ", r_samples_array)
        r_array = r_samples_array
        return r_array

    def distance(self, num_samples, tt_cross_section, row, column, r_array):
        self.num_samples = num_samples
        self.tt_cross_section = tt_cross_section
        self.row = row
        self.column = column
        self.r_array = r_array
        prob_matrix = np.zeros((row, column))
        i = 0
        while i < len(r_array):
            for r in row:
                for c in column:
                    if (r % 2 != 0 and c % 2 == 0) or (r % 2 == 0 and c % 2 != 0):
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
                    else 

    def cross_amount(self, tt_cross_section, row, column):
        self.tt_cross_section = tt_cross_section
        self.row = row
        self.column = column
        cross_amount_matrix = np.zeros((row, column))
        aux = 3
        aux_matrix = np.zeros((aux, aux))
        print("aux matriz", aux_matrix)
        total_spaces = row * column
        for i in total_spaces:
            for r in row:
                for c in column:
                    for x in


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
    column = np.append(column, x+1)
    row = np.append(row, x+1)


aux = Two_dimensions(
    initial_neutrons, macro_tt_UO2, rowcol, rowcol)
random_array = aux.random_array(
    initial_neutrons)
cross_amount = aux.cross_amount(macro_tt_UO2, rowcol, rowcol)

# como fazer quando tiver numero diferente de colunas e linhas
