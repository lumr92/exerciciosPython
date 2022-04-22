"""Crie um módulo chamado MOEDA.PY que tenha as funções incorporadas AUMENTAR(), DIMINUIR(), DOBRO() e METADE().
Faça tambem um programa que IMPORTE esse módulo e use algumas dessas funções."""

import moeda

preco = float(input("Digite o preço: R$"))
print(f'A metade de R${preco} é R${moeda.metade(preco)}')
print(f'O dobro de R${preco} é R${moeda.dobro(preco)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(preco, 10)}')
print(f'Diminuindo 30% temos R${moeda.diminuir(preco, 30)}')
