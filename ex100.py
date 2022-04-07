"""Faça um programa que tenha uma LISTA chamada NUMEROS e duas FUNÇÕES chamadas SORTEIO() e SOMAPAR(). A primeira função
vao sortear 5 NUMEROS e vai colocá-los dentro da lista e a segunda função vai mostar a SOMA entre todos os valores PARES
sorteados pela função anterior"""
from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(randint(1, 10))
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos o uso {soma}')



numeros = []
sorteia(numeros)
print(numeros)
somaPar(numeros)
