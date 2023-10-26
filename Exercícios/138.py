# Obtenha dois números do usuário usando o prompt de entrada. Se a é maior que b, retorna a é maior que b, se a é menor que b, retorna a é menor que b, senão a é igual a b. Saída:
#     Enter number one: 4
#     Enter number two: 3
#     4 is greater than 3


valor_a = int(input("Informe o valor do A: "))
valor_b = int(input("Informe o valor do B: "))

if valor_a > valor_b:
    print("A maior que B")
elif valor_a == valor_b:
    print("A e B tem ambos valores")
else:
    print("B maior que A")