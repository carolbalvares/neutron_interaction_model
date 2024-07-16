import numpy as np

# Criar uma matriz 10x10 com valores aleatórios
original_matrix = np.random.randint(0, 100, (10, 10))
print("Matriz Original 10x10:\n", original_matrix)

# Inicializar a nova matriz 5x5
new_matrix = np.zeros((5, 5), dtype=int)

# Definindo o fator de escala
scale_factor = 2  # Como estamos reduzindo de 10x10 para 5x5

# Preencher a nova matriz
for i in range(5):
    for j in range(5):
        # Calcular a soma de um subconjunto da matriz original
        block_sum = np.sum(original_matrix[i*scale_factor:(i+1)*scale_factor, j*scale_factor:(j+1)*scale_factor])
        new_matrix[i, j] = block_sum

print("Matriz Reduzida 5x5:\n", new_matrix)
