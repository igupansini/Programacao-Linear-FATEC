continuar = True
somaTemperaturas = 0.0
cont = 0
maiorTemperatura = 0.0

while continuar == True:
    temperatura = float(input("Digite a temperatura: "))
    cont = cont + 1
    somaTemperaturas = somaTemperaturas + temperatura
    if temperatura >= maiorTemperatura:
        maiorTemperatura = temperatura
    
    resposta = input("Deseja continuar? Digite (s/n): ")
    if resposta != "s":
        continuar = False
        mediaTemperaturas = somaTemperaturas / cont
        print("\nTotal de temperaturas inseridas:", cont)
        print("Media das temperaturas inseridas:", mediaTemperaturas)
        print("Maior temperatura inserida:", maiorTemperatura)
