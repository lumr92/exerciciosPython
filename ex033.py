'''Faça um programa que leia três numeros e mostre qual é o maior e qual é o menor'''

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
if n1 < n2 and n1 < n3:
    menorValor = n1
    print('O menor valor digitado foi {}'.format(menorValor))
elif n2 < n1 and n2 < n3:
    menorValor = n2
    print('O menor valor digitado foi {}'.format(menorValor))
elif n3 < n1 and n3 < n2:
    menorValor = n3
    print('O menor valor digitado foi {}'.format(menorValor))
if n1 > n2 and n1 > n3:
    maiorValor = n1
    print('O maior valor digitado foi {}'.format(maiorValor))
elif n2 > n1 and n2 > n3:
    maiorValor = n2
    print('O maior valor digitado foi {}'.format(maiorValor))
elif n3 > n1 and n3 > n2:
    maiorValor = n3
    print('O maior valor digitado foi {}'.format(maiorValor))