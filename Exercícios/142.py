# Aqui temos um dicionário de pessoas. Sinta-se livre para modificá-lo!

aluno = {
    "primeiro_nome": "Jhonnata",
    "sobrenome": "Ribeiro",
    "gênero": "Homem",
    "idade": "12",
    "estado civil": "Solteiro",
    "habilidades": ["HTML", "CSS", "JavaScript"],
    "país": "Brasil",
    "cidade": "Cajapió",
    "endereço": "Av. Mario"
}

# Verifique se o dicionário de pessoas tem chave de habilidades, se assim for, imprima a habilidade do meio na lista de habilidades.

if "habilidades" in aluno:
    print(aluno["habilidades"][1])
else:
    pass