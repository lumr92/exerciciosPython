'''Faça um programa que calcule a SOMA entre todos os NUMEROS IMPARES que são MULTIPLOS DE TRES e
que se encontram no intervalo de 1 até 500'''

s = 0
c2 = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c
        c2 = c2 + 1

print('A soma de todos os {} valores solicitados é {}'.format(c2, s))
