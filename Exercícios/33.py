# Escreva um script que solicite ao usuário que insira o número de anos. Calcule quantos segundos uma pessoa pode viver. Suponha que uma pessoa pode viver cem anos

idade = int(input("Informe sua idade: "))
vida = 100

restante = vida - idade
segundos = restante * 365 * 24 * 60 * 60

print(f"Você ainda vai viver por {segundos} segundos.")