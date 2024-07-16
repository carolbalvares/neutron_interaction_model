import numpy as np

##ONE DIMENSION

one_d_df_5 = [45741,7590,436,20,0] #densidade%n de particulas
python = [89900, 9087, 911, 85, 15]
# openmc=[58, 58, 15, 3, 0]


## TWO DIMENSIONS
neutron_flux_values_openmc =np.array( [
    523.279004, 2168.936060, 3571.512504, 2185.006363, 525.697360,
    2197.683749, 12661.421117, 24161.207437, 12595.640454, 2173.572822,
    3605.617669, 24215.271718, 49360.123614, 24187.019510, 3568.238635,
    2170.938314, 12650.431384, 24268.280515, 12612.123250, 2195.513602,
    513.449598, 2157.760072, 3631.601986, 2171.109212, 526.930728
]).astype(int)


neutron_flux_values_python = np.array([
    [8034, 12595, 22016, 12436, 7977],
    [19762, 42197, 63343, 41299, 19341],
    [28617, 71656, 170267, 71712, 28008],
    [21586, 46727, 73410, 47320, 21524],
    [10764, 21606, 29251, 22077, 10884]
])

neutron_flux_values_finite_dif = np.array([
    [109, 472, 825, 472, 109],
    [472, 3075, 7418, 3075, 472],
    [825, 7418, 25318, 7418, 825],
    [472, 3075, 7418, 3075, 472],
    [109, 472, 825, 472, 109]
])