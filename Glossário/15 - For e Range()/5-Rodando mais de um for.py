#Usando zip para rodar mais de uma lista ou dicionário no mesmo comando

perguntas = ["nome", "cor", "cidade"]
respostas = ["Jhonnata", "cinza", "cajapió"]

cobinacao = []

for perguntas, respostas in zip(perguntas, respostas):
    cobinacao.append(f"Qual é seu {perguntas}? É {respostas}")

print(cobinacao)