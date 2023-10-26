try:
    nome = input("Informe seu nome: ")
    idade = input("Informe sua idade: ")
    nascimento = 2023 - idade
    print(f"Você nasceu no ano {nascimento}")
except Exception as e: #Aqui vai expecificar o motivo do erro
    print(e)


print("")


try:
    divisao = 2 / 0
    print(divisao)
except Exception as erro:
    print(erro)