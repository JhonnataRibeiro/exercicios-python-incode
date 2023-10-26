# Sistema simples

import os
import time

#----------------------------- DADOS RAIZ
login_admin = "admin"
senha_admin = "admin"

usuarios = [
        [0, "sara", "sa234"],
        [1, "ester", "est23er34"],
        [2, "carina", "caca123"],
        [3, "giovana", "gi34gi12"],
        [4, "fernanda", "234ksdf"],
        [5, "helenna", "nna12nan"]
    ]

id_contador = 6

#--------------------------------- INICIO PROGRAMA
while True:
    os.system('clear')
    print("|---------- MENU ----------|")
    print(" [1] Fazer cadastro.")
    print(" [2] Fazer login.")
    print(" [3] Lista de usuários.")
    print(" [4] Acesso Administrador.")
    print(" [0] Encerrar programa.")
    print("")
    print("Escolha uma opção...")
    opcao = str(input("Opção: "))

    #--------------------------------------------------------- COMANDO 1
    if opcao == "1":
        #---------------------------- LOGIN
        os.system('clear')
        print("|---------- NOVO CADASTRO ----------|")
        login = str(input("Informe o login: "))

        login_while = False
        for indice in range(len(usuarios)):
            if login in usuarios[indice][1]:
                login_while = True
        
        while login_while:
            os.system('clear')
            print("[ERROR] Usuário já em uso.")
            time.sleep(3)

            os.system('clear')
            print("|---------- NOVO CADASTRO ----------|")
            login = str(input("Informe o login: "))

            fim_login_while = False
            for indice in range(len(usuarios)):
                if login in usuarios[indice][1]:
                    fim_login_while = True

            if not(fim_login_while):
                break
        #---------------------------- SENHA
        os.system('clear')
        print("|---------- NOVO CADASTRO ----------|")
        senha = str(input("Informe a Senha: "))

        novo_cadastro = [[id_contador, login, senha]]
        usuarios.extend(novo_cadastro)

        id_contador += 1

        os.system('clear')
        print("[SUCCESS] cadastro realizado com sucesso.")
        time.sleep(3)
        while True:
            os.system('clear')
            print("|---------- CADASTRADO! ----------|")
            print(f"Novo Cadastro: Login ( {login} ), Senha ( {senha} ) ")
            print("")
            print("Digite [1] para voltar ao menu.")
            opcao = str(input("Opção: "))

            if opcao == "1":
                break
    
    #--------------------------------------------------------- COMANDO 2
    if opcao == "2":
        os.system('clear')
        print("|---------- LOGIN ----------|")
        login = str(input("Informe o login: "))
        senha = str(input("Informe a senha: "))

        #Diacho de lógica enferruda siow, revisar cartilha abc primario jardim
        login_while = False
        for indice in range(len(usuarios)):
            if login in usuarios[indice][1]:
                login_while = True

        senha_while = False
        for indice in range(len(usuarios)):
            if senha in usuarios[indice][2]:
                senha_while = True

        while not(login_while and senha_while):
            os.system('clear')
            print("[ERROR] login ou senha incorreta.")
            time.sleep(3)
            os.system('clear')
            print("|---------- LOGIN ----------|")
            login = str(input("Informe o login: "))
            senha = str(input("Informe a senha: "))

            login_while = False
            for indice in range(len(usuarios)):
                if login in usuarios[indice][1]:
                    login_while = True

            senha_while = False
            for indice in range(len(usuarios)):
                if senha in usuarios[indice][2]:
                    senha_while = True

            if login_while and senha_while:
                break
        
        #Hora vaga estruturar logado
        os.system('clear')
        print("[SUCCESS] login efetuado com sucesso.")
        time.sleep(3)
        while True:
            os.system('clear')
            print("|---------- LOGADO! ----------|")
            print(f"  Olá, {login}!")
            print("")
            print(" [1] Mensagens")
            print(" [2] Novidades")
            print(" [3] Galerias")
            print(" [4] Amigos")
            print(" [5] Solicitações")
            print(" [6] Configurações")
            print(" [0] Voltar para o menu.")
            print("")
            print("Escolha uma opção...")
            opcao = str(input("Opção: "))

            if opcao == "0":
                break
    
    #--------------------------------------------------------- COMANDO 3
    if opcao == "3":
        while True:
            os.system('clear')
            print("|---------- USUÁRIOS CADASTRADO ----------|")
            for indice in range(len(usuarios)):
                print(usuarios[indice])

            print("")
            print("Digite [1] para voltar ao menu.")
            opcao = str(input("Opção: "))

            if opcao == "1":
                break
    
    #--------------------------------------------------------- COMANDO 4
    if opcao == "4":
        os.system('clear')
        print("|---------- SOLICITAÇÃO ----------|")
        login = str(input("Informe o login administrador: "))
        senha = str(input("Informe a senha administrador: "))

        login_while = False
        if not((login == login_admin) and (senha == senha_admin)):
            login_while = True

        while login_while:
            os.system('clear')
            print("[ERROR] login ou senha incorreta.")
            time.sleep(3)
            os.system('clear')
            print("|---------- SOLICITAÇÃO ----------|")
            login = str(input("Informe o login administrador: "))
            senha = str(input("Informe a senha administrador: "))

            acesso_admin = False
            if (login == login_admin) and (senha == senha_admin):
                acesso_admin = True

            if acesso_admin:
                break
        
        #Hora vaga estruturar administrador
        os.system('clear')
        print("[SUCCESS] login efetuado com sucesso.")
        time.sleep(3)
        while True:
            os.system('clear')
            print("|---------- ADMINISTRADOR! ----------|")
            print(" [1] Análise")
            print(" [2] Pesquisa")
            print(" [3] Server ON")
            print(" [4] Server OFF")
            print(" [5] Excluir Cadastro")
            print(" [6] Alterar Chave de Acesso")
            print(" [0] Voltar para o menu.")

            print("")
            print("Escolha uma opção...")
            opcao = str(input("Opção: "))

            if opcao == "0":
                break
    
    #--------------------------------------------------------- COMANDO 0
    if opcao == "0":
        os.system('clear')
        print("[BYE] espero ter sido útil para você T_T.")
        time.sleep(3)
        break
        

print("")
print("Programa encerrado. :(")

            