import numpy as np

v = 2.4355  # for thermal 235U

#### core homogenization ####

# density g/cm^3 at STP
# p_Th232 = 11.724
# p_U233  = 16.7   ####procurar com mais informações
p_O = 1.429
p_Fe = 7.874
# p_H2O = 
#source:https://www.nuclear-power.com/i ; https://iopscience.iop.org/article/10.1088/1742-6596/98/6/062017/pdf 

general_height =  4.2672 #m
power =  1000*(10**6) # MWt (335 MWe)

# atomic number density : N = (density*Na)/m
Na = 6.02214076 * 10**(23)
dens = 10.5  # convention
m = ((0.0495/235.04393 + 0.9505/238.05078)**(-1)+15.999*2)
n_U = (0.0495/235.04393 + 0.9505/238.05078)**(-1)
n_UO2 = dens * Na / m
n_U235 = (0.0495 * Na * 10.5 / 235.04393) * (238.05078 / m)
n_U238 = (0.9505 * Na * 10.5 / 238.05078) * (235.04393 / m)
n_O = 2 * n_UO2
n_Fe = 7.874 * Na / 55.845
n_H2O = 0.999 * Na / 18.015

#dimensions reactor core
active_core_diameter = 2.4127 #m
core_average_power_density = 51.26 #W/C

#dimensions fuel assembly
fa_lenght = 21.4 #square, in cm
fa_rod = 17 #Fuel assembly rod lattice (17x17 / 264 fuel rods + 25 non-fuel rods)
n_FA = 89
aux = 185

#dimensions fuel-pin cell - geometry: square
heat_rate = 99.74 #W/cm
fuel_pellet_radius = 0.4095 #cm
#fuel type = UO2
gap_width = 0.0082 #cm
clad_thickness = 0.0572 #cm
#clad material = Fe
clad_radius = fuel_pellet_radius + clad_thickness + gap_width
clad_area = ((clad_radius)**2) * np.pi
gap_radius = fuel_pellet_radius + gap_width
gap_area = ((gap_radius)**2) * np.pi
pin_pitch = 1.254 #cm  (distância entre os centros de duas varetas)
#coolant type = light water
area_H2O = (pin_pitch)**2 - clad_area
#BA material ( Burnable Absorber ) = zirconium bidoride (ZrB2) => linear density +- = 1.0 mg/cm 10

#primary coolant system
core_float_rate = 4700 #kg/s
nominal_pressure = 15.5 #MPa
inlet_temp = 565 #K
outlet_temp = 330 #K

# volume m^3 -- unity
vol_UO2 = (((fuel_pellet_radius) ** 2 ) * np.pi * general_height)*10**(-4)
vol_Fe = ((clad_area - gap_area)* (clad_radius*2*np.pi)  * general_height)*10**(-4)
vol_H2O = (area_H2O * general_height)*10**(-4)
vol_Fa = (fa_lenght**2)*general_height*10**(-4)

#volume m^3 -- total
aux = 17 ** 2 * 89 
tt_act_core_vol = (general_height * (active_core_diameter/2)**2*(np.pi))
tt_vol_UO2 = aux *  vol_UO2
tt_vol_Fe = aux *  vol_Fe
tt_vol_H2O = aux *  vol_H2O
# #without gap vol
# tt_volume = n_FA * vol_Fa
