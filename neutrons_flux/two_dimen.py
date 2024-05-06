import sys

sys.path.append("../")
from homogenization.cross_sections import *
from parameters import *
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class Random_array:
    # class defines one array of random numbers,  quantity of samples definied by the user
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
        # r_array = array of random numbers (from other class)
        self.r_array = r_array
        # creates one prob_matrix that will be completed, but now it has only zeros
        prob_matrix = np.zeros((len(row), len(column)))
        # creates condition using i as aux for while i < len(r_array):
        i = 0
        while i < len(r_array):
            # creates condition using r as aux for while r < len(row):
            r = 0
            while r < len(row):
                # creates condition using c as aux for while c < len(column):
                # using these 3 conditions, we complete every window of our prob_matrix with the probability definied as dist_to_collision
                c = 0
                while c < len(column):
                    if i < len(r_array):
                        if r_array[i] != 1:
                            dist_to_collision = (
                                -np.log(1 - r_array[i]) / tt_cross_section
                            )
                            prob_matrix[r][c] = round(dist_to_collision, 4)
                        else:
                            while i < len(r_array) and r_array[i] == 1:
                                r_array[i] = round(np.random.rand(), 3)
                                i += 1
                                if i < len(r_array):
                                    dist_to_collision = (
                                        -np.log(1 - r_array[i]) / tt_cross_section
                                    )
                                    prob_matrix[r][c] = round(dist_to_collision, 4)
                    i += 1
                    c += 1
                r += 1
        # we add to each corner one row or column of zeros
        matrix_corners = np.zeros((len(row) + 2, len(column) + 2))
        matrix_corners[1 : len(row) + 1, 1 : len(column) + 1] = prob_matrix


        print("matrix", matrix_corners)
        return matrix_corners


