# capitalize()
texto = "Python É Uma Linguagem Muito Legal"
texto = texto.capitalize() #Retorna apenas a primeira palavras em maiúscula o resto em minúsculo
print(texto)


# casefold()
texto = "Python É Uma Linguagem Muito Legal"
texto = texto.casefold() #Vai deixar todas as palavras minúsculas
print(texto)


# center()
texto = "banana"
texto = texto.center(20) #Vai ocupar um espaço de 20 caracteres incluindo a palavra digitada, e vai centralizar no meio
print(texto)


# center()
texto = "banana"
texto = texto.center(20, "x") #Aqui vai ocupar os espaços com a letra x
print(texto)


# count()
texto = "Eu amo maçãs, maçã é minha fruta favorita"
texto = texto.count("maçã") #Vai contar quantas vezes a palavra está na string, não importa se está no singular ou no plural, vai contar assim mesmo
print(texto)


# count()
texto = "Eu amo maçãs, maçã é minha fruta favorita"
texto = texto.count("maçã", 3, 19) #Definindo onde começa e terminar a contagem
print(texto)


# encode()
texto = "O meu nome é Ståle"
texto = texto.encode() #Estudar mais
print(texto)


# endswith()
texto = "Python é uma linguagem muito legal."
texto = texto.endswith(".") #Verifica se no fim da string tem o que foi especificado, retorna um valor booleano 
print(texto)


# endswith()
texto = "Python é uma linguagem muito legal"
texto = texto.endswith("muito legal") #Verificando frase
print(texto)


# endswith()
texto = "Python é uma linguagem muito legal."
texto = texto.endswith("linguagem", 2, 5) #Vai verificar no indice inicio e fim se tem a palavra especificada
print(texto)


# expandtabs()
texto = "\tMeu nome é\t Jhonnata"
texto = texto.expandtabs(5) #Definindo o tamanho do espaço de tab na string, osb: por padrão o tamanho é 8 espaços
print(texto)


# find()
texto = "Olá, bem vinda ao meu mundo."
texto = texto.find("vinda") #Vai retornar o indice da primeira palavra escontrada
#Obs: Retorna -1 se a palavra não for encontrada.
print(texto)


# find()
texto = "Olá, bem vinda ao meu mundo."
texto = texto.find("ao", 5, 20) #Vai procurar a palavra no indice inicio e fim na string
#Obs: Retorna -1 se a palavra não for encontrada.
print(texto)


# format()
texto = "Python"
print("A linguagem que amo é {}".format(texto)) #É um dos formatadores em python para usar variável ao imprimir


# format()
texto1 = "Python"
texto2 = "Django"
texto3 = "MySQL"
print("A linguagens que estudo é {0}, {1} e {2}".format(texto1, texto2, texto3)) #Colocando indices no {} vai dizer o que vai exibir na ordem colocado no format()