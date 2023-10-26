# Escreva um script que solicite ao usuário que insira o lado a, o lado b e o lado c do triângulo. Calcule o perímetro do triângulo (perímetro = a + b + c).

lado_a = int(input("Informe o lado A do triângulo: "))
lado_b = int(input("Informe o lado B do triângulo: "))
lado_c = int(input("Informe o lado C do triângulo: "))

perimetro = lado_a + lado_b + lado_c

print(f"O perímetro do triângulo é {perimetro}")