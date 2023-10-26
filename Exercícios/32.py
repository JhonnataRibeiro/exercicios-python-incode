# Escreva um script que solicite ao usuário que insira as horas e a taxa por hora. Calcular salário da pessoa?

horas = int(input("Informe as horas trabalhadas: "))
valor_por_hora = float(input("Informe quanto ganha por hora: "))

salario = horas * valor_por_hora

print(f"O sálario da pessoa é R$ {salario:.0f} reais.")