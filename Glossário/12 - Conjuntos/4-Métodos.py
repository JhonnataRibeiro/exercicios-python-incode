#Add para adicionar no conjunto
conjunto_frutas = {"maçã", "banana", "cereja"}

conjunto_frutas.add("pera")
conjunto_frutas.add("kiwi")

print(conjunto_frutas)


#Remove
conjunto_frutas = {"maçã", "banana", "cereja"}

conjunto_frutas.remove("maçã")

print(conjunto_frutas)


#Adicionando varios elementos com Update
conjunto_frutas = {"maçã", "banana", "cereja"}

conjunto_frutas.update(["uva", "pitomba", "laranja"])

print(conjunto_frutas)


conjunto_frutas = {"maçã", "banana", "cereja"}
adicionar_conjunto = ["uva", "pitomba", "laranja"]

conjunto_frutas.update(adicionar_conjunto)

print(conjunto_frutas)


#Removendo um item do conjunto (Caso não for encontrado não gera erro)
conjunto_frutas = {"maçã", "banana", "cereja"}
conjunto_frutas.discard("maçã")
conjunto_frutas.discard("pera") #Aqui não mostrar o erro por não ter encontrado

print(conjunto_frutas)


# Pop() para remover um item aleatorio do conjunto
conjunto_frutas = {"maçã", "banana", "cereja"}
conjunto_frutas.pop()

print(conjunto_frutas)



conjunto_frutas = {"maçã", "banana", "cereja"}
item_removido = conjunto_frutas.pop()

print(item_removido)


#Limpando o conjunto
conjunto_frutas = {"maçã", "banana", "cereja"}
conjunto_frutas.clear()

print(conjunto_frutas)


#
