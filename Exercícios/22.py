# Obtenha o raio de um círculo usando o prompt. Calcule a área (área = pi x R x R) e a circunferência (c = 2 x pi x R) onde pi = 3,14.

raio = float(input("Informe o raio do círculo: "))
pi = float(3.1415)

area = pi * (raio * 2)
circunferencia = 2 * pi * raio

print(
    f"A área do círculo é {area:.2f}"
    f"\nA circuferência do circulo é {circunferencia:.2f}"
)

