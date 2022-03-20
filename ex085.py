""" Crie um programa onde o usuário possa digitar SETE VALORES NUMÉRICOS e cadastre-os em uma LISTA ÚNICA que mantenha
separados os valores pares e ímpares em ordem crescente. """

# variaveis
numeros = [[], []] # lista numeros com 2 listas dentro dela a lista da posição 0 será com os numeros pares e a 1 impares
valores = 0

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor) # adicionando valor par na lista da posição 0
    else:
        numeros[1].append(valor) # adicionando valor impar na lista da posição 1
print('-=' * 30)
# colocando as duas listas pares e impares em ordem crescente
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram {numeros[0]}')
print(f'Os valores ímpares digitados foram {numeros[1]}')