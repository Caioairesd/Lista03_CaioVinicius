#10- Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
#Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, de 15%.

salario = float(input("Insira o valor do seu salário?"))

#Indicadores de porcentagem para cada classe salarial:

#Salarios acima do definido:
SalMenor = 10/100

#Salários abaixo do definido:
SalMaior = 15/100

if salario > 1250.00:
    aumento = salario * SalMenor
    print("Seu salário aumentou: R$",(round.aumento,2),", e está em: R$",salario + aumento)
else:
    aumento = salario * SalMaior
    print("Seu salário aumentou: R$",aumento,", e está em: R$",salario + aumento)

print("Caio Vinicius Aires da Silva")