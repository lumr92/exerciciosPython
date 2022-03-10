'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL
e CONDIÇÃO DE PAGAMENTO
- a vista dinheiro / cheque: 10% de desconto
- a vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartãp: 20% de juros'''
print('=' * 10, ' LOJÃO DA MIA E DORA ', '=' * 10)
preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] a vista dinheiro/cheque')
print('[ 2 ] a vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    print('O valor da compra com 10% de desconto será de R${:.2f}'.format(preco - (preco * (10/100))))
elif opcao == 2:
    print('O valor da compra com 5% de desconto será de R${:.2f}'.format(preco - (preco * (5/100))))
elif opcao == 3:
    print('O valor da compra será de R${:.2f} dividida em 2x SEM JUROS'.format(preco))
    print('O valor a ser pago em 2x será de R${:.2f} por mês'.format(preco/2))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    preco2 = preco + (preco * (20/100))
    print('Sua compra será parcelada em {}x de R${:.2f} com JUROS'.format(parcelas, preco2/parcelas))
    print('O valor da sua compra é de R${:.2f} e com 20% de juros será de R${:.2f}'.format(preco, preco2))
else:
    print('Não existe esta opção, tente novamente!')