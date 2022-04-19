"""Faça um programa que tenha uma FUNÇÃO chamada FICHA(), que receba dois PARAMETROS OPCIONAIS: o NOME de um jogador e
quantos GOLS ele marcou.
O programa deverá ser capaz de mostrar a FICHA DO JOGADOR, mesmo que algum dado não tenha sido informado corretamente."""


def ficha(jogador='<desconhecido>', gol=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


# Programa Principal
nome = str(input('Nome do jogador: '))
gols = str(input('Numero de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)