'''Escreva um programa que leia um NUMERO N inteiro qualquer e mostre na tela os N primeiros elementos de uma SEQUENCIA
DE FIBONACCI'''

print('-' * 60)
print('SEQUENCIA DE FIBONACCI')
print('-' * 60)
n = int(input('Quantos termos você quer mostrar? '))
print('~' * 50)
cont = 1
primeiroValor = 0
segundoValor = 1
valoresSeguintes = 0
print('{} -> '.format(primeiroValor), end='')
print('{} -> '.format(segundoValor), end='')
while cont < n - 1:
    valoresSeguintes = primeiroValor + segundoValor
    print('{} -> '.format(valoresSeguintes), end='')
    primeiroValor = segundoValor
    segundoValor = valoresSeguintes
    cont += 1
print('FIM')
print('~' * 50)