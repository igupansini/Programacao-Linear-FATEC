def somarDuasMatrizes(matriz1, matriz2):
    matriz_soma = []
    quant_linhas = len(matriz1)
    quant_colunas = len(matriz1[0])
    for i in range(quant_linhas):
        matriz_soma.append([])
        for j in range(quant_colunas):
            soma = matriz1[i][j] + matriz2[i][j]
            matriz_soma[i].append(soma)
    return matriz_soma


def matrizTransposta(matriz):
    matriz_transposta = []
    for j in range(len(matriz[0])):
        aux = []
        for i in range(len(matriz)):
            aux.append(matriz[i][j])
        matriz_transposta.append(aux)
    return matriz_transposta


def multiplicarMatrizes(matriz1, matriz2):
    quant_linhas_1 = len(matriz1)
    quant_colunas_1 = len(matriz1[0])
    quant_linhas_2 = len(matriz2)
    quant_colunas_2 = len(matriz2[0])
    assert quant_colunas_1 == quant_linhas_2
    aux = []

    for linha in range(quant_linhas_1):
        aux.append([])
        for coluna in range(quant_colunas_2):
            aux[linha].append(0)
            for i in range(quant_colunas_1):
                aux[linha][coluna] += matriz1[linha][i] * matriz2[i][coluna]
    return aux


matriz_A = [[2, 1], [-3, 4]]
matriz_B = [[0, -1], [2, 5]]
matriz_C = [[3, 0], [6, 1]]
matriz_AB = somarDuasMatrizes(matriz_A, matriz_B)

ex_1 = multiplicarMatrizes(matriz_A, matriz_B)
ex_2 = multiplicarMatrizes(matriz_AB, matriz_C)
# ex_3 =

print(ex_1)
print(ex_2)
