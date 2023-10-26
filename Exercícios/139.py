# Escreva um código que atribua notas aos alunos de acordo com suas pontuações:
#     90-100, A
#     70-89, B
#     60-69, C
#     50-59, D
#     0-49, F


nota = int(input("Informe a nota do aluno de 0 a 100: "))

if nota >= 0 and nota <= 100:
    if nota >= 0 and nota <= 49:
        print("Nota F")
    elif nota >= 50 and nota <= 59:
        print("Nota D")
    elif nota >= 60 and nota <= 69:
        print("Nota C")
    elif nota >= 70 and nota <= 89:
        print("Nota B")
    else:
        print("Nota A")
elif nota > 100:
    print("[ERRO] Você informou uma nota maior que 100")
else:
    print("[ERRO] Você informou uma nota menor que 0")