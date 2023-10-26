# Aqui temos um dicionário de pessoas. Sinta-se livre para modificá-lo!

aluno = {
    "primeiro_nome": "Jhonnata",
    "sobrenome": "Ribeiro",
    "gênero": "Homem",
    "idade": "12",
    "estado civil": "Solteiro",
    "habilidades": ["HTML", "CSS", "JavaScript", "React"],
    "país": "Brasil",
    "cidade": "Cajapió",
    "endereço": "Av. Mario"
}

# Se a pessoa for casada e residir na Finlândia, imprima as informações no seguinte formato:
#   Asabeneh Yetayeh vive na Finlândia. Ele é casado.

if aluno["estado civil"] == "casado":
    nome_completo = aluno["primeiro_nome"] + " " + aluno["sobrenome"]
    pais = aluno["país"]
    print(f"{nome_completo} vive no(a) {pais}. Ele é casado")
else:
    nome_completo = aluno["primeiro_nome"] + " " + aluno["sobrenome"]
    pais = aluno["país"]
    print(f"{nome_completo} é solteiro e vive no(a) {pais}")