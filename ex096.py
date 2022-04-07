"""Faça um programa que tenha uma função chamada ARÉA(), que receba as dimensões de um terreno retangular (LARGURA x
COMPRIMENTO) e mostre a ÁREA DO TERRENO"""

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')


#  Programa Principal
print('  Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
