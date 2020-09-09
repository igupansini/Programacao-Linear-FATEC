carrosConsumo = {"Ferrari": 9.0, "BMW": 11.0, "Audi": 13.0, "Mercedes-Benz": 14.0, "Porsche": 12.0}
menorConsumo = 0.0

for carro in carrosConsumo:
    if carrosConsumo[carro] >= menorConsumo:
        menorConsumo = carrosConsumo[carro]
        carroEconomico = carro

print("O carro mais econômico é o(a)", carroEconomico,"faz", menorConsumo, "kms com um litro de combustível.")
