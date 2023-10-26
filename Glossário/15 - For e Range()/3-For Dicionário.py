pessoa = {
    "nome": "Jhonnata",
    "habilidade": "Python",
    "poder": "Fogo"
}

nome_chave = []
tipo_valor = []

for chave, valor in pessoa.items():
    nome_chave.append(chave)
    tipo_valor.append(valor)


print(nome_chave)
print(tipo_valor)