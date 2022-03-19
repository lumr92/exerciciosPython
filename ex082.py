'''Crie um programa que vai ler vários números e colocar em uma LISTA.
Depois disso, crie DUAS LISTAS EXTRAS que vão conter apenas os valores PARES e os valores IMPARES digitados respectivamente.
Ao final, mostre o conteúdo das TRÊS LISTAS geradas.'''

valores = []
valoresP = []
valoresI = []

while True:
    valores.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        valoresP.append(v)
    elif v % 2== 1:
        valoresI.append(v)
print('-=' * 30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {valoresP}')
print(f'A lista de ímpares é {valoresI}')