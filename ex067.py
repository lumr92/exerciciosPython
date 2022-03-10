'''Faça um programa que mostre a TABUADA de VARIOS NÚMEROS, um de cada vez, para cada valor digitado pelo usuário. O programa será INTERROMPIDO quando o número solicitado for NEGATIVO.'''

while True:
    n = int(input('Digite um número para ver a sua tabuada: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' * 30)

print('PROGRAMA DE TABUADA ENCERRADO, volte sempre!')
