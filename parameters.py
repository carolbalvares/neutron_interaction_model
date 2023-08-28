import numpy as np

## core homogenization
# density g/cm^3 at STP
p_Th232 = 11.724
p_U233  = 16.7   ####procurar com mais informações
p_O = 1.429
p_Fe = 7.874
# p_H2O = 
#source:https://www.nuclear-power.com/i ; https://iopscience.iop.org/article/10.1088/1742-6596/98/6/062017/pdf 

general_height =  4.2672 #m

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
#core configuration: 185 (FA)???? * (17 * 17) (The fuel rods in each fuel assembly are arranged in 17 x 17 rectangular lattices) *  28 (layers) * 89 (number of FA)
aux = 17 ** 2 * 89 
tt_act_core_vol = (general_height * (active_core_diameter/2)**2*(np.pi))
tt_vol_UO2 = aux *  vol_UO2
tt_vol_Fe = aux *  vol_Fe
tt_vol_H2O = aux *  vol_H2O
# #without gap vol
# tt_volume = n_FA * vol_Fa


# print("tt_act_core_vol", tt_act_core_vol)
# print("tt_vol_UO2", tt_vol_UO2)
# print("tt_vol_Fe", tt_vol_Fe)
# print("tt_vol_H2O", tt_vol_H2O)
# print("tt", tt_volume)