try:
    divisao = 2 / 1
except:
    print("Algo deu errado")
else:
    print("Nada deu errado")
finally:
    print("Essa mensagem vai exibida independente se o try der erro ou não")


print("")


try:
    nome = input("Informe seu nome: ")
    idade = input("Informe sua idade: ")
    nascimento = 2023 - idade
except TypeError:
    print("[ERRO] ocorreu um erro Type")
except ValueError:
    print("[ERRO] ocorreu um erro Value")
except ZeroDivisionError:
    print("[ERRO] ocorreu um erro ZeroDivision")
else:
    print("Else será ativado se não der erro no try")
finally:
    print("Vai ser executado independente do try")