import pandas as pd
import numpy as np

## Generate Data
num_of_samples = 100
range_of_sample = 1000
samples = np.random.choice(range_of_sample, size=num_of_samples)

## Create DataFrame: just 1 column, named "values"
# All DataFrames automatically create a "index" column, all rows must have a unique index. 
# By default, it is 0,1,2,3,4, but you can always set a column you create to be the index (a date, for example)
samples_df = pd.DataFrame({"values": samples})

# This prints the first 5 elements of dataframe, so you know how it looks like
samples_df.head()
#print(samples_df)
## Selecting Rows: use .loc in dataframe. It always returns a new df, with the selected rows

# Specific Index 
index = 3
one_row_df = samples_df.loc[[index]]
#print(one_row_df)

# A range
first_index = 10
last_index = 30
range_of_rows_df = samples_df.loc[first_index:last_index]
#print(range_of_rows_df)

# Some indexes
indexes = [3, 4, 5, 10]
some_indexed_df = samples_df.loc[indexes]
#print(some_indexed_df)

# Get the actual value (in a specific column)
specific_value = samples_df.loc[index, "values"]
#print(specific_value)


#only values column
column_values = samples_df.values
#print(column_values)

#only index column
column_index = samples_df.index
#print(column_index)

# Getting the Sum: use .sum(), returns a new df with the sum of the columns that can be summed (numeric ones)

# Df with the sum
sum_df = samples_df.sum()
#print(sum_df)

# Value of sum of specific column. 
sum_of_values_column = sum_df = samples_df.sum()["values"]
#print(sum_of_values_column)

# See here that, to use just one column of a df, just use df["name_of_column"]. 
# If it is just one element, if will return a value instead of a df