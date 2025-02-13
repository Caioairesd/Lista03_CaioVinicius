#09- Escreva um programa que faça o cálculo do imposto de renda 2025. Consulte a tabela no site da Receita federal.

salario = float (input("Insira seu salário:"))

if salario <= 2259.20:
    print("Você não precisa pagar.")
elif salario >= 2259.21 and salario <= 2826.65:
    aumento = salario *0.075
    print("Você deve pagar: R$",round(aumento,2))
elif salario >= 2826.66 and salario <= 3751.05:
    aumento = salario *0.15
    print("Você deve pagar: R$",round(aumento,2))
elif salario >= 3751.06 and salario <= 4664.68:
    aumento = salario *0.225
    print("Você deve pagar: R$",round(aumento,2))
elif salario > 4664.69:
    aumento = salario *0.275
    print("Você deve pagar: R$",round(aumento,2))

print("Caio Vinicius Aires da Silva")