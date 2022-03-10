'''Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
ele disser que quer mostrar 0 termos'''

print('=' * 30)
print('     10 TERMOS DE UMA PA      ')
print('=' * 30)
novoCont = 1
pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
cont = 1
termo = pt
quantTermos = 0
while cont <= 10:
    print('{} -> '.format(termo), end='')
    cont += 1
    termo += r
    quantTermos += 1
print('PAUSA')
while novoCont != 0:
    novoCont = int(input('Quantos termos você quer mostrar a mais? '))
    if novoCont == 0:
        print('Progressão finalizada com {} termos mostrados.'.format(quantTermos))
    else:
        cont = 1
        while cont <= novoCont:
            print('{} -> '.format(termo), end='')
            cont+= 1
            termo += r
            quantTermos += 1
        print('PAUSA')

