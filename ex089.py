"""Crie um programa que leia NOME e DUAS NOTAS de vários alunos e guarde tudo em uma LISTA COMPOSTA.
No final, mostre um BOLETIM contendo a média de cada um e permita que o usuário possa mostrar as NOTAS de cada aluno
individualmente"""

dadosAlunos = []

while True:  # estrutura de repetição para inserir dados na lista dadosAlunos
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    dadosAlunos.append([nome, [nota1, nota2], media])  # inseridos os dados das variaveis, sendo que as notas é
                                                        # inserido em uma lista dentro da lista dadosAlunos
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'nN':
        break

print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for indice, aluno in enumerate(dadosAlunos):  # estrutura de repetição para mostrar os dados inseridos dos alunos
                                                # formatados
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:  # estrutura de repetição para criar um menu para mostrar as notas de cada aluno
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:  # estrutura condicional para dar a opção do usuario sair do menu
        print('FINALIZANDO...')
        break
    if opc <= len(dadosAlunos) - 1:  # estrutura condicional para o usuario selecionar o aluno que quer ver as notas
        print(f'Notas de {dadosAlunos[opc][0]} são {dadosAlunos[opc][1]}')
print('VOLTE SEMPRE!')