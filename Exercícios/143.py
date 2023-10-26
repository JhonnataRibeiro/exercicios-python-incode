# Aqui temos um dicionário de pessoas. Sinta-se livre para modificá-lo!

aluno = {
    "primeiro_nome": "Jhonnata",
    "sobrenome": "Ribeiro",
    "gênero": "Homem",
    "idade": "12",
    "estado civil": "Solteiro",
    "habilidades": ["HTML", "CSS", "JavaScript", "Python"],
    "país": "Brasil",
    "cidade": "Cajapió",
    "endereço": "Av. Mario"
}

# Verifique se o dicionário da pessoa possui chave de habilidades, se sim, verifique se a pessoa possui a habilidade 'Python' e imprima o resultado.

if "habilidades" in aluno:
    if "Python" in aluno["habilidades"]:
        print("Tem a habilidade Python")
    else:
        print("Não tem a habilidade Python")
else:
    print("Não tem essa chave")