# Crie um acrônimo ou abreviação para o nome 'Python para todos'.

texto = "Python para todos"

abreviacao = texto[0:1] + texto[7:8] + texto[12:13]

print(abreviacao)


formacao = ""
acronimo = texto.split(" ")
for indice in range(3):
    texto = acronimo[indice]
    formacao += texto[0:1]

print(formacao)