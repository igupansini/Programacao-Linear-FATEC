carrosConsumo = {"Ferrari": 9.0, "BMW": 11.0, "Audi": 13.0, "Mercedes-Benz": 14.0, "Porsche": 12.0}
menorConsumo = 0.0
distancia = 1000.0
litrosCombustivel = 0.0
valorGasolina = 4.25

for carro in carrosConsumo:
    if carrosConsumo[carro] >= menorConsumo:
        menorConsumo = carrosConsumo[carro]
        carroEconomico = carro
for carro in carrosConsumo:
    litrosCombustivel = distancia / carrosConsumo[carro]
    custoTotal = litrosCombustivel * valorGasolina
    print(carro, "consome", round(litrosCombustivel, 2), "litros para percorrer 1.000 quilômetros.")
    print(carro, "gastará um total de R$", round(custoTotal, 2), "\n")

print("O carro mais econômico é o(a)", carroEconomico,"faz", menorConsumo, "kms com um litro de combustível.")
