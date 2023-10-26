dicionario_vazio = {}
print(dicionario_vazio)


frutas_dicionario = {
    "cereja": "vermelho",
    "maça": "vermelho",
    "banana": "amarelo"
}

print(isinstance(frutas_dicionario, dict))
print(frutas_dicionario)


livros_dicionario = dict()
print(livros_dicionario)


alimento_dicionario = dict([("a1", "arroz"), ("a2", "macarrão"), ("a3", "feijão")])
print(alimento_dicionario)


# Quando as chaves são strings simples, às vezes é mais fácil especificar pares usando
dicionario = dict(idade = 12, altura = 1.90, peso = 88)

print(dicionario)