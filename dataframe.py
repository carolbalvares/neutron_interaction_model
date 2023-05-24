from montecarlo_1d_2ways import qt_left, qt_right, total_int, initial_num_samples
from montecarlo_1d_1way import *
import pandas as pd

# setting data frame
n_cross_1d_1w_df = pd.DataFrame({
    "qt_neutrons_crossed": array_of_crossed
})
n_cross_1d_1w_df.head()
n_cross_1d_1w_df = n_cross_1d_1w_df.T

qt_left = qt_left.T
n_cross_1d_2w_df = pd.DataFrame({
    "qt_right": qt_right,
    "qt_left": qt_left,
    "total_int": total_int
})

