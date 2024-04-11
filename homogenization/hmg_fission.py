import sys
sys.path.append('../')  # Adjust the path as needed
from parameters import *

# core homogenization

# given data (micro fission cross section)
micro_fission_U235 = 584.4 * 10 ** (-24)
micro_fission_U238 = 11.77 * 10 ** (-27) 


#calculating homogeneous macro and micro gamma cross section
macro_fission_U235 = micro_fission_U235 * n_U235
macro_fission_U238 = micro_fission_U238 * n_U238

macro_cs_fission = (macro_fission_U235 + macro_fission_U238) * tt_vol_UO2 / tt_act_core_vol

micro_cs_fission = macro_cs_fission / n_UO2

# source:
# 1- Nuclear Reactor Analysis - James Duderstadt, Louis Hamilton  (data)
# 2- https://atom.kaeri.re.kr/old/ton/ (data)
