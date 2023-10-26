# Juntar A com B e B com A

conjunto_a = {19, 22, 24, 20, 25, 26}
conjunto_b = {19, 22, 20, 25, 26, 24, 28, 27}

acomb = conjunto_a.union(conjunto_b)
bcoma = conjunto_b.union(conjunto_a)

print(acomb)
print(bcoma)