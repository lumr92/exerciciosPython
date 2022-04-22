"""
Crie um pequeno SISTEMA MODULARIZADO que permita cadastrar pessoas pelo seu NOME e IDADE em um arquivo de texto simples
"""

from ex115.lib.interface import *
from time import sleep
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        #  opção de listar o conteudo da lista
        lerarquivo(arq)
    elif resposta == 2:
        #  opção de cadastrar um novo item da lista
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema...Até logo.')
        break
    else:
        print('ERRO! Digite uma opção válida!')
    sleep(2)
