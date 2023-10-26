# Obtenha a entrada do usuário usando input(“Digite sua idade: ”). Se o usuário tiver 18 anos ou mais, dê feedback: Você tem idade suficiente para dirigir. Se for menor de 18 anos, dê feedback para aguardar a quantidade de anos que faltam. Saída:
#     Enter your age: 30
#     You are old enough to learn to drive.
#     Output:
#     Enter your age: 15
#     You need 3 more years to learn to drive.


idade = int(input("Informe sua idade: "))

if idade > 18:
    print(f"Você tem {idade} anos, e já tem idade suficiente para dirigir")
else:
    restante = 18 - idade
    print(f"Você precisa aguardar {restante} anos para poder dirigir")