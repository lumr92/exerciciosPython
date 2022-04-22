"""Reescreva a função LEIAINT() que fizemos no DESAFIO 104, incluindo agora a possibilidade da digitação de um número
de tipo inválido.
Aproveite e crie também uma função LEIAFLOAT() com a mesma funcionalidade"""


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada interrompida pelo usuário.\033[m')
            break
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mEntrada interrompida pelo usuário.\033[m')
            break
        else:
            return n


num = leiaint('Digite um valor: ')
num2 = leiafloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {num}')
print(f'O valor real digitado foi {num2}')