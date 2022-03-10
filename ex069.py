'''Crie um programa que leia a IDADE e o SEXO de VÁRIAS PESSOAS. a cada pessoa cadastrada, o programa deverá se o USUÁRIO quer ou não continuar. no final, mostre:
A) Quantas pessoas tem mais de 18 ANOS
B) Quantos HOMENS foram cadastrados
C) Quantas MULHERES tem menos de 20 ANOS'''

mulheresMenos20 = 0
pessoas18Mais = 0
homens = 0
sexo = ''
idade = 0
continuar = ''

while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade? '))
    sexo = str(input('Sexo? [F/M] ')).upper().strip()[0]
    if idade >= 18:
        pessoas18Mais += 1
    if idade < 20 and sexo == 'F':
        mulheresMenos20 += 1
    if sexo == 'M':
        homens += 1
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {pessoas18Mais}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheresMenos20} mulheres com menos de 20 anos')