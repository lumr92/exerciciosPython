'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
formar um triangulo'''

print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)
primeiraReta = float(input('Primeiro segmento: '))
segundaReta = float(input('Segundo segmento: '))
terceiraReta = float(input('Terceiro segmento: '))
soma1 = primeiraReta + segundaReta
soma2 = primeiraReta + terceiraReta
soma3 = terceiraReta + segundaReta
if soma1 > terceiraReta and soma2 > segundaReta and soma3 > primeiraReta:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
