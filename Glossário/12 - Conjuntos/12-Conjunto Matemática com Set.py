# UNIÃO
conjunto1 = {"a", "b"}
conjunto2 = {"c", "d"}
# Pode ser usado com números

uniao = conjunto1.union(conjunto2)

print(uniao)



# INTERSEÇÃO
conjunto1 = {"a", "b", "y", "w"}
conjunto2 = {"y", "c", "w", "d"}
# Pode ser usado com números

intersecao = conjunto1.intersection(conjunto2)

print(intersecao)



# DIFERENÇA
conjunto1 = {"a", "b", "c", "d"}
conjunto2 = {"b", "d"}
# Pode ser usado com números

diferenca = conjunto1.difference(conjunto2)

print(diferenca)



# DIFERENÇA SIMÉTRICA
conjunto1 = {"a", "w", "b"}
conjunto2 = {"a", "y", "b"}
# Pode ser usado com números

diferenca_simetrica = conjunto1.symmetric_difference(conjunto2)

print(diferenca_simetrica)



# CONJUNTOS DE JUNÇÃO (VERIFICA SE NÃO TEM ITEM EM COMUM)
conjunto1 = {"a", "w", "b"}
conjunto2 = {"a", "y", "b"}
# Pode ser usado com números

print(conjunto1.isdisjoint(conjunto2))


conjunto1 = {1, 3, 5, 7}
conjunto2 = {2, 4, 6, 6}
# Pode ser usado com números

print(conjunto1.isdisjoint(conjunto2))



# VERIFICANDO SUBCONJUNTO
conjunto1 = {"a", "b", "c", "d", "e"}
conjunto2 = {"a", "b", "c"}
# Pode ser usado com números

subconjunto = conjunto2.issubset(conjunto1) #Verifica se o conjunto1 tem os mesmo itens do conjunto2

print(subconjunto)



# VERIFICANDO SUPERCONJUNTO
conjunto1 = {"a", "b", "c", "d", "e"}
conjunto2 = {"a", "b", "c", "d", "e"}
# Pode ser usado com números

subconjunto = conjunto2.issuperset(conjunto1) #Verifica se todos os elementos do conjunto1 está no conjunto2

print(subconjunto)