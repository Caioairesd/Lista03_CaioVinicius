#11- Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
#Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km,
#e R$ 0,45 para viagens mais longas.

distancia = float(input("Qual a distância que você deseja percorrer?(KM)"))

#Valor em R$ da taxação.

#Se for até 200 Km
taxaAbaixo = 0.50

#Se for acima 200 Km
taxaAcima = 0.45

if distancia <= 200:
    calculo = distancia * taxaAbaixo
    print("O valor da sua viagem será: R$",calculo)

if distancia > 200:
    calculo = distancia * taxaAcima
    print("O valor da sua viagem será: R$",calculo)

print("Caio Vinicius Aires da Silva")
