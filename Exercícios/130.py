# Modifique os valores das habilidades adicionando uma ou duas habilidades

aluno = {
    "primeiro_nome": "",
    "sobrenome": "",
    "gênero": "",
    "idade": "",
    "estado civil": "",
    "habilidades": ["Python", "HTML", "CSS", "JavaScript"],
    "país": "",
    "cidade": "",
    "endereço": ""
}

aluno["habilidades"].append("Flask")
aluno["habilidades"].append("Django")

print(aluno)