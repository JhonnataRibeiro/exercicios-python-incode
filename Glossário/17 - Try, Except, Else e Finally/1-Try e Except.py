# Manipulação de exceção


try: #Vai testar um código, se gerar erro, vai executar o Except
    erro = 2 / 0
except ZeroDivisionError:
    print("Não pode dá certo a divisão")



# declarado = False

# try:
#     nao_declarado = (teste)
# except NameError:
#     print("[ERRO] não é possível chamar uma variável não declarada")



try:
    print(10 + "5")
except:
    print("[ERRO] Não se pode somar int com str")



try:
    nome = input("Informe seu nome: ")
    idade = input("Informe sua idade: ")
    nascimento = 2023 - idade
except:
    print("[ERRO] a idade está em Str, logo não pode fazer a soma")



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