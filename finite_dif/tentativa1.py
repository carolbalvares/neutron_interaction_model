import numpy as np
import matplotlib.pyplot as plt

# Definição dos parâmetros (valores aproximados)
dif_coef = 0.16950370743719267  # Coeficiente de difusão
macro_cs_absorption = 1.450667024580102  # Seção de absorção macroscópica

# Parâmetros da grade
n = 5  # Número de pontos na grade
Δx = 10.0  # Espaçamento da grade

# Fonte de partículas em cada ponto
S_source = [100000, 0, 0, 0, 0]

# Construindo a matriz tridiagonal
a = [2 * dif_coef / Δx**2 + macro_cs_absorption] * n  # Coeficientes da diagonal principal
b = [-dif_coef / Δx**2] * (n - 1)  # Coeficientes das diagonais superiores e inferiores

# Algoritmo de Thomas
def thomas_algorithm(a, b, d):
    n = len(d)
    c_prime = [0] * n
    d_prime = [0] * n
    x = [0] * n
    
    # Eliminação progressiva
    c_prime[0] = b[0] / a[0]
    d_prime[0] = d[0] / a[0]
    
    for i in range(1, n):
        denom = a[i] - b[i-1] * c_prime[i-1]
        if i < n - 1:
            c_prime[i] = b[i] / denom
        d_prime[i] = (d[i] - b[i-1] * d_prime[i-1]) / denom
    
    # Substituição retroativa
    x[n-1] = d_prime[n-1]
    for i in range(n-2, -1, -1):
        x[i] = d_prime[i] - c_prime[i] * x[i+1]
    
    return x

# Resolver o sistema
solucao = thomas_algorithm(a, b, S_source)
print("Distribuição de partículas Φ:", solucao)

# Calcular o número de partículas por célula
area_celula = Δx**2
numero_particulas_por_celula = np.array(solucao) * area_celula

print("Número de partículas por célula:", numero_particulas_por_celula)

# Visualização
plt.figure(figsize=(10, 2))
plt.title("Distribuição de Partículas na Malha")
plt.imshow(np.array(solucao).reshape(1, -1), cmap="viridis", interpolation="nearest", aspect="auto")
plt.colorbar(label='Intensidade de Partículas')
plt.yticks([])  # Oculta os ticks do eixo y
plt.xticks(range(n), labels=[f"Ponto {i+1}" for i in range(n)])
plt.show()