'''O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos,
faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada'''
from random import sample

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
alunos = [n1, n2, n3, n4]
print('A ordem de apresentação será \n{}'.format(sample(alunos, len(alunos))))