'''Faça um programa que mostra na tela uma CONTAGEM REGRESSIVA para o estouro de fogos de artifício, indo
de 10 ATÉ 0, com uma pausa de 1 SEGUNDO entre eles.'''
from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)

print('SHOW DE FOGOS NA PRAIA DE BOA VIAGEM!!!')