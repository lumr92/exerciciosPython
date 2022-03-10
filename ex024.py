'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome SANTO'''

cid = input('Em que cidade você nasceu? ').strip()
cid = cid.lower()
print('{}'.format(cid[:5] == 'santo'))
