'''Faça um programa que leia um NUMERO qualquer e mostre o seu fatorial'''

cont = 0
n1 = int(input('Digite um numero: '))
somaFatorial = 0

print('{}! = {} x '.format(n1, n1), end='')
cont = n1 - 1
somaFatorial = n1 * cont
while cont != 0:
    print('{} x '.format(cont), end='')
    cont -= 1
    if cont != 0:
        somaFatorial *= cont
print('= {}'.format(somaFatorial))