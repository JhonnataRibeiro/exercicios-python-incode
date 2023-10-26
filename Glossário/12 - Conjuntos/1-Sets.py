conjunto_frutas = {"maçã", "banana", "cereja"}

print(conjunto_frutas)
print(isinstance(conjunto_frutas, set))


conjunto_livros = set()
print(conjunto_livros)
print(type(conjunto_livros))


lista = [1, 5, 2, 7, 2, 7, 4, 9, 5]
conjunto = set(lista) #Transformando lista para conjunto, os numeros iguais vai se aplicado somente um, vai eleminar item duplicado e deixar só um
print(conjunto)