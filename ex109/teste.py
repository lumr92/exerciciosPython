"""Modifique as funções que foram criadas no DESAFIO 107 para que elas aceitem UM PARAMETRO a mais, informando se o
valor retornado por elas vai ser ou não formatado pela função MOEDA(), desenvolvida no DESAFIO 108"""

from ex109 import moeda
preco = float(input("Digite o preço: R$"))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}')
print(f'Diminuindo 30% temos {moeda.diminuir(preco, 30, True)}')
