'''Crie um programa que leia VARIOS NUMEROS inteiros pelo teclado. no final da execução, mostre a MEDIA ENTRE TODOS
os valores e qual foi o MAIOR e o MENOR valor lido. o programa deve perguntar ao usuario se ele quer'''

n = somaN = maiorN = menorN = 0
somaCont = 1
cont = ''

while cont != 'N':
    n = int(input('Digite um número: '))
    somaN += n
    if somaCont == 1:
        somaN = n
        maiorN = n
        menorN = n
    else:
        if n > maiorN:
            maiorN = n
        if n < menorN:
            menorN = n
    cont = str(input('Quer continuar? [S/N] ')).upper().strip()
    if cont == 'S':
        somaCont += 1
    elif cont == 'N':
        mediaCont = somaN / somaCont
        print('Foram digitados {} numeros e a media entre eles é de {}'.format(somaCont, mediaCont))
        print('O maior valor foi de {} e o menor foi de {}'.format(maiorN, menorN))
        print(somaCont, somaN)
    else:
        print('Por favor digitew S ou N para prosseguir.')
        cont = str(input('Quer continuar? [S/N] ')).upper().strip()
        if cont == 'S':
            somaCont += 1
        elif cont == 'N':
            mediaCont = somaN / somaCont
            print('Foram digitados {} numeros e a media entre eles é de {}'.format(somaCont, mediaCont))
            print('O maior valor foi de {} e o menor foi de {}'.format(maiorN, menorN))
            print(somaCont, somaN)