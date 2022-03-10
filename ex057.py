'''Faça um programa que leia o SEXO de uma pessoa, mas só aceite os valores M ou F. caso esteja errado,
peça a digitação novamente até ter um valor correto'''

c = 0
sexo = str(input('Qual é o seu sexo? [M/F] ')).upper().strip()[0]

while sexo not in 'MmFf':
    if sexo != 'M' and sexo != 'F':
        sexo = str(input('Digite M para masculino e F para feminino, tente novamente: [M/F]')).strip().upper()[0]

print('Sexo {} registrado com sucesso!'.format(sexo))


