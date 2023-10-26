#Sorted para organizar em ordem alfabetica
frutas_dicionario = {
    "cereja": "vermelho",
    "maça": "vermelho",
    "banana": "amarelo"
}

frutas_dicionario = sorted(frutas_dicionario)

print(frutas_dicionario)


#Método get retorna None (mas não erro) se não achar a chave solicitada
frutas_dicionario = {
    "cereja": "vermelho",
    "maça": "vermelho",
    "banana": "amarelo"
}

print(frutas_dicionario.get("abacaxi")) # Retorna None
print(frutas_dicionario.get("maça"))


#Append adicionando novo item na lista dentro do dicionário
frutas_dicionario = {
    "cereja": "vermelho",
    "maça": "vermelho",
    "banana": "amarelo",
    "laranjas": ["brasil", "frança"]
}

frutas_dicionario["abacaxi"] = "verde"
frutas_dicionario["laranjas"].append("alemanha")

print(frutas_dicionario)


#Removendo um item do dicionário
frutas_dicionario = {
    "cereja": "vermelho",
    "maça": "vermelho",
    "banana": "amarelo",
}

frutas_dicionario.pop("maça")

print(frutas_dicionario)



frutas_dicionario = {
    "cereja": "vermelho",
    "maça": "vermelho",
    "banana": "amarelo",
}

frutas_dicionario.popitem() #Remove o ultimo item do dicionário

print(frutas_dicionario)


# Limpando um dicionário
frutas_dicionario = {
    "cereja": "vermelho",
    "maça": "vermelho",
    "banana": "amarelo",
}

print(frutas_dicionario.clear()) #Retorna None


#Copiar um dicionário
frutas_dicionario = {
    "cereja": "vermelho",
    "maça": "vermelho",
    "banana": "amarelo",
}

copia_dicionario = frutas_dicionario.copy()

print(copia_dicionario)


#Obtendo as chaves do dicionário como lista
frutas_dicionario = {
    "cereja": "vermelho",
    "maça": "vermelho",
    "banana": "amarelo",
}

chaves = frutas_dicionario.keys()

print(chaves)


#Obtendo os valores do dicionário como lista
frutas_dicionario = {
    "cereja": "vermelho",
    "maça": "vermelho",
    "banana": "amarelo",
}

valores = frutas_dicionario.values()

print(valores)