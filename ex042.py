'''Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triangulo
será formado:
- EQUILATERO: Todos os lados iguais
- ISOSCELES: Dois lados iguais
- ESCALENO: Todos os lados diferentes'''

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
    if primeiraReta == segundaReta and primeiraReta == terceiraReta and segundaReta == terceiraReta:
        print('Este é um riangulo EQUILÁTERO!')
    elif (primeiraReta == segundaReta) or (segundaReta == terceiraReta) or (terceiraReta == primeiraReta):
        print('Este é um triangulo ISÓSCELES!')
    else:
        print('Este é um triangulo ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')