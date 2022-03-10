'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. o programa vai
perguntar o VALOR DA CASA, o SALÁRIO do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado'''

valorCasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anosFinanc = int(input('Quantos anos de financiamento? '))
prestacao = valorCasa / (anosFinanc * 12)
maxDescontado = salario * (30/100)
if prestacao > maxDescontado:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}\nEmpréstimo NEGADO!'
          .format(valorCasa, anosFinanc, prestacao))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}\nEmpréstimo pode ser CONCEDIDO!'
          .format(valorCasa, anosFinanc, prestacao))