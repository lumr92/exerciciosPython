'''Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO de uma PA. No final, mostre os 10 primeiros
termos dessa progressão'''

print('=' * 30)
print('     10 TERMOS DE UMA PA      ')
print('=' * 30)
pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
decimo = pt + (10 - 1) * r

for c in range(pt, decimo + r, r):
    print(pt, '->', end=' ')
    pt = pt + r

print('ACABOU')