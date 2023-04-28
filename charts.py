import matplotlib.pyplot as plt
from discretizacao1Dalt import * 

#ploting graph using discretizacao1Dalt
#1 way
plt.plot(column_index,column_values)
plt.xlabel('sample')
plt.ylabel('value')
plt.title("sample x value")
plt.show()

#2 way
plt.bar(column_index, samples_df.values.reshape(len(samples_df)), color ='red', width = 0.4)
plt.show()

#3 way
plt.scatter(column_index,column_values)
plt.show()