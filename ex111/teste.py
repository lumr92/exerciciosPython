"""Crie um PACOTE chamado UTILIDADESCEV() que tenha dois MÓDULOS INTERNOS chamados MOEDA E DADO.
Transfira todas as funções utilizadas nos DESAFIOS 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando."""
from ex111.utilidadesCeV import moeda

preco = float(input("Digite o preço: R$"))
moeda.resumo(preco, 35, 22)