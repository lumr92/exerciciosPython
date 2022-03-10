'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo
retangulo calcule e mostre o comprimento da hipotenusa'''
from math import hypot

catop = float(input('Comprimento do cateto oposto: '))
catadj = float(input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}'.format(hypot(catop, catadj)))