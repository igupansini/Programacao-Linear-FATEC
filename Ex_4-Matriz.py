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

def somarTresMatrizes(matriz1, matriz2, matriz3):
    matriz_soma = []
    quant_linhas = len(matriz1)  
    quant_colunas = len(matriz1[0])  
    for i in range(quant_linhas):
        matriz_soma.append([])
        for j in range(quant_colunas):
            soma = matriz1[i][j] + matriz2[i][j] + matriz3[i][j]
            matriz_soma[i].append(soma)
    return matriz_soma

a = [[0, 3], [2, -5]]
b = [[-2, 4], [0, -1]]
c = [[4, 2], [-6, 0]]

print(somarDuasMatrizes(a, b))
print(somarDuasMatrizes(a, c))
print(somarTresMatrizes(a, b, c))
