# Sou professora e adoro inspirar e ensinar as pessoas. Quantas palavras únicas foram usadas na frase? Use os métodos split e set para obter as palavras únicas.

texto = "Sou professora e adoro inspirar e ensinar as pessoas"

lista = list(texto.split(" "))

conjunto = set(lista)

print(conjunto)
print(len(conjunto))