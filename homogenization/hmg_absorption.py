import sys
sys.path.append('../')  # Adjust the path as needed
from parameters import *
from hmg_fission import macro_cs_fission
from hmg_gamma import macro_cs_gamma

micro_abs_H2O = 0.66 * 10**(-24)
macro_cs_absorption = macro_cs_gamma + macro_cs_fission
micro_cs_absorption = macro_cs_absorption/(n_UO2 + n_H2O + n_Fe)