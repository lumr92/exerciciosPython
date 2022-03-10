'''Ecreva um programa que leia a velocidade de um carro, se ele ultrapassar 80km/h, mostre uma mensagem
dizendo que ele foi multado
A multa vai custar R$7,00 por cada km/h acima do limite'''

vel = float(input('Qual é a velocidade do carro? '))
if vel <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (vel - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
    print('Tenha um bom dia! Dirija com segurança!')