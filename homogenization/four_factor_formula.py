from hmg_absorption import macro_cs_absorption
from hmg_fission import macro_cs_fission

#given data
v = 2.4355 # for thermal 235U


n = v * macro_cs_fission/macro_cs_absorption