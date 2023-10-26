#Com Break
numero = 0

while numero < 10:
    print(numero)

    numero += 1

    if numero == 5:
        break


print("")


#Com Break
numero = 0

while numero < 10:
    numero += 1

    if numero == 5:
        continue #Volta para o inicio da interação do loop sem exibir o 5 no print

    print(numero)