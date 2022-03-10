'''Fça um programa que jogue PAR OU IMPAR com o computador. o jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele ganhou no final do jogo'''

from random import randint

usuario = ''
computador = ''
usuarioNumero = 0
computadorNumero = 0
somaN = 0
resultado = ''
nVitorias = 0

while True:
    usuarioNumero = int(input('Diga um valor: '))
    usuario = str(input('Par ou Ímpar? [P/I]')).upper().strip()[0]
    computadorNumero = randint(0, 10)
    somaN = usuarioNumero + computadorNumero
    print('-' * 30)
    if somaN % 2 == 0:
        print(f'Você jogou {usuarioNumero} e o computador {computadorNumero}. Total deu {somaN} DEU PAR')
        print('-' * 30)
        resultado = 'P'
    elif somaN % 2 == 1:
        print(f'Você jogou {usuarioNumero} e o computador {computadorNumero}. Total deu {somaN} DEU IMPAR')
        resultado = 'I'
    if resultado != usuario:
        print('Você PERDEU!')
        break
    elif resultado == usuario:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        nVitorias += 1
        print('-' * 30)

print(f'GAME OVER! Você venceu {nVitorias} vezes.')