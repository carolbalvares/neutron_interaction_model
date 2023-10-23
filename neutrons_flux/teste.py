def percorrer_seis_frentes(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    meio_linha = linhas // 2
    meio_coluna = colunas // 2

    # Definir direções
    direcoes = [
        (0, -1),  # Para a esquerda
        (0, 1),   # Para a direita
        (-1, 0),  # Para cima
        (1, 0),   # Para baixo
        (-1, 1),  # Diagonal superior direita
        (1, 1),   # Diagonal inferior direita
        (1, -1),  # Diagonal inferior esquerda
        (-1, -1)  # Diagonal superior esquerda
    ]

    for direcao in direcoes:
        i, j = meio_linha, meio_coluna
        while 0 <= i < linhas and 0 <= j < colunas:
            print(matriz[i][j])
            i += direcao[0]
            j += direcao[1]
            print("0-1",matriz[meio_linha][meio_coluna])

# Exemplo de uso
minha_matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

percorrer_seis_frentes(minha_matriz)