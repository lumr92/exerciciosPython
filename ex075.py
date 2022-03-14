'''Desenvolva um programa que leia QUATRO VALORES pelo TECLADO e guarde-os em uma TUPLA. No final mostre:
A) Quantas vezes aparece o valor 9
B) Em que posição foi digitado o primeiro valor 3
C)Quais foram os números PARES.'''

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))
n4 = int(input('Digite o ultimo numero: '))
valores = (n1, n2, n3, n4)

print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição!')
print(f'Os valores pares digitados foram ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=' ')