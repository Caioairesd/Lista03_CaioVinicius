#08- Escreva um programa que pergunte a velocidade do carro de um usuário.
#Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
#Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

velocidade = int(input("Qual velocidade você estava? (km/h)"))
if velocidade > 80:
    
    #Você pode alterar a velocidade permitida alterando a variável (acima).
    acima = velocidade - 80
    multa = acima * 5
    print("Você foi multado em:R$",multa,"Por estar com:", velocidade, "KM/H")  
else:
    print("Você estava dentro do limite permitido, Parabéns!")

print("Caio Vinicius Aires da Silva")