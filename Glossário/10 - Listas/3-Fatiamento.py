lista = [1, 4, 0, 8, 3, 23]

metade = lista[0:3]
print(metade)


lista = [2, 5, 2, 7, 4, 9, 1, 6]
metade_ultimos = lista[3:8]
print(metade_ultimos)


letras = ["a", "b", "c", "d"]
fatia = letras[1:3]
print(fatia)


#Fatimanento por etapa
letras = ["a", "b", "c", "d", "e", "f", "g", "h"]
fatia = letras[::2] #Vai fatiar os itens de dois em dois
print(fatia)


#Limpando lista com fatiamento
lista = ["a", "b", "c", "d"]
lista[:] = []
print(lista)