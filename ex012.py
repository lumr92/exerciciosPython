valor = float(input('Qual é o preço do produto? '))
desconto = valor * (5/100)
print('O valor que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(valor, valor - desconto))