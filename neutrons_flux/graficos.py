import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = np.array([
    [523.2790045, 2168.93606, 3571.512504, 2185.006363, 525.69736],
    [2197.683749, 12661.42112, 24161.20744, 12595.64045, 2173.572822],
    [3605.617669, 24215.27172, 49360.12361, 24187.01951, 3568.238635],
    [2170.938314, 12650.43138, 24268.28052, 12612.12325, 2195.513602],
    [513.4495979, 2157.760072, 3631.601986, 2171.109212, 526.9307281]
])

# Criando o heatmap
plt.figure(figsize=(10, 8))  # Tamanho da figura
sns.heatmap(data, annot=True, fmt=".2f", cmap="viridis", linewidths=.5)
plt.title('Heatmap de Fluxo de Nêutrons')
plt.show()