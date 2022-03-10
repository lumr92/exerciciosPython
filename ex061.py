'''Refaça o DESAFIO 051, lendo o PRIMEIRO TERMO e a RAZÃO de uma PA, mostrando os 10 PRIMEIROS TERMOS da progressão
usando a estrutura while'''

print('=' * 30)
print('     10 TERMOS DE UMA PA      ')
print('=' * 30)

pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
cont = 1
termo = pt
while cont <= 10:
        print('{} -> '.format(termo), end='')
        cont += 1
        termo += r
print('ACABOU')

