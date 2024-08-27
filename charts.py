data_two_d_1_fuel = np.array([
    [523, 2169, 3572, 2185, 526],
    [2198, 12661, 24161, 12596, 2174],
    [3606, 24215, 49360, 24187, 3568],
    [2171, 12650, 24268, 12612, 2196],
    [513, 2158, 3632, 2171, 527]
])

# Gerar o heatmap usando Seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(data, annot=True, fmt="d", cmap="viridis", cbar_kws={'label': 'Neutron Count'})

# Ajustes do gráfico
plt.title('Heatmap of Neutron Count')
plt.show()