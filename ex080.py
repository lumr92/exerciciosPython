'''Crie um programa onde o usuário possa digitar cinco VALORES NUMÉRICOS e cadastre-os em uma LISTA, JÁ NA POSIÇÃO CORRETA
 de inserção (sem usar o sort).
 No final, mostre a LISTA ORDENADA na tela'''

valores = []

for cont in range(0, 5):
    n = int(input('Digite um valor: '))
    if cont == 0 or n > valores[-1]:
        valores.append(n)
        print('Adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(valores):
            if n <= valores[posicao]:
                valores.insert(posicao, n)
                print(f'Adicionado na posição {posicao} da lista')
                break
            posicao += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')