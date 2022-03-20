"""Crie um programa que crie uma MATRIZ de DIMENSÃO 3X3 e preencha com valores lidos pelo teclado.
No final mostre a MATRIZ na tela, com a formatação correta."""

#variaveis
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # lista com a quantidade de valores que uma matriz 3x3 exige
for linha in range(0, 3): # estrutura de repetição para percorrer a linha da matriz
    for coluna in range(0, 3): # estrutura de repetição para percorrer a coluna da matriz
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}], [{coluna}]: '))
print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='') # impressao dos numeros da matriz linha e coluna com formatação
                                                        # de 5 espaços e conteudo centralizado
    print() # print para pular quando for feito a repetição
