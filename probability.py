# import seaborn as sns
#import pandas as pd
# import numpy as np

probability = [0.7, 0.1, 0.9, 0.1, 0.6, 0.7, 0.6, 1, 0.45, 0.9]
discr_1d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# from first discretization
free_neutrons = [1000]
short_prob = []
for e in (range(len(discr_1d))):
    free_neutrons.append(free_neutrons[e] * probability[e])
    n_of_samples = free_neutrons[e]

free_neutrons = ['%.3f' % elem for elem in free_neutrons]
print("neutrons amount for each interaction: ", free_neutrons)


# from specific discretization
free_neutrons = [1000]
discr_start = int(input('Choose a start from 0 to 9:   '))
del probability[0:discr_start]
short_discr_1d = range(10-discr_start)
for e in short_discr_1d:
    free_neutrons.append(free_neutrons[e] * probability[e])
    n_of_samples = free_neutrons[e]

spc_free_neutrons = ['%.3f' % elem for elem in free_neutrons]
print("neutrons amount for each interaction: ", spc_free_neutrons)


## settingg data frame
#prob_df = pd.DataFrame({"probability": probability})
