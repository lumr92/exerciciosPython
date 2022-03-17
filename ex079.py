'''Crie um programa onde o usuário possa digitar vários VALORES NUMÉRICOS e cadastre-os em uma LISTA. Caso o número
já exista lá dentro, ele NÃO SERÁ ADICIONADO.
No final, serão exibidos todos os VALORES ÚNICOS digitados, em ORDEM CRESCENTE'''

valores = []
cont = ''


while True:
    #valores.append(int(input('Digite um valor: ')))
    #for i, v in enumerate(valores):
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while cont not in 'NS':
        cont = str(input('Digite [S/N]: ')).strip().upper()[0]
    if cont in 'N':
            break
print('-=' * 20)
valores.sort()
print(f'Você digitou os valores {valores}')