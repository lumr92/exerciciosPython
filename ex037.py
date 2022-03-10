'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
- 1 para binário
- 2 para octal
- 3 para hexadecimal'''

n = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
escolha = int(input('Sua opção: '))
if escolha == 1:
    binario = bin(n)
    print('{} convertido para BINÁRIO é igual a {}'.format(escolha, binario[2:]))
elif escolha == 2:
    octal = oct(n)
    print('{} convertido para OCTAL é igual a {}'.format(escolha, octal[2:]))
elif escolha == 3:
    hexa = hex(n)
    print('{} convertido para HEXADECIMAL é igual a {}'.format(escolha, hexa[2:]))
else:
    print('Opção inválida, tente novamente!')