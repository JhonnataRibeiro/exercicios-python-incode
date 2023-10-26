#Usando Break
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

encontrou = False

for numero in numeros:
    if numero == 5:
        encontrou = True
        break

if encontrou:
    print("O número 5 foi encontrado")
else:
    print("O número 5 não foi encontrado")


#Usando Continue
vogais = ["a", "e", "i", "o", "u"]

palavra = "python"

for letra in palavra:
    if letra not in vogais:
        continue
    
    print(letra) #Vai exibir a primeira letra vogal encontrada