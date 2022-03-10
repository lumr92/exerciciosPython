'''Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar'''

n = int(input('Me diga um número qualquer: '))
if n % 2 == 1:
    print('O numero {} é ÍMPAR'.format(n))
else:
    print('O numero {} é par'.format(n))