'''Crie um programa que simule o funcionamento de um CAIXA ELETRONICO no inicio, pergunte ao usuário qual será o VALOR A SER SACADO (numeros inteiros) e o programa vai informar quantas
CÉDULAS de cada valor serão entregues.
obs: considere que o caixa possui cédulas de R$50 R$20 R$10 e R$1'''

notas = 50
totalNotas = 0

print('=' * 40)
print('{:^40}'.format('BANCO LUCAS DEV'))
print('=' * 40)
valor = int(input('Que valor você quer sacar? R$'))
totalValor = valor
while True:
    if totalValor >= notas:
        totalValor -= notas
        totalNotas += 1
    else:
        if totalNotas > 0:
            print(f'Total de {totalNotas} cédulas de R${notas}')
        if notas == 50:
            notas = 20
        elif notas == 20:
            notas = 10
        elif notas == 10:
            notas = 1
        totalNotas = 0
        if totalValor == 0:
            break

print('=' * 40)
print('Volte sempre ao BANCO LUCAS DEV!')
