'''Desenvolva um programa que leia SEIS NUMEROS INTEIROS e mostre a soma apenas daqueles que forem PARES
se o valor digitado for ÍMPAR, desconsidere-o'''

n = 0
s = 0
for c in range(1, 7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n % 2 == 0:
        s = s + n

print('A soma dos números pares digitados foi: {}'.format(s))
