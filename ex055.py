'''Faça um programa que leia o PESO de CINCO PESSOAS no final, mostre qual foi o MAIOR e o MENOR peso lido'''

maiorPeso = 0
menorPeso = 0

for c in range(1, 6):
    peso = float(input('Peso da {} pessoa: (kg) '.format(c)))
    if c == 1:
        maiorPeso = peso
        menorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso

print('O maior peso entre as pessoas foi de {:.2f}kg'.format(maiorPeso))
print('O menor peso entre as pessoas é de {:.2f}kg'.format(menorPeso))