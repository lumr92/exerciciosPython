'''Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
from random import randint
from time import sleep

print('-=-' * 25)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
resp = randint(0, 5)
print('-=-' * 25)
adv = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if adv == resp:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(resp, adv))
