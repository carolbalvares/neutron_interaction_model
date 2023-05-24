# from montecarlo_1d_2ways import qt_left, qt_right, total_int, initial_num_samples
from montecarlo_1d_1way import *
import pandas as pd

# setting data frame
df_1d_1w = pd.DataFrame({
    "amount_neutrons_crossed": can_cross,
    "amount_neutrons_cant_crossed": cant_cross,
    "amount_of_interactions": total_int
})
df_1d_1w.head()

columns = ["amount_neutrons_crossed"]
transposed = np.array(columns).T.tolist()

df_selected = df_1d_1w[transposed]
df_sel_transp = df_selected.T

