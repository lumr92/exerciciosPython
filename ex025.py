'''Crie um programa que leia o nome de uma pessoa e diga se tem SILVA no nome'''

nome = input('Qual é o seu nome completo? ').strip()
nome = nome.upper()
print('Seu nome tem Silva? {}'.format('SANTO' in nome))
