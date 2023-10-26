palavra = "Olá, Mundo!"

print(palavra) #Vai exibir normalmente a palavra

print(palavra.strip()) #Vai remover os espaços em branco no inicio e fim
palavra_strip = " Olá, Mundo! "
print(palavra_strip)
print(palavra_strip.strip())

print(len(palavra)) #Vai exibir a quantidade de caracteres tem na palavra ou frase

print(palavra.lower()) #Vai deixar todas as letras em minusculas

print(palavra.upper()) #Vai deixar todas as letras em maiusculas

print(palavra.replace("l", "X")) #Vai substituir a letra pela outra (Obs: todas as letras da frase vai ser alterado)

print(palavra.split(",")) #Vai dividir as palavras em substrings (Obs: pode especificar onde vai ser dividio, por ponto, virgula, espaço e etc)

print(palavra.capitalize()) #A primeira palavra vai começa com letra maisculas

print(palavra.count('M')) #Vai retornar a quantidade de letra ou palavra numa palavra ou frase

print(palavra.count("o", 2, 8)) #No count(subtring, start=, end=) vai especificar onde começa a contagem e onde termina

print(palavra.find("Mundo")) #Vai retornar a posição onde foi encontrada a palavra ou letra, se não encontrar nada vai retornar -1

print(palavra.title()) #Vai deicar cada palavra com a primeira letra maiuscula

print(palavra.replace("Mundo", "Terra")) #Vai trocar a palavra informada pela existente

minha_tuple = ('Jhonna', 'Rodrigues', 'Ribeiro')
print(','.join(minha_tuple)) #Para unir palavra em tuple em unica string

teste = "ABC"
print(teste.isupper()) #Retornar um valor boleano se todas as letras é maiusculas
print(not(teste.isupper())) #Mudando o valor boleano

teste1 = "Casa1"
teste2 = "Casas"
print(teste1.isalpha()) #Verifica se todas as letra é apenas letras
print(teste2.isalpha()) #Verifica se todas as letra é apenas letras

numero1 = "1234"
numero2 = "1234ss"
print(numero1.isdecimal()) #Verifica se é tudo numero decimal
print(numero2.isdecimal()) #Verifica se é tudo numero decimal


texto = "Python"
print(texto.endswith("on")) #Verifica se o fim da string tem o especificado e retorna um valor bool
print(texto.endswith("tion"))


texto2 = "Python é legal"
print(texto2.expandtabs()) #Vai dá tab a cada espaços na string com tabulação de 8 espaços
print(texto2.expandtabs(4)) #Especificando o tamanho do tab


texto3 = "Python"
texto4 = "Python3"
texto5 = "Python3 Mass"
print(texto3.isalnum()) #Verifica se o texto não tem espaço, é apenas uma palavra limpa
print(texto4.isalnum()) #Não importa o numero
print(texto5.isalnum()) 


#Existe mais isFunção, estudar mais