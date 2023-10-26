numero1 = float(input("Informe o primeiro numero: "))
numero2 = float(input("Informe o segundo numero: "))

soma = (numero1 + numero2) / 2

print(type(numero1))
print(type(numero2))
print(type(soma))
print(f"A soma de {numero1} + {numero2} = {soma}")

if soma % 2 == 0:
    print("O numero é par")
else:
    print("O numero é impar")

try:
    soma = 0 + 0
except:
    print("[ERROR] seleko fi 0 + 0???")
else:
    print("Não houve erro")
finally:
    print("tudo certo meu parceiro")

try:
    numero = int(5)
    numero = float(5.4)
except Exception as erro:
    print(erro)
