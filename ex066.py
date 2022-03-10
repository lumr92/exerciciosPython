'''Crie um programa que leia VARIOS NUMEROS inteiros pelo teclado. o programa só vai parar quando o usuário digitar o valor 999, que é a CONDIÇÃO DE PARADA. No final, mostre QUANTOS NUMEROS
foram digitados e qual foi a SOMA entre eles (Desconsiderando  a flag)'''

somaN = 0
somaCont = 0

while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    somaCont += 1
    somaN += n

print(f'Foram digitados {somaCont} números e a soma entre eles foi de {somaN}')
