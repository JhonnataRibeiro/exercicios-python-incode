# Obtenha o comprimento e a largura de um retângulo usando o prompt. Calcule sua área (área = comprimento x largura) e perímetro (perímetro = 2 x (comprimento + largura))

comprimento = int(input("Informe o comprimento do retângulo: "))
largura = int(input("Informe a largura do retângulo: "))

area = comprimento * largura
perimetro = 2 * (comprimento + largura)

print(
    f"A área do retângulo é {area}"
    f"\nO perímetro do retângulo é {perimetro}"
)