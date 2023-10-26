# Excluir um dos itens do dicionário

aluno = {
    "primeiro_nome": "Jhonnata",
    "sobrenome": "Ribeiro",
    "gênero": "Homem",
    "idade": "12",
    "estado civil": "Solteiro",
    "habilidades": ["Python", "HTML", "CSS", "JavaScript"],
    "país": "Brasil",
    "cidade": "Cajapió",
    "endereço": "Av. Mario"
}

aluno.pop("gênero")
aluno.popitem()
del aluno["cidade"]

print(aluno)