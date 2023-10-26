# Tuples não pode alterar o valor
# Tuples não pode remover itens

frutas_tuple = ("maça", "banana", "cereja")
print(frutas_tuple)


comidas_tuple = tuple()
print(comidas_tuple)


numeros_tuple = tuple((1, 2, 3, 4, 5, 6, 7))
print(numeros_tuple)
print(isinstance(numeros_tuple, tuple))


#Omitindo parenteces antes de inicializar tuples
outra_tuple = 1234, 5434, "olá"
outra_tuple == ( 1234, 5434, "olá" )
print(outra_tuple)