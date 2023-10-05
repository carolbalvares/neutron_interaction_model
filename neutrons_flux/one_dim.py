import sys
sys.path.append('../') 
from homogenization.hmg_fission import macro_cs_fission
from homogenization.hmg_gamma import macro_cs_gamma_fuel
from parameters import *



# Adjust the path as needed
# material chosen: UO2

# mi = 2/(3*m)
# free_trn_path = 1/(macro_cs_UO2_scattering*(1-mi))
# dif_coef = free_trn_path/3
# sigma_s = round(macro_cs_UO2_scattering, 3)


class One_d_one_material:
    def __init__(self, num_samples, discretizations, prob_abs, prob_scat):
        self.num_samples = num_samples
        self.discretizations = discretizations
        self.prob_abs = prob_abs
        self.prob_scat = prob_scat

    def n_neutrons_cross(self, num_samples, discretizations, prob_abs, prob_scat):
        self.discretizations = discretizations
        self.num_samples = num_samples
        self.prob_abs = prob_abs
        self.prob_scat = prob_scat
        # cant_cross_array = np.array([])
        cross_array = np.array([])
        aux_array = np.array([])
        r_samples_array = np.random.rand(num_samples).round(3)
        print("samples array:   ", r_samples_array)
        aux_array = r_samples_array
        while discretizations != 1:
            cross_array = np.array([])
            cross_amount = 0
            cant_cross_amount = 0
            cant_cross_amount = False
            for i in range(num_samples):
                if cant_cross_amount != False:
                    if prob_abs > aux_array[i] or prob_scat > aux_array[i]:
                        cant_cross_amount += 1
                        # cant_cross_array = np.append(
                        #     cant_cross_array, aux_array[i])
                        cross_array = np.append(
                            cross_array, 0.0
                        )

                        num_samples = num_samples - 1

                    else:
                        cross_amount += 1
                        cross_array = np.append(cross_array, aux_array[i])
                        # cant_cross_array = np.append(
                        #     cant_cross_array, 0.000
                        # )

                        num_samples = num_samples - 1

                else:
                    if prob_abs > aux_array[i] or prob_scat > aux_array[i]:
                        cant_cross_amount = 1
                        # cant_cross_array = np.append(
                        #     cant_cross_array, aux_array[0])
                        cross_amount = 0
                        cross_array = np.append(cross_array, 0.0)
                        num_samples = num_samples - 1

                    else:
                        cross_amount = 1
                        cross_array = np.append(cross_array, aux_array[i])
                        # cant_cross_array = np.append(
                        #     cant_cross_array, 0.000
                        # )
                        cant_cross_amount = 0
                        num_samples = num_samples - 1

            aux_array = cross_array

            num_samples = cross_amount
            discretizations -= 1
            non_zero_indices = aux_array != 0
            aux_array[non_zero_indices] = np.random.rand(
                non_zero_indices.sum()).round(3)

            print("aux_array", aux_array)
            print("discretization:  ", discretizations)
            # print("matrix: ",cross_matrix)  # Decrementa a variável auxiliar
            
            
        return cross_amount


micro_scattering_U235 = 15.04 * 10 ** (-24)
micro_scattering_U238 = 9.360 * 10 ** (-24)
micro_scattering_O = 3.780 * 10 ** (-24)

macro_scattering_U235 = micro_scattering_U235 * n_U235
macro_scattering_U238 = micro_scattering_U238 * n_U238
macro_scattering_O = micro_scattering_O * n_O

macro_cs_UO2_scattering = (macro_scattering_U235 + macro_scattering_U238 +
                           macro_scattering_O)*(tt_vol_UO2) / tt_act_core_vol
# macro_cs_UO2_scattering = 0.118

macro_cs_UO2_absorption = macro_cs_gamma_fuel + macro_cs_fission
# macro_cs_UO2_absorption = 0.258


macro_tt_UO2 = macro_cs_UO2_scattering+macro_cs_UO2_absorption
prob_scat = macro_cs_UO2_scattering/macro_tt_UO2
prob_abs = macro_cs_UO2_absorption/macro_tt_UO2
print("prob_abs", prob_abs)
print("prob_scat", prob_scat)
initial_num_discr = int(input('Choose a initial number of discretization:   '))
initial_neutrons = int(input("Choose initial number of neutrons:    "))


aux = One_d_one_material(
    initial_neutrons, initial_num_discr, prob_abs, prob_scat)
cross_amount = aux.n_neutrons_cross(
    initial_neutrons, initial_num_discr, prob_abs, prob_scat)
print("amount that crosses:       ", cross_amount)

# strange value https://www.dgtresearch.com/diffusion-coefficients/
# https://www.nuclear-power.com/nuclear-power/reactor-physics/neutron-diffusion-theory/neutron-current-density/
# Não há uma regra específica da comunidade científica para arredondamento de nêutrons além do arredondamento para o número inteiro mais próximo.
