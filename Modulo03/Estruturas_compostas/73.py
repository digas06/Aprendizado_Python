'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
 na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.'''
times = ("Flamengo", "Santos", "Palmeiras", "Gremio",
         "Atletico Paranaense", "São Paulo", "Internacional",
         "Conrithians", "Fortaleza", "Goias", "Bahia", "Vasco",
         "Atletico Mineiro", "Fluminense", "Botafogo", "Ceará",
         "Cruzeiro", "CSA", "Chapecoense", "Avaí")
print(f'Todos os times: {times}\n{"-=-"*20}')
print(f'5 primeiros: {times[0:5]}\n{"-=-"*20}')
print(f'Últimos 4: {times[-4:]}\n{"-=-"*20}')
print(f'Times em ordem alfabética: {sorted(times)}\n{"-=-"*20}')
print(f'Posição do Chapecoense: {times.index("Chapecoense")+1}')

