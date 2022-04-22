"""Dentro do pacote UTILIDADECEV que criamos no DESAFIO 111 temos um MODULO chamado dado. Crie uma função chamada
LEIADINHEIRO() que seja capaz de funcionar como a função INPUT(), mas com uma VALIDAÇÃO DE DADOS para ceitar apenas
valores que sejam MONETÁRIOS"""
from ex112.utilidadescev import moeda
from ex112.utilidadescev import dado

preco = dado.leiadinheiro("Digite o preço: R$")
moeda.resumo(preco, 35, 22)
