'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO!
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('A sua média foi de {} e você está REPROVADO!'.format(m))
elif m >= 5 and m < 7:
    print('A sua média foi de {} e você está de RECUPERAÇÃO!'.format(m))
else:
    print('A sua média foi de {} e PARABÉNS você está APROVADO!'.format(m))