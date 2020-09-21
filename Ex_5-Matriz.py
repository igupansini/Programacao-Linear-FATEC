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

a = [[1, -1, 0], [2, 3, 4], [0, 1, -2]]
a_transposta = matrizTransposta(a)
b = somarDuasMatrizes(a, a_transposta)

print(a)
print(a_transposta)
print(b)
