"""Faça um programa que leia NOME E MÉDIA de um aluno, guardando também a SITUAÇÃO em um DICIONÁRIO.
No final, mostre o conteúdo da estrutura na tela."""

aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'{k} = {v}')