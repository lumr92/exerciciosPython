"""Faça um programa que ajude um jogador da MEGASENA a criar PALPITES. O programa vai perguntar QUANTOS JOGOS serão
gerados e vai sortear 6 NUMEROS ENTRE 1 E 60 para cada jogo, cadastrando tudo em uma LISTA COMPOSTA."""

# importando a biblioteca random para utilizar os valores randomicos da megasena
from random import randint
# importando a biblioteca time para simular o pc "pensando" para gerar os numeros dos jogos
from time import sleep

# variaveis
valores = []
jogos = []  # variavel para listar os jogos sorteados
print('-' * 30)
print('      JOGA NA MEGA SENA        ')
print('-' * 30)
quantJogos = int(input('Quantos jogos você quer sortear? '))
totJogos = 1
while totJogos <= quantJogos:
    contador = 0
    while True:
        numero = randint(1, 60)  # variavel recebendo um numero sorteado de 1 a 60
        if numero not in valores:  # estrutura condicional para verificar se na lista valores existe o numero sorteado
                                    #se não tiver, adicionar na lista, ao final adiciona mais um ao contador até chegar em 6
            valores.append(numero)
            contador += 1
        if contador >= 6:
            break
    valores.sort()
    jogos.append(valores[:])  # copiando os valores da lista valores para a lista jogos
    valores.clear()  # apagando a lista valores para adicionar um novo jogo
    totJogos += 1

print('-=' * 3, f' SORTEANDO {quantJogos} JOGOS ', '=-' * 3)
for indice, lista in enumerate(jogos):  # estrutura de repetição para imprimir na tela de forma vertical os jogos sorteados
    print(f'Jogo {indice + 1}: {lista}')
    sleep(1)
print('-=' * 5, ' < BOA SORTE! > ', '=-' * 5)
