'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas'''

km = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(km))
if km <= 200:
    passagem = km * 0.5
    print('E o preço da sua passagem será de R${:.2f}'.format(passagem))
else:
    passagem = km * 0.45
    print('E o preço da sua passagem será de R${:.2f}'.format(passagem))
