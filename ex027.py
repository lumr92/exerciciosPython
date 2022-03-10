'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e ultimo
nome separadamente'''

nome = input('Digite seu nome completo: ').strip()
print('Muito prazer em te conhecer!')
div = nome.split()
print('Seu primeiro nome é {}'.format(div[0]))
print('Seu ultimo nome é {}'.format(div[len(div)-1]))
