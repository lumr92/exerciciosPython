'''Faça um programa que leia NOME E PESO de VÁRIAS PESSOAS, guardando tudo em uma LISTA. No final mostre:
A) QUANTAS pessoas foram cadastradas.
B) Uma listagem com as pessoas mais PESADAS
C) Uma listagem com as pessoas mais LEVES'''

temporaria = []
principal = []
maior = menor = 0

while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi de {maior}kg. Peso de', end=' ')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor}kg. Peso de ', end=' ')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')