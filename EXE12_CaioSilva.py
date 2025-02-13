#12- Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
#Você deve poder calcular a soma (+), subtração (-), multiplicação (*) e divisão (/).
#Exiba o resultado da operação solicitada. (usar ELIF)

n1 = float(input("Insira seu primeiro valor:"))
n2 = float(input("Insira seu segundo valor:"))
 
operacao = input("Insira qual operação você deseja fazer: \nSoma(+), subtração (-), multiplicação (*) e divisão (/):")

#As variáveis podem ser alteradas se for necessário adicionar mais números nas operações.

if operacao == '+':
    resultado = n1 + n2
    print("RESULTADO:",resultado)
elif operacao == '-':
    resultado = n1 - n2
    print("RESULTADO:",resultado)
elif operacao == '*':
    resultado = n1 * n2
    print("RESULTADO:",resultado)
elif operacao == '/':
    resultado = n1 / n2
    print("RESULTADO:",resultado)

print("Caio Vinicius Aires da Silva")


