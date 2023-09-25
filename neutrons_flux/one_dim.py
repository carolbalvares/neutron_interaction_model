
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


class One_d_discr_one:
    def __init__(self, num_samples, prob_abs, prob_scat):
        self.num_samples = num_samples
        self.prob_abs = prob_abs
        self.prob_scat = prob_scat

    def n_neutrons_cross(self, num_samples, prob_abs, prob_scat):
        self.num_samples = num_samples
        self.prob_abs = prob_abs
        self.prob_scat = prob_scat
        cant_cross_amount = 0
        cross_amount = 0
        cant_cross_array = np.array([])
        cross_array = np.array([])
        r_samples_array = np.random.rand(num_samples).round(3)
        print("samples array:   ", r_samples_array)
        print("prob_abs", prob_abs)
        print("prob_scat", prob_scat)
        aux_array = r_samples_array
        for i in range(num_samples):
            if cant_cross_amount != 0:
                if prob_abs < aux_array[i] and prob_scat < aux_array[i]:
                    cross_amount += 1
                    cross_array = np.append(cross_array, aux_array[i])
                    num_samples = num_samples - 1

                else:
                    cant_cross_amount +=  1
                    cant_cross_array = np.append(
                        cant_cross_array, aux_array[i])

                    num_samples = num_samples - 1

            else:
                if prob_abs < aux_array[i] and prob_scat < aux_array[i]:
                    cross_amount = 1
                    cross_array = np.append(cross_array, aux_array[i])
                    
                    num_samples = num_samples - 1
                else:
                    cant_cross_amount = 1
                    cant_cross_array = np.append(
                        cant_cross_array, aux_array[0])
                    
                    num_samples = num_samples - 1

            print("cant_cross_amount", cant_cross_amount)
            print("cross_amount", cross_amount)
            print("cross_array", cross_array)
        return cross_array


initial_neutrons = 10


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

aux = One_d_discr_one(initial_neutrons, prob_abs, prob_scat)
cross_matrix = aux.n_neutrons_cross(
    initial_neutrons, prob_abs, prob_scat)
print("matrix:       ", cross_matrix)

# strange value https://www.dgtresearch.com/diffusion-coefficients/
# https://www.nuclear-power.com/nuclear-power/reactor-physics/neutron-diffusion-theory/neutron-current-density/
# Não há uma regra específica da comunidade científica para arredondamento de nêutrons além do arredondamento para o número inteiro mais próximo.
