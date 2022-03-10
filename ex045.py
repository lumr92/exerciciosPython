'''Crie um programa que faça o computador jogar JOKENPO com voce'''
import random
from time import sleep
print('''Suas opções:
PEDRA
PAPEL
TESOURA''')
usuario = input('Qual é a sua escolha? ').upper()

if usuario != 'PEDRA' and usuario != 'PAPEL' and usuario != 'TESOURA':
    print('Escolha errada, tente novamente!')
else:
    escolhas = ['PEDRA', 'PAPEL', 'TESOURA']
    pc = random.choice(escolhas)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)
    print('O computador escolheu {}'.format(pc))

    if (usuario == 'PEDRA' and pc == 'PAPEL') or (usuario == 'PAPEL' and pc == 'TESOURA') or (usuario == 'TESOURA'
                                                                                          and pc == 'PEDRA'):
        print('-=' * 11)
        print('COMPUTADOR VENCE!')
        print('-=' * 11)


    elif (pc == 'PEDRA' and usuario == 'PAPEL') or (pc == 'PAPEL' and usuario == 'TESOURA') or (pc == 'TESOURA'
                                                                                            and usuario == 'PEDRA'):
        print('-=' * 11)
        print('JOGADOR VENCEU!')
        print('-=' * 11)


    elif (pc == 'PEDRA' and usuario == 'PEDRA') or (pc == 'PAPEL' and usuario == 'PAPEL') or (pc == 'TESOURA'
                                                                                            and usuario == 'TESOURA'):
        print('-=' * 11)
        print('EMPATE, tentem novamente!!')
        print('-=' * 11)