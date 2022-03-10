'''Crie um programa que leia DOIS VALORES e mostre um MENU na tela:
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NUMEROS
[ 5 ] SAIR DO PROGRAMA
Seu programa deverá realizar a operação solicitada em cada caso'''

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
menu = 0
separaMenu = '-' * 80

while menu != 5:
    print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NUMEROS
[ 5 ] SAIR DO PROGRAMA''')
    menu = int(input('Escolha uma das opções do menu acima: '))
    if menu == 1:
        s = n1 + n2
        print('A opção escolhida foi {}. SOMAR!'.format(menu))
        print('A soma entre {} + {} é: {}, obrigado.'.format(n1, n2, s))
        print(separaMenu)
    elif menu == 2:
        m = n1 * n2
        print('A opção escolhida foi {}. MULTIPLICAR!'.format(menu))
        print('A multiplicação entre {} * {} é: {}, obrigado.'.format(n1, n2, m))
        print('-' * 60)
    elif menu == 3:
        if n1 > n2:
            print('A opção escolhida foi {}. MAIOR!'.format(menu))
            print('O maior número entre {} e {} é {}, obrigado.'.format(n1, n2, n1))
            print(separaMenu)
        if n2 > n1:
            print('A opção escolhida foi {}. MAIOR!'.format(menu))
            print('O maior número entre {} e {} é {}, obrigado.'.format(n1, n2, n2))
            print(separaMenu)
        else:
            print('A opção escolhida foi {}. MAIOR!'.format(menu))
            print('O maior número entre {} e {} não existe, pois os números escolhidos são IGUAIS!'.format(n1, n2))
            print(separaMenu)
    elif menu == 4:
        print('A opção escolhida foi {}. NOVOS NUMEROS!'.format(menu))
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))
        print(separaMenu)
    elif menu == 5:
        print('A opção escolhida foi {}. SAIR DO PROGRAMA, obrigado.'.format(menu))
    else:
        print('Opção inválida, digite uma opção entre as disponíveis no MENU!')
        print(separaMenu)