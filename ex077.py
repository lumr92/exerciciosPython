'''Crie um programa que tenha uma TUPLA com VARIAS PALAVRAS (não usar acentos). Depois disso, você deve mostrar, para cada
palavra, quais são as suas VOGAIS'''

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
            'MERCADO', 'PROGRAMADOR', 'FUTURO')

for palavra in palavras:
    print(f'\nNa palavra {palavra} temos ', end=' ')
    for letra in palavra:
        if letra in 'AEIOU':
            print(letra, end=' ')