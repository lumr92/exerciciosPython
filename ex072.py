'''Crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem por extensão, de ZERO até VINTE'''

contagem = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
            'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
continuar = ''

while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {contagem[n]}')
    else:
        print('Tente novamente... ', end='')
        n = int(input('Digite um numero entre 0 e 20: '))
    continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('Você escolheu não digitar mais números.')