# ['China', 'Rússia', 'EUA', 'Finlândia', 'Suécia', 'Noruega', 'Dinamarca']. Descompacte os três primeiros países e o restante como países escandinavos.

paises = ['China', 'Rússia', 'EUA', 'Finlândia', 'Suécia', 'Noruega', 'Dinamarca']

china, russia, eua, *outros = paises

print(china)
print(russia)
print(eua)
print(outros)