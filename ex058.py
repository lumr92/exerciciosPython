'''Melhore o jogo do DESAFIO 028 onde o computador vai PENSAR em um NUMERO ENTRE O 0 E 1O. só que agora
o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer'''

from random import randint
from time import sleep

contPalp = 0
usuario = 99

print('-=-' * 25)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
computador = randint(0, 10)
while usuario != computador:
    print('-=-' * 25)
    usuario = int(input('Em que número eu pensei? '))
    print('PROCESSANDO...')
    sleep(1)
    if usuario < computador:
        print('Mais... tente novamente!')
    if usuario > computador:
        print('Menos... tente novamente!')
    contPalp += 1

print('PARABÉNS eu escolhi o número {}! Você conseguiu me vencer em {} tentativas!'.format(computador, contPalp))