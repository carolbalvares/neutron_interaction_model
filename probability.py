# import seaborn as sns
import pandas as pd
# import numpy as np

probability = [0.7, 0.1, 0.9, 0.1, 0.6, 0.7, 0.6, 1, 0.45, 0.9]
discr_1d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

free_neutrons = [1000]
short_prob = []
for e in (range(len(discr_1d))):
    free_neutrons.append(free_neutrons[e] * probability[e])
    n_of_samples = free_neutrons[e]

short_free_neutrons = ['%.3f' % elem for elem in free_neutrons]
print(short_free_neutrons)

#settingg data frame
prob_df = pd.DataFrame({"probability": probability})
