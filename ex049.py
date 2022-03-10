'''Refaça o DESAFIO 009, mostrando a TABUADA de um número que o usuário escolher, só que agora
utilizando o LAÇO FOR'''

n = int(input('Digite um número para ver sua tabuada: '))
print('-' * 13)
for c in range(0, 11):
    print('{} x {:2} = {}'.format(n, c,  n * c))
print('-' * 13)