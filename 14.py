# nota1 = int(input("Informe a primeira nota: "))
# nota2 = int(input("Informe a segunda nota: "))
# nota3 = int(input("Informe a terceira nota: "))
# nota4 = int(input("Informe a quarta nota: "))

# media_1sem = (nota1 + nota2) / 2
# media_2sem = (nota3 + nota4) / 2
# media_final = (nota1 + nota2 + nota3 + nota4) / 4

# print(
#     f"A média do 1 semestre {media_1sem}"
#     f"\nA média do 2 sementre {media_2sem}"
#     f"\nA média final é {media_final}"
# )


nota1 = 0
nota2 = 0
nota3 = 0
nota4 = 0
while True:
    while True:
        nota1 = float(input("Informe a primeira nota: "))
        if nota1 >= 0 and nota1 <= 10:
            break
        else:
            continue

    while True:
        nota2 = float(input("Informe a segunda nota: "))
        if nota2 >= 0 and nota2 <= 10:
            break
        else:
            continue

    while True:
        nota3 = float(input("Informe a terceira nota: "))
        if nota3 >= 0 and nota3 <= 10:
            break
        else:
            continue
    
    fim_while = False
    while True:
        nota4 = float(input("Informe a quarta nota: "))
        if nota4 >= 0 and nota4 <= 10:
            fim_while = True
            break
        else:
            continue
    
    media1 = (nota1 + nota2) / 2
    media2 = (nota3 + nota4) / 4
    final = (nota1 + nota2 + nota3 + nota4) / 4
    if fim_while:
        break

print(
    f"Media da 1 semestre{media1}"
    f"\nMediaa do 2 sementre\n{media2}"
    f"\nMedia final {final}"
)
