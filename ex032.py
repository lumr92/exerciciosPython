'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto'''
import datetime

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) and (ano != 0):
    print('O ano {} é BISSEXTO'.format(ano))
elif ano == 0:
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    anoAtual = (int(year))
    if(anoAtual % 4 == 0 and anoAtual % 100 != 0) or (anoAtual % 400 == 0):
        print('O ano {} é BISSEXTO'.format(anoAtual))
    else:
        print('O ano {} NÃO é BISSEXTO'.format(anoAtual))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))

'''currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
anoAtual = (int(year))
print(anoAtual)'''