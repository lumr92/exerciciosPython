''''Faça um programa que leia 5 VALORES NUMÉRICOS e guarde-os em uma LISTA
No final, mostre qual foi o MAIOR e o MENOR valor digitado e as suas respectivas POSIÇÕES na lista'''

valores = []
maxValor = 0
minValor = 0

for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        maxValor = valores[cont]
        minValor = valores[cont]
    else:
        if valores[cont] > maxValor:
            maxValor = valores[cont]
        if valores[cont] < minValor:
            minValor = valores[cont]

print('-=' * 20)
print(f'Vocẽ digitou os valores {valores}')
print(f'O maior valor digitado foi {maxValor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maxValor:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {minValor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == minValor:
        print(f'{i}...', end='')
