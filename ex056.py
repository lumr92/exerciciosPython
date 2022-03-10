'''Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 pessoas, no final do programa mostre:
- a MÉDIA DE IDADE do grupo
- quantas mulheres tem MENOS DE 20 ANOS
- qual é o homem MAIS VELHO do grupo'''

somaIdades = 0
mulheresMenos20 = 0
homemMaisVelho = ''
idadeHomemMaisVelho = 0

for c in range(1, 5):
    nome = str(input('Qual o nome da {}ª pessoa? '.format(c)))
    idade = int(input('Qual é a idade da {}ª pessoa? '.format(c)))
    sexo = str(input('Qual o sexo da {}ª pessoa? (m/f) '.format(c))).upper()
    if idade < 20 and sexo == 'F':
        mulheresMenos20 += 1
    if c == 1 and sexo == 'M':
        homemMaisVelho = nome
        idadeHomemMaisVelho = idade
    if sexo == 'M' and idade > idadeHomemMaisVelho:
        homemMaisVelho = nome
        idadeHomemMaisVelho = idade
    somaIdades = somaIdades + idade

print('A média de idade do grupo é de {} anos'.format(somaIdades/4))
print('No grupo existem {} mulher(es) menor(es) de 20 anos'.format(mulheresMenos20))
print('O homem mais velho do grupo tem {} e se chama {}'.format(idadeHomemMaisVelho, homemMaisVelho))