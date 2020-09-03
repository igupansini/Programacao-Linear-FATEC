salarioBase = float(input("Digite o salario para ser calculado o reajuste: "))
porcentagem = "0%"

if salarioBase <= 1280.0:
    reajuste = salarioBase * 0.2
    novoSalario = salarioBase + reajuste
    porcentagem = "20%"

elif salarioBase > 1280.0 and salarioBase <= 1700.0:
    reajuste = salarioBase * 0.15
    novoSalario = salarioBase + reajuste
    porcentagem = "15%"

elif salarioBase > 1700 and salarioBase <= 11500:
    reajuste = salarioBase * 0.1
    novoSalario = salarioBase + reajuste
    porcentagem = "10%"

elif salarioBase > 11500:
    reajuste = salarioBase * 0.05
    novoSalario = salarioBase + reajuste
    porcentagem = "5%"

print("Salario antes do reajuste: R$", salarioBase)
print("Salario reajustado em:", porcentagem)
print("Valor reajustado: R$", reajuste)
print("Novo salario: R$", novoSalario)
