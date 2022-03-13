'''Crie um programa que vai gerar 5 NUMEROS ALEATORIOS e colocar em uma TUPLA.
Depois disso, mostre a LISTAGEM DE NÚMEROS gerados e também indique o MENOR e o MAIOR valor que estão na tupla'''
from random import randint

numeroAleatorio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

for n in numeroAleatorio:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeroAleatorio)}')
print(f'O menor valor sorteado foi {min(numeroAleatorio)}')