class Distance:
    # usando fórmula da distância euclidiana: \[ d = \sqrt{(i - 3)^2 + (j - 3)^2} \]
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def dist(self, row, column):
        self.row = row
        self.column = column
        half_row = ((len(row)) + 1) // 2
        half_col = ((len(column)) + 1) // 2
        distance_matrix = np.zeros((len(row), len(column)))
        for i in range(len(row)):
            for j in range(len(column)):
                distance_matrix[i][j] = round(
                    np.sqrt((i + 1 - half_row) ** 2 + (j + 1 - half_col) ** 2), 3
                )
        final_dist_matrix = np.zeros((len(row) + 2, len(column) + 2))
        final_dist_matrix[1 : len(row) + 1, 1 : len(column) + 1] = (
            distance_matrix  *5
        )
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

        ##defining
        cross_amount_matrix = np.zeros(((len(row) + 2), (len(column) + 2)))
        aux_matrix = np.zeros((3, 3))
        half_row = (len(row) + 2) // 2
        half_col = (len(column) + 2) // 2
        neutrons = initial_neutrons
        distance = Distance(row, column)
        dist_matrix = distance.dist(row, column)

        # II QUADRANT  #######################################################################################amarelo no centro certinho
        # vetores auxiliares usado para acessar elementos da matriz auxiliar
        #######################################ver se pode generalizar esses arrays
        aux_array = [1, 0, 2]
        aux_array2 = [1, 2, 0]
        cross_amount_matrix[half_row][half_col] = neutrons / 4
        #This "while" makes all windows in the second quadrant to be analysed
        hc = half_col
        while hc >= 0:
            hr = half_row
            while hr >= 0:
                #################################################ver se pode generalizar esses arrays
                center_aux_array_r = [hr, hr - 1, hr + 1]
                center_aux_array_c = [hc, hc - 1, hc + 1]
                # verifica se todos os elementos da matriz auxiliar são diferentes de zero
                # matriz auxiliar
                aux_matrix = np.zeros((3, 3))
                i = 0
                while i < 3:
                    j = 0
                    while j < 3:
                        # Verificar limites da matriz
                        if (
                            center_aux_array_r[i] >= 0
                            and center_aux_array_r[i] <= len(prob_matrix)
                            and center_aux_array_c[j] >= 0
                            and center_aux_array_c[j] <= len(prob_matrix[0])
                        ):
                            aux_matrix[aux_array[i]][aux_array[j]] = prob_matrix[
                                center_aux_array_r[i]
                            ][center_aux_array_c[j]]
                            if not np.all(aux_matrix == 0):
                                # comparando um valor da aux_matrix com o valor correspondente na dist_matrix.
                                # Se o valor na aux_matrix for maior ou igual ao valor correspondente na dist_matrix,
                                # significa que o nêutron pode se mover para a próxima célula sem colidir.
                                # Portanto, a quantidade de nêutrons na célula atual é atualizada.
                                if (
                                    aux_matrix[aux_array[i]][aux_array2[j]]
                                    >= dist_matrix[center_aux_array_r[i]][
                                        center_aux_array_c[j]
                                    ]
                                ):  
                                    neutrons_part = (
                                            cross_amount_matrix[center_aux_array_r[i]][
                                                center_aux_array_c[j]
                                            ]
                                            / 9
                                        )
                                    # neutrons_part_si= 100000
                                    cross_amount_matrix[center_aux_array_r[i]][
                                        center_aux_array_c[j]
                                    ] = round(# 8/9 dos neutrons ficam na casa atual para que o centro tambem receba sua parte
                                        cross_amount_matrix[center_aux_array_r[i]][
                                            center_aux_array_c[j]
                                        ]
                                        * 8
                                        / 9,
                                        0,
                                        #arredonda para 0 os numeros quebrados
                                    )
                                    #se a casa a uma linha acima e uma coluna a esquerda da casa analisada forem menores que o 
                                    #comprimento da linha e da coluna, entra-se no if:
                                    #seleciona-se 1/9 da quantidade total (((((ver isso)))))
                                    if hr - 1 < len(row) and hc - 1 < len(column):
                                        #se popula cross_amount_matrix 
                                        for t in range(2):
                                            for k in range(2):
                                                #se o valor do center_aux_array_r (formato center_aux_array_r = [hr, hr - 1, hr + 1]) em t for maior que a len de linhas de cross_amount_matrix
                                                #e se o valor de center_aux_array_c for maior que o  len de colunas de cross_amount_matrix 
                                                # Em Python, você pode obter o número de linhas e colunas de uma matriz (assumindo que é uma lista de listas)
                                                # usando len(matrix) para as linhas e len(matrix[0]) para as colunas.
                                                if center_aux_array_r[t] < len(
                                                    cross_amount_matrix
                                                ) and center_aux_array_c[k] < len(
                                                    cross_amount_matrix[0]
                                                ):
                                                    #caso essas condicoes forem verdadeiras, a matrix cross_amount_matrix recebe na posicao analisada
                                                    #anteriormente uma adicao a seu valor que e neutrons_part
                                                    cross_amount_matrix[
                                                        center_aux_array_r[t]
                                                    ][center_aux_array_c[k]] += round(
                                                        neutrons_part, 0
                                                    )
                                else:
                                    cross_amount_matrix[center_aux_array_r[i]][
                                        center_aux_array_c[j]
                                        # 8/9 dos neutrons ficam na casa atual
                                    ] = round(
                                        cross_amount_matrix[center_aux_array_r[i]][
                                            center_aux_array_c[j]
                                        ]
                                        * 8
                                        / 9,
                                        0,
                                    )
                                    neutrons_part = 0
                                    for t in range(2):
                                            for k in range(2):
                                                if center_aux_array_r[t] < len(
                                                    cross_amount_matrix
                                                ) and center_aux_array_c[k] < len(
                                                    cross_amount_matrix[0]
                                                ):
                                                    cross_amount_matrix[
                                                        center_aux_array_r[t]
                                                    ][center_aux_array_c[k]] += round(
                                                        neutrons_part, 0
                                                    )
                            elif (
                                hr == 0
                                or hr == len(row) - 1
                                or hc == 0
                                or hc == len(column) - 1
                            ):
                                prob_matrix[center_aux_array_r[i]][
                                    center_aux_array_c[j]
                                ] = 0
                            # print("cross amount", cross_amount_matrix)

                        j = j + 1
                    i = i + 1
                hr = hr - 1
            hc = hc - 1

        # I QUADRANT ##############centro certinho###################################################
        aux_array = [1, 0, 2]
        aux_array2 = [1, 2, 0]
        cross_amount_matrix[half_row][half_col] = neutrons / 4
        hc = half_col
        while hc <= len(column):
            hr = half_row
            while hr >= 0:
                center_aux_array_r = [hr, hr - 1, hr + 1]
                center_aux_array_c = [hc, hc + 1, hc - 1]
                aux_matrix = np.zeros((3, 3))
                i = 0
                while i < 3:
                    j = 0
                    while j < 3:
                        # Verificar limites da matriz
                        if (
                            center_aux_array_r[i] >= 0
                            and center_aux_array_r[i] <= len(prob_matrix)
                            and center_aux_array_c[j] >= 0
                            and center_aux_array_c[j] <= len(prob_matrix[0])
                        ):
                            aux_matrix[aux_array[i]][aux_array[j]] = prob_matrix[
                                center_aux_array_r[i]
                            ][center_aux_array_c[j]]
                            if not np.all(aux_matrix == 0):
                                if (
                                    aux_matrix[aux_array[i]][aux_array2[j]]
                                    >= dist_matrix[center_aux_array_r[i]][
                                        center_aux_array_c[j]
                                    ]
                                ):
                                    neutrons_part = 0
                                    cross_amount_matrix[center_aux_array_r[i]][
                                        center_aux_array_c[j]
                                    ] = round(
                                        cross_amount_matrix[center_aux_array_r[i]][
                                            center_aux_array_c[j]
                                        ]
                                        * 8
                                        / 9,
                                        0,
                                    )
                                    if hr - 1 < len(row) and hc + 1 > 0:
                                        neutrons_part = (
                                            cross_amount_matrix[center_aux_array_r[i]][
                                                center_aux_array_c[j]
                                            ]
                                            / 9
                                        )
                                        # neutrons_part_si = 100090

                                        for t in range(2):
                                            for k in range(2):
                                                if center_aux_array_r[t] < len(
                                                    cross_amount_matrix
                                                ) and center_aux_array_c[k] < len(
                                                    cross_amount_matrix[0]
                                                ):
                                                    cross_amount_matrix[
                                                        center_aux_array_r[t]
                                                    ][center_aux_array_c[k]] += round(
                                                        neutrons_part, 0
                                                    )
                                else:
                                    cross_amount_matrix[center_aux_array_r[i]][
                                        center_aux_array_c[j]
                                        # 8/9 dos neutrons ficam na casa atual
                                    ] = round(
                                        cross_amount_matrix[center_aux_array_r[i]][
                                            center_aux_array_c[j]
                                        ]
                                        * 8
                                        / 9,
                                        0,
                                    )
                                    neutrons_part = 0
                                    for t in range(2):
                                            for k in range(2):
                                                if center_aux_array_r[t] < len(
                                                    cross_amount_matrix
                                                ) and center_aux_array_c[k] < len(
                                                    cross_amount_matrix[0]
                                                ):
                                                    cross_amount_matrix[
                                                        center_aux_array_r[t]
                                                    ][center_aux_array_c[k]] += round(
                                                        neutrons_part, 0
                                                    )
                            elif (
                                hr == 0
                                or hr == len(row) - 1
                                or hc == 0
                                or hc == len(column) - 1
                            ):
                                prob_matrix[center_aux_array_r[i]][
                                    center_aux_array_c[j]
                                ] = 0
                            # print("cross amount", cross_amount_matrix)

                        j = j + 1
                    i = i + 1
                hr = hr - 1
            hc = hc + 1

        # III QUADRANT #################################################################################################################
        aux_array = [1, 0, 2]
        aux_array2 = [1, 2, 0]
        cross_amount_matrix[half_row][half_col] = neutrons / 4
        hc = half_col
        while hc >= 0:
            hr = half_row
            while hr <= len(row):
                center_aux_array_r = [hr, hr + 1, hr - 1]
                center_aux_array_c = [hc, hc - 1, hc + 1]
                aux_matrix = np.zeros((3, 3))
                i = 0
                while i < 3:
                    j = 0
                    while j < 3:
                        # Verificar limites da matriz
                        if (
                            center_aux_array_r[i] >= 0
                            and center_aux_array_r[i] <= len(prob_matrix)
                            and center_aux_array_c[j] >= 0
                            and center_aux_array_c[j] <= len(prob_matrix[0])
                        ):
                            aux_matrix[aux_array[i]][aux_array[j]] = prob_matrix[
                                center_aux_array_r[i]
                            ][center_aux_array_c[j]]
                            if not np.all(aux_matrix == 0):
                                if (
                                    aux_matrix[aux_array[i]][aux_array2[j]]
                                    >= dist_matrix[center_aux_array_r[i]][
                                        center_aux_array_c[j]
                                    ]
                                ):
                                    neutrons_part = 0
                                    cross_amount_matrix[center_aux_array_r[i]][
                                        center_aux_array_c[j]
                                    ] = round(
                                        cross_amount_matrix[center_aux_array_r[i]][
                                            center_aux_array_c[j]
                                        ]
                                        * 8
                                        / 9,
                                        0,
                                    )
                                    if hr - 1 < len(row) and hc + 1 > 0:
                                        neutrons_part = (
                                            cross_amount_matrix[center_aux_array_r[i]][
                                                center_aux_array_c[j]
                                            ]
                                            / 9
                                        )
                                        # neutrons_part_si=100000
                                        for t in range(2):
                                            for k in range(2):
                                                if center_aux_array_r[t] < len(
                                                    cross_amount_matrix
                                                ) and center_aux_array_c[k] < len(
                                                    cross_amount_matrix[0]
                                                ):
                                                    cross_amount_matrix[
                                                        center_aux_array_r[t]
                                                    ][center_aux_array_c[k]] += round(
                                                        neutrons_part, 0
                                                    )
                                else:
                                    cross_amount_matrix[center_aux_array_r[i]][
                                        center_aux_array_c[j]
                                        # 8/9 dos neutrons ficam na casa atual
                                    ] = round(
                                        cross_amount_matrix[center_aux_array_r[i]][
                                            center_aux_array_c[j]
                                        ]
                                        * 8
                                        / 9,
                                        0,
                                    )
                                    neutrons_part = 0
                                    for t in range(2):
                                            for k in range(2):
                                                if center_aux_array_r[t] < len(
                                                    cross_amount_matrix
                                                ) and center_aux_array_c[k] < len(
                                                    cross_amount_matrix[0]
                                                ):
                                                    cross_amount_matrix[
                                                        center_aux_array_r[t]
                                                    ][center_aux_array_c[k]] += round(
                                                        neutrons_part, 0
                                                    )
                            elif (
                                hr == 0
                                or hr == len(row) - 1
                                or hc == 0
                                or hc == len(column) - 1
                            ):
                                prob_matrix[center_aux_array_r[i]][
                                    center_aux_array_c[j]
                                ] = 0
                            elif (
                                hr == 0
                                or hr == len(row) - 1
                                or hc == 0
                                or hc == len(column) - 1
                            ):
                                prob_matrix[center_aux_array_r[i]][
                                    center_aux_array_c[j]
                                ] = 0
                            # print("cross amount", cross_amount_matrix)

                        j = j + 1
                    i = i + 1
                hr = hr + 1
            hc = hc - 1

        # IV QUADRANT
        aux_array = [1, 0, 2]
        aux_array2 = [1, 2, 0]
        cross_amount_matrix[half_row][half_col] = neutrons / 4
        hc = half_col
        while hc <= len(column):
            hr = half_row
            while hr <= len(row):
                center_aux_array_r = [hr, hr + 1, hr - 1]
                center_aux_array_c = [hc, hc + 1, hc - 1]
                aux_matrix = np.zeros((3, 3))
                i = 0
                while i < 3:
                    j = 0
                    while j < 3:
                        # Verificar limites da matriz
                        if (
                            center_aux_array_r[i] >= 0
                            and center_aux_array_r[i] <= len(prob_matrix)
                            and center_aux_array_c[j] >= 0
                            and center_aux_array_c[j] <= len(prob_matrix[0])
                        ):
                            aux_matrix[aux_array[i]][aux_array[j]] = prob_matrix[
                                center_aux_array_r[i]
                            ][center_aux_array_c[j]]
                            if not np.all(aux_matrix == 0):
                                if (
                                    aux_matrix[aux_array[i]][aux_array2[j]]
                                    >= dist_matrix[center_aux_array_r[i]][
                                        center_aux_array_c[j]
                                    ]
                                ):
                                    cross_amount_matrix[center_aux_array_r[i]][
                                        center_aux_array_c[j]
                                    ] = round(
                                        cross_amount_matrix[center_aux_array_r[i]][
                                            center_aux_array_c[j]
                                        ]
                                        * 8
                                        / 9,
                                        0,
                                    )
                                    neutrons_part = 0
                                    if hr - 1 < len(row) and hc + 1 > 0:
                                        neutrons_part = (
                                            cross_amount_matrix[center_aux_array_r[i]][
                                        center_aux_array_c[j]
                                            ]
                                            / 9
                                        )
                                        # neutrons_part=99999
                                        for t in range(2):
                                            for k in range(2):
                                                if center_aux_array_r[t] < len(
                                                    cross_amount_matrix
                                                ) and center_aux_array_c[k] < len(
                                                    cross_amount_matrix[0]
                                                ):
                                                    cross_amount_matrix[
                                                        center_aux_array_r[t]
                                                    ][center_aux_array_c[k]] += round(
                                                        neutrons_part, 0
                                                    )
                                else:
                                    cross_amount_matrix[center_aux_array_r[i]][
                                        center_aux_array_c[j]
                                        # 8/9 dos neutrons ficam na casa atual
                                    ] = round(
                                        cross_amount_matrix[center_aux_array_r[i]][
                                            center_aux_array_c[j]
                                        ]
                                        * 8
                                        / 9,
                                        0,
                                    )
                                    neutrons_part = 0
                                    for t in range(2):
                                            for k in range(2):
                                                if center_aux_array_r[t] < len(
                                                    cross_amount_matrix
                                                ) and center_aux_array_c[k] < len(
                                                    cross_amount_matrix[0]
                                                ):
                                                    cross_amount_matrix[
                                                        center_aux_array_r[t]
                                                    ][center_aux_array_c[k]] += round(
                                                        neutrons_part, 0
                                                    )
                            elif (
                                hr == 0
                                or hr == len(row) - 1
                                or hc == 0
                                or hc == len(column) - 1
                            ):
                                prob_matrix[center_aux_array_r[i]][
                                    center_aux_array_c[j]
                                ] = 0
                            # print("cross amount", cross_amount_matrix)

                        j = j + 1
                    i = i + 1
                hr = hr + 1
            hc = hc + 1
        print("cross amount", cross_amount_matrix)
        print("soma", np.sum(cross_amount_matrix))
        df = pd.DataFrame(cross_amount_matrix)
        nome_arquivo = "matriz_excel_python_1.xlsx"
        df.to_excel(nome_arquivo, index=False, header=False)
        return cross_amount_matrix


# micro_scattering_U235 = 15.04 * 10 ** (-24)
# micro_scattering_U238 = 9.360 * 10 ** (-24)
# micro_scattering_O = 3.780 * 10 ** (-24)
# ##corrigir tudo

macro_scattering_U235 = micro_scattering_U235 * n_U235
macro_scattering_U238 = micro_scattering_U238 * n_U238
macro_scattering_O = micro_scattering_O * n_O

macro_cs_UO2_scattering = (
    (macro_scattering_U235 + macro_scattering_U238 + macro_scattering_O)
    * (tt_vol_UO2)
    / tt_act_core_vol
)

micro_cs_UO2_scattering = macro_cs_UO2_scattering / (6.02214076 * 10 ** (23))

macro_cs_UO2_absorption = macro_cs_gamma + macro_cs_fission

macro_tt_UO2 = (macro_cs_UO2_absorption + macro_cs_UO2_scattering) * 10 ** (-23)

# micro_tt_UO2 = micro_cs_scattering + micro_cs_absorption


# macro_cs_Fe_absorption = macro_gamma_Fe
# macro_tt_Fe = macro_cs_Fe_absorption + macro_scattering_Fe

# print("micro_tt_UO2", micro_tt_UO2)
# print("micro_cs_scattering", micro_cs_scattering)
# print("micro_cs_absorption", micro_cs_absorption)

# max_dist = 1/micro_tt_UO2
# print("max_dist", max_dist)


initial_neutrons = int(input("Choose initial number of neutrons:    "))
row_input = int(input("Choose your matrix row dimension:     "))
col_input = int(input("Choose your matrix column dimension:     "))
rowcol_array = np.array([])
column = np.array([])
row = np.array([])
for x in range(row_input):
    row = np.append(row, int(x + 1))
for y in range(col_input):
    column = np.append(column, int(y + 1))

obj = Random_array(initial_neutrons)
r_array_result = obj.random(initial_neutrons)
item = Probability(initial_neutrons, macro_tt_UO2, row, column, r_array_result)
prob_matrix = item.probab(initial_neutrons, macro_tt_UO2, row, column, r_array_result)
aux = Two_dimensions(row, column, prob_matrix, initial_neutrons)
cross_amount_matrix = aux.quadrants(row, column, prob_matrix, initial_neutrons)

print("macro_tt_UO2", macro_tt_UO2)

sns.heatmap(cross_amount_matrix, annot=False, cmap="viridis")
plt.show()
