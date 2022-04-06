"""Crie um programa que leia NOME, SEXO e IDADE de VÁRIAS PESSOAS, guardando os dados de cada pessoa em um DICIONÁRIO
e todos os dicionários em uma LISTA. No final mostre:
A) Quantas pessoas foram cadastradas.
B) A MÉDIA de idade do grupo.
C) Uma lista com todas as MULHERES.
D) Uma lista com todas as pessoas com IDADE acima da MÉDIA."""
#  declarando as listas, variaveis e dicionarios
galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()  # limpando os dados do dicionario para adicionar o próximo
    pessoa['nome'] = str(input('Nome: '))
    while True:  # estrutura de repetição para validar se a resposta do usuária será de acordo com o solicitado
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())  # adicionando na lista galera os dados do dicionario pessoa
    while True:  # estrutura de repetição para validar se a resposta do usuario sera de acordo com o solicitado
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO!  >>')
