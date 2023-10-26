# Use o loop for para iterar de 0 a 100 e imprimir a soma de todos os números.

lista = list(range(0, 101))

somatorio = 0

for numero in lista:
    somatorio += numero

print(f"A soma dos valores é {somatorio}")