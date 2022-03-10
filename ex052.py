'''Faça um programa que leia um NUMERO INTEIRO e diga se ele é ou não um NUMERO PRIMO'''

n = int(input('Digite um numero: '))
mult = 0

for c in range(2, n):
    if n % c == 0:
       mult += 1

if mult == 0:
    print('É primo!')
else:
    print('{} não é primo!'.format(n))