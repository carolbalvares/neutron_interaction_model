import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#a mean of 100% and standard deviation of 10%
avg = 1
std_dev = .1
num_reps = 500
num_simulations = 1000


#use numpy to generate a list of percentages that will replicate our historical normal distribution
pct_to_target = np.random.normal(avg, std_dev, num_reps).round(3)
# print(pct_to_target)

#we will use a uniform distribution but assign lower probability rates for some of the values
sales_target_values = [75_000, 100_000, 200_000, 300_000, 400_000, 500_000]
sales_target_prob = [.3, .3, .2, .1, .05, .05]
sales_target = np.random.choice(sales_target_values, num_reps, p=sales_target_prob)
#print(sales_target)

#build up a pandas dataframe
df = pd.DataFrame(index=range(num_reps), data={'Pct_To_Target': pct_to_target,
                                               'Sales_Target': sales_target})

df['Sales'] = df['Pct_To_Target'] * df['Sales_Target']


def calc_commission_rate(x):
    """ Return the commission rate based on the table:
    0-90% = 2%
    91-99% = 3%
    >= 100 = 4%
    """
    if x <= .90:
        return .02
    if x <= .99:
        return .03
    else:
        return .04

#Now we create our commission rate and multiply it times sales
df['Commission_Rate'] = df['Pct_To_Target'].apply(calc_commission_rate)
df['Commission_Amount'] = df['Commission_Rate'] * df['Sales']
# df.head()
# print(df)

#set our plotting style
# sns.set_style('whitegrid')
# sns.jointplot(data=df, x='Sales', y='Commission_Amount',
#               palette='Set1',  kind='scatter')
# plt.show()

#getting mean of comission amount
mean  = df["Commission_Amount"].mean()
# print(mean)

#getting the pct of it pct_to_target between 0.5 and 0.75 and creating a dataframe just for this (not necessary)
pct_between_to_target = df['Pct_To_Target'].between(0.5, 0.75)
pct_df = pd.DataFrame(
    index=range(num_reps), data={'pct_between_to_target': pct_between_to_target,
                                               })

n_btw_numbers = []
n_btw_numbers = pct_df.loc[pct_df['pct_between_to_target'] == True]
# print(n_btw_numbers)


# Define a list to keep all the results from each simulation that we want to analyze
all_stats = []

# Loop through many simulations
for i in range(num_simulations):

    # Choose random inputs for the sales targets and percent to target
    sales_target = np.random.choice(sales_target_values, num_reps, p=sales_target_prob)
    pct_to_target = np.random.normal(avg, std_dev, num_reps).round(2)

    # Build the dataframe based on the inputs and number of reps
    df = pd.DataFrame(index=range(num_reps), data={'Pct_To_Target': pct_to_target,
                                                   'Sales_Target': sales_target})

    # Back into the sales number using the percent to target rate
    df['Sales'] = df['Pct_To_Target'] * df['Sales_Target']

    # Determine the commissions rate and calculate it
    df['Commission_Rate'] = df['Pct_To_Target'].apply(calc_commission_rate)
    df['Commission_Amount'] = df['Commission_Rate'] * df['Sales']

    # We want to track sales,commission amounts and sales targets over all the simulations
    all_stats.append([df['Sales'].sum().round(0),
                      df['Commission_Amount'].sum().round(0),
                      df['Sales_Target'].sum().round(0)])
    
results_df = pd.DataFrame.from_records(all_stats, columns=['Sales',
                                                           'Commission_Amount',
                                                           'Sales_Target',
                                                           ])

results_df.describe().style.format('{:,}')
results_df.head()



