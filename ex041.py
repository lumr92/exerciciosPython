'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e
mostre sua categoria, de acordo com a idade:
- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: junior
- até 20 anos: senior
- acima: master'''
from datetime import date

anoNasc = int(input('Ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc
print('O atleta tem {} anos.'.format(idade))
if idade < 9:
    print('Classificação: MIRIM')
elif idade >= 9 and idade < 14:
    print('Classificação: INFANTIL')
elif idade >= 14 and idade < 19:
    print('Classificação: JUNIOR')
elif idade >= 19 and idade < 20:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')