# Regra
print("Hello World!")

# Variaveis
carros = ["Ferrari", "BMW", "Audi"]
temperatura = 27.0
idade = 17

# Funções
def somaDoisNumeros(numA, numB):
    soma = numA + numB
    return soma

# Modificando Lista
carros[0] = "Uno de firma com escada"

# Entrada de dados
nome = input("Digite seu nome: ")

# Saida de dados com alguns métodos basicos de string
print("Seu nome é " + nome.upper())
print(carros[0])
print(somaDoisNumeros(15, 60))
print(len(nome))

# Condicionais
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# Laços
while idade < 20:
    idade += 1
    print(idade)

for marca in carros:
    print(marca)

# Exibindo tipo da variavel
print(type(idade))
print(type(temperatura))
print(type(nome))
