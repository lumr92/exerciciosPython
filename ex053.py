'''Crie um programa que leia uma FRASE qualquer e diga se ela é um PALÍNDROMO, desconsiderando os espaços
Ex: Após a sopa / a salada da casa / a torre da derrota'''

'''frase = input('Digite uma frase: ').upper()
frase = frase.replace(" ", "")
esarf = "".join(reversed(frase))
print('O inverso de {} é {}'.format(frase, esarf))
if str(frase) == ''.join(esarf):
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')'''

'''METODO CURSO EM VIDEO'''
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

print('O inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')