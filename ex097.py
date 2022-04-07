"""Faça um programa que tenha uma FUNÇÃO chamada ESCREVA(), que receba um texto qualquer como PARAMETRO e mostre uma
mensagem com tamanho adaptavel.
Ex: Escreva('Olá Mundo!')
Saída:
~~~~~~~~~~~~
Olá Mundo!
~~~~~~~~~~~~"""

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)



#  Programa Principal
escreva('Lucas Rodrigues')
escreva('Curso de Python no Youtube')
escreva('Olá')