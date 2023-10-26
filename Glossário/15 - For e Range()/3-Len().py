lista_palavras = ["Jhonnata", "gosta", "de", "uma", "pessoa", "no", "Incode"]
string_concateanada = ""

for indice_palavra in range(len(lista_palavras)):
    string_concateanada += lista_palavras[indice_palavra] + " "

print(string_concateanada)


#Outra alternativa com enumerate
lista_palavras = ["Jhonnata", "gosta", "de", "uma", "pessoa", "no", "Incode"]
string_concateanada = ""

for indice_palavra, palavra in enumerate(lista_palavras):
    string_concateanada += palavra + " "

print(string_concateanada)