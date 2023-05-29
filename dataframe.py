# from montecarlo_1d_2ways import qt_left, qt_right, total_int, initial_num_samples
from montecarlo_1d_1way import *
import pandas as pd

# setting data frame
df_1d_1w = pd.DataFrame(cross_matrix)
df_1d_1w.head()       
print(df_1d_1w)


# columns = ["amount_neutrons_crossed"]
# transposed = np.array(columns).T.tolist()

# df_selected = df_1d_1w[transposed]
# df_sel_transp = df_selected.T

