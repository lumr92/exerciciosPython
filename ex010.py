#Conversor de moedas

real = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Com R${} você ṕode comprar US${:.2f} e E${:.2f}'.format(real, real / 5.33, real / 6.10))
