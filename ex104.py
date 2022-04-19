"""Crie um programa que tenha a FUNÇÃO LEIAINT(), que vai funcionar de forma semelhante a função INPUT() do python, só
que fazendo a VALIDAÇÃO para aceitar apenas um valor numérico.
Ex: n = leiaint('Digite um n: ')"""


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um numero inteiro: ')
print(f'Você acabou de digitar o número {n}')
