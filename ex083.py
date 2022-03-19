'''Crie um programa onde o usuário digite uma expressão matemática qualquer que use PARÊNTESES. Seu aplicativo deverá
analisar se a expressão passada está com os parênteses abertos e fechados na ORDEM CORRETA'''

expressao = str(input('Digite uma expressão: '))
parenteses = []
for simbolos in expressao:
    if simbolos == '(':
        parenteses.append('(')
    elif simbolos == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break
if len(parenteses) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está inválida!')