"""Crie um programa que leia NOME, ANO DE NASCIMENTO e CARTEIRA DE TRABALHO e cadastre-os (com IDADE) em um DICIONARIO
se por acaso a CTTPS for diferente de ZERO, o dicionário receberá também o ANO DE CONTRATAÇÃO e o salário. Calcule
e eacrescente, além da IDADE, com quantos anos a a pessoa vai se APOSENTAR"""
from datetime import datetime

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = idade = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')