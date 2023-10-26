# Use o loop for para iterar de 0 a 100 e imprimir a soma de todos os pares e a soma de todas os impares.

lista = list(range(0, 101))

somatorio_pares = 0
somatorio_impares = 0

for numero in lista:
    if numero % 2 == 0:
        somatorio_pares += numero
    else:
        somatorio_impares += numero
    
print(f"Soma de todos os pares {somatorio_pares}")
print(f"Soma de todos os impares {somatorio_impares}")