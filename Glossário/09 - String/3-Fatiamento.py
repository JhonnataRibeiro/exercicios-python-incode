texto = "Python"
print(texto[0:2]) #Vai fatiar do inicio do texto até 2 (Obs: no fatiamento o 2 não é exibido, apenas o anterior)
print(texto[2:5])

print(texto[:2] + texto[2:]) #Vai exibir a string completa
print(texto[:4] + texto[4:])


print(texto[:2]) #Vai exibir do inicio até o 1 (2 não mostra)
print(texto[4:]) #Vai mostrar do indice 4 até o fim
print(texto[-2:]) #Vai mostrar as duas ultimas palavras


print(texto[4:42]) #Vai mostrar do indice 4 até o fim da string (não importa colocar um valor muito alto, python ignora e vai até onde a string existe)
print(texto[42:]) #Vai pegar uma string que não existe nesse indice vai mostrar nada

print(texto[::-1]) #Vai deixar o Python ao contrário

print(texto[0:6:2]) #Vai fatiar a string pulando de dois em dois