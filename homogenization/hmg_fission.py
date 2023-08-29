import sys
sys.path.append('../')  # Adjust the path as needed
from parameters import *

# core homogenization

# given data
macro_fission_U235 = 584.4 * 10 ** (-24)
macro_fission_U238 = 11.77 * 10 ** (-27) 

# calculations
macro_cs_fission = (macro_fission_U235 + macro_fission_U238) * tt_vol_UO2 / tt_act_core_vol

micro_cs_fission = macro_cs_fission / n_UO2

# source:
# 1- Nuclear Reactor Analysis - James Duderstadt, Louis Hamilton  (data)
# 2- https://atom.kaeri.re.kr/old/ton/ (data)
