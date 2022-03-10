'''Crie um programa que leia o ANO DE NASCIMENTO de SETE PESSOAS. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
'''pegando ano atual da maquina'''
anoAtual = date.today().year
menorIdade = 0
maiorIdade = 0

for c in range(1, 8):
    anoNasci = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    '''verificar quantas pessoas não chegaram a maioridade'''
    if anoAtual - anoNasci < 18:
        menorIdade += 1
    else:
        maiorIdade += 1

print('{} não atingiram a maioridade.'.format(menorIdade))
print('{} já são maiores de idade.'.format(maiorIdade))