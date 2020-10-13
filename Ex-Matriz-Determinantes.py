def criarMatriz(quant_linhas, quant_colunas):
    matriz = []
    for i in range(quant_linhas):
        linha = []
        for j in range(quant_colunas):
            valor = int(input("Digite o elemento ["+str(i)+"]["+str(j)+"]"))
            linha.append(valor)
        matriz.append(linha)
    return matriz


def verificarMatrizQuadrada(matriz):
    quant_linhas = len(matriz)
    quant_colunas = len(matriz[0])
    if quant_linhas == quant_colunas:
        return True
    else:
        return False


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


def calcularDeterminante(matriz, ordem):
    if ordem == 1:
        determinante = matriz[0][0]
        return determinante

    elif ordem == 2:
        principal, secundaria = 1, 1
        for i in range(ordem):
            for j in range(ordem):
                if i == j:
                    principal *= matriz[i][j]
                else:
                    secundaria *= matriz[i][j]
        determinante = principal - secundaria
        return determinante

    elif ordem == 3:
        principais = ((matriz[0][0] * matriz[1][1] * matriz[2][2]) +
                      (matriz[0][1] * matriz[1][2] * matriz[2][0]) +
                      (matriz[0][2] * matriz[1][0] * matriz[2][1]))
        secundarias = ((matriz[0][2] * matriz[1][1] * matriz[2][0]) +
                       (matriz[0][0] * matriz[1][2] * matriz[2][1]) +
                       (matriz[0][1] * matriz[1][0] * matriz[2][2]))
        determinante = principais - secundarias
        return determinante


matrizCriada = criarMatriz(2, 2)
matrizA = [[1, -1, 0], [2, 3, 4], [0, 1, -2]]
matrizB = [[2, 7, 2], [8, -1, -3], [-1, 9, 5]]
matrizA_Transposta = matrizTransposta(matrizA)
somaEx = somarDuasMatrizes(matrizB, matrizA_Transposta)
multiplicacaoEx = multiplicarMatrizes(matrizA, somaEx)
resultadoEx = calcularDeterminante(multiplicacaoEx, len(multiplicacaoEx))

print(matrizCriada)
print(verificarMatrizQuadrada(matrizCriada))
print(matrizA_Transposta)
print(somaEx)
print(multiplicacaoEx)
print(resultadoEx)
