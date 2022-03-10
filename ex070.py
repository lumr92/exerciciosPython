'''Crie um programa que leia o NOME e o PREÇO de VARIOS PRODUTO. O programa deverá perguntar se o USUÁRIO vai continuar. No final, mostre:
A)Qual é o TOTAL GASTO na compra
B)Quantos produtos custam MAIS DE R$ 1000
C)Qual é o NOME do produto mais BARATO'''

totalCompra = menorPreco = nomeProdutoMenorPreco = maisde1000 = contador = 0

while True:
    nomeProduto = str(input('Qual o nome do produto: '))
    preco = float(input('Ṕreço: R$'))
    contador += 1
    if contador == 1:
        menorPreco = preco
    if preco > 1000:
        maisde1000 += 1
    totalCompra += preco
    if preco <= menorPreco:
        menorPreco = preco
        nomeProdutoMenorPreco = nomeProduto
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if cont == 'N':
        print('{:-^40}'.format(' FIM DO PROGRAMA '))
        break

print(f'O total da compra foi R${totalCompra:.2f}')
print(f'Temos {maisde1000} produto custando mais de R$1000,00')
print(f'O produto mais barato foi {nomeProdutoMenorPreco} que custa R${menorPreco:.2f}')