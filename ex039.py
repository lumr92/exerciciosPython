'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda VAI SE ALISTAR ao serviço militar
- Se é a HORA DE SE ALISTAR
- Se já PASSOU DO TEMPO de se alistar
Seu programa deverá também mostrar o tempo  que falta ou que passou do prazo'''

from datetime import date

anoNasc = int(input('Qual o seu ano de nascimento: '))
anoAtual = date.today().year
if anoNasc > (anoAtual - 18):
    print('Ainda faltam {} anos para o alistamento.'.format((anoNasc + 18) - anoAtual))
    print('Seu alistamento será em {}'.format(anoNasc + 18))
elif anoNasc == anoAtual - 18:
    print('Você está na idade de se alistar.')
else:
    print('Você já passou do tempo de se alistar a {} anos.'.format(anoAtual - (anoNasc + 18)))
    print('Seu período de alistamento militar foi no ano de {}'.format(anoNasc + 18))