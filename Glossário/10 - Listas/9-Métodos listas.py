frutas = ["laranja", "uva", "pera"]
frutas.append("melancia") #Append vai adicionar um novo item no final da lista
print(frutas)


frutas = ["laranja", "uva", "pera"]
frutas.remove("uva") #Remove vai remover o item especificado
print(frutas)


frutas = ["laranja", "uva", "pera"]
frutas.insert(1, "banana") #Insert adiciona um item na posição especificada
print(frutas)


frutas = ["laranja", "uva", "pera"]
print(frutas.index("laranja")) #Index retorna o indice do item na lista
print(frutas.index("uva")) #Index retorna o indice do item na lista
print(frutas.index("pera")) #Index retorna o indice do item na lista


frutas = ["laranja", "uva", "pera", "uva", "melancia", "pera", "uva"]
print(frutas.count("uva")) #Count vai retornar a quantidade que tem do item especificado na lista
print(frutas.count("pera")) #Count vai retornar a quantidade que tem do item especificado na lista


frutas = ["laranja", "uva", "pera"]
frutas_concorente = frutas.copy() #Copy vai fazer uma copia rasa da lista, se tiver listas dentro de listas o copy() não vai poder copiar, apenas a listas mais externa
print(frutas_concorente)


frutas = ["laranja", "uva", "pera", "abacate", "wiki"]
frutas.reverse() #Reverse vai inverter a ordem da lista de trás para frente
print(frutas)


frutas = ["laranja", "uva", "pera", "abacate", "wiki"]
frutas.sort() #Sort vai organizar os item por ordem alfabetica
print(frutas)


frutas = ["laranja", "uva", "pera", "abacate", "wiki"]
frutas.sort(reverse=True) # Deixa ao contrario a lista organizada por lista alfabetica
print(frutas)


frutas = ["laranja", "uva", "pera", "abacate", "wiki"]
frutas.pop() #Pop vai eleminar o ultimo item da lista
frutas.pop(3) #Vai remover o item do indice 3
print(frutas)


frutas = ["laranja", "uva", "pera", "abacate", "wiki"]
frutas.clear() #Clear vai limpar a lista complentamente
print(frutas)


lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2) #Extend vai extender a lista adicionando outras listas
print(lista1)


frutas = ["laranja", "uva", "pera", "abacate", "wiki"]
del frutas[0] #Vai remover o item pelo indice
print(frutas)


frutas = ["laranja", "uva", "pera", "abacate", "wiki", "banana"]
del frutas[0:3] #Removendo item da listas por fatiamento
print(frutas)

frutas = ["laranja", "uva", "pera", "abacate", "wiki", "banana"]
del frutas[:] #Vai limpar a lista completamente
print(frutas)