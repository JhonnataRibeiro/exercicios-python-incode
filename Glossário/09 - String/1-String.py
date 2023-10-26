nome1 = "João"
nome2 = "João"

print(nome1 == nome2)
print(isinstance(nome1, str))
print(isinstance(nome2, str))


aspas_simples = 'Jhonnata'
aspas_duplas = "Jhonnata"
aspas_triplas_simples = '''Jhonnata'''
aspas_triplas_duplas = """Jhonnata"""

print(f"{aspas_simples}")
print("{}".format(aspas_duplas))
print("", aspas_triplas_simples)
print(aspas_triplas_duplas)

print("")
#Desempacotando Personagens
linguagem = "Python"
a, b, c, d, e, f = linguagem
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)