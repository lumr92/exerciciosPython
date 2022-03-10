'''Crie um programa que leia um VARIOS NUMEROS inteiros pelo teclado, o programa só vai parar quando o usuário digitar
o valor 999, que é a CONDIÇÃO DE PARADA. No final mostre QUANTOS NUMEROS foram digitados e qual foi a SOMA entre eles
DESCONSIDERANDO A FLAG'''

n = cont = somaCont = 0
n = int(input('Digite um número: '))
while n != 999:
    cont += 1
    somaCont += n
    n = int(input('Digite um número: '))

print('Foram digitados {} numeros e a soma entre eles é de {}'.format(cont, somaCont))