palavras = ["gato", "janela", "cachorro", "tijolo"]
comprimento = 0

for indice in palavras:
    comprimento += len(indice)

print(comprimento)


#Loop Infinito
# palavras = ["gato", "janela", "cachorro", "tijolo"]

# for indice in palavras:
#     if len(indice) > 6:
#         palavras.insert(0, indice)

# print(palavras)


#Sem Loop infinito
palavras = ["gato", "janela", "cachorro", "tijolo"]

lista = []
for indice in palavras:
    lista.append(indice)
    if len(indice) > 6:
        lista.insert(0, indice)

print(lista)