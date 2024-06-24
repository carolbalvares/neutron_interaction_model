import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.append("../")
from aux_information.diffusion_bucklings import dif_coef
from homogenization.cross_sections import micro_cs_absorption

# Parâmetros
n = 5  # Número de pontos na grade
print("dif_coef", dif_coef)
Δx = 10.0  # Espaçamento da grade
print("micro_cs_absorption", micro_cs_absorption)
micro_cs_absorption = 0.1  # Coeficiente de absorção
S_source = [100000, 0, 0, 0, 0]  # Fonte de partículas em cada ponto

# Criando a matriz tridiagonal M
a = 2 * dif_coef / Δx**2 + micro_cs_absorption
b = -dif_coef / Δx**2
main_diag = [a] * n
off_diag = [b] * (n - 1)

# Utilizando numpy para criar a matriz M
M = np.diag(main_diag) + np.diag(off_diag, k=1) + np.diag(off_diag, k=-1)

# Definindo o vetor S com fontes
S = np.array(S_source)

# Resolvendo o sistema linear
Φ = np.linalg.solve(M, S)

print("Distribuição de partículas Φ:", Φ)


plt.figure(figsize=(10, 2))
plt.title("Distribuição de Partículas na Malha")
plt.imshow(Φ.reshape(1, -1), cmap="viridis", interpolation="nearest", aspect="auto")
plt.colorbar(label='Intensidade de Partículas')
plt.yticks([])  # Oculta os ticks do eixo y
plt.xticks(range(n), labels=[f"Ponto {i+1}" for i in range(n)])
plt.show()