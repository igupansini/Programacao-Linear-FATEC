def nomeReverso(nome):
    return nome[::-1]

nome = input("Digite seu nome: ")

print("Seu nome de trás para frente é:", nomeReverso(nome.upper()))