"""Aprimore o DESAFIO ANTERIOR, mostrando no final:
A) A SOMA de todos os VALORES PARES digitados.
B) A SOMA dos valores da TERCEIRA COLUNA
C) O maior valor da SEGUNDA LINHA"""

# variaveis
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # lista com a quantidade de valores que uma matriz 3x3 exige
somaPar = maiorValor = somaTColuna = 0

for linha in range(0, 3):  # estrutura de repetição para percorrer a linha da matriz
    for coluna in range(0, 3):  # estrutura de repetição para percorrer a coluna da matriz
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}], [{coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:  # estrutura condicional para fazer a soma dos numeros pares
            somaPar += matriz[linha][coluna]
print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')  # impressao dos numeros da matriz linha e coluna com formatação
                                                        # de 5 espaços e conteudo centralizado
    print() # print para pular quando for feito a repetição
print('-=' * 30)
print(f'A soma dos valores pares é {somaPar}')
for linha in range(0, 3):  # estrutura de repetição para fazer a soma dos valores da terceira coluna da matriz
    somaTColuna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {somaTColuna}')
for coluna in range(0, 3):  # estrutura de repetição para identificar qual é o maior valor da segunda linha da matriz
    if coluna == 0 or matriz[1][coluna] > maiorValor:
        maiorValor = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maiorValor}')