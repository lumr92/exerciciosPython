'''Crie uma TUPLA preenchida com os 20 PRIMEIROS colocados da tabela do CAMPEONATO BRASILEIRO DE FUTEBOL, na ordem de colocação.
Depois mostre:
A) Apenas os 5 primeiros colocados
B) Os últimos 4 colocados da tabela
C) Uma lista com os times em ORDEM ALFABÉTICA
D) Em que POSIÇÃO na tabela está o time CHAPECOENSE'''

tabela = ('Atletico-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Red Bull Bragantino', 'Fluminense', 'America-MG', 'Atletico-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo',
          'Athletico-PR', 'Cuiabá', 'Juventude', 'Gremio', 'Bahia', 'Sport', 'Chapecoense')

print(f'Lista de times do Brasileirão: {tabela}')
print('-=-' * 20)
print(f'Os cinco primeiros são {tabela[0:5]}')
print('-=-' * 20)
print(f'Os 4 últimos são {tabela[16:]}')
print('-=-' * 20)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-=-' * 20)
print(f'A Chapecoense está na {tabela.index("Chapecoense") + 1}ª posição')