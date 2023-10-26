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

# Se as habilidades da pessoa tiverem apenas JavaScript e React, print('Ele é um desenvolvedor front-end'), se as habilidades da pessoa tiverem Node, Python, MongoDB, print('Ele é um desenvolvedor back-end'), se as habilidades da pessoa tiverem React, Node e MongoDB, Print('Ele é um desenvolvedor fullstack'), else print('título desconhecido') - para resultados mais precisos, mais condições podem ser aninhadas!

back_end = ["Python", "MongoDB", "Node", "Java"]
front_end = ["HTML", "CSS", "JavaScript", "React"]
full_stack = ["Python", "MongoDB", "Node", "Java", "HTML", "CSS", "JavaScript", "React"]

print(aluno["habilidades"])


if aluno["habilidades"] == back_end:
    print("Back-end")
elif aluno["habilidades"] == front_end:
    print("Front-end")
elif aluno["habilidades"] == full_stack:
    print("Full-Stack")