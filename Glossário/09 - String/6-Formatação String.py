# F-strintg
ano = 2023
evento = "conferência"

print(f"Resultado do {ano} {evento}")


# Str format()
votos_sim = 2423
votos_nao = 123

print("{} votos sim, {} votos não".format(votos_sim, votos_nao))


print("{0}, {1}, {2}".format("Ovo", "Banana", "Uva"))
print("{2}, {0}, {1}".format("Ovo", "Banana", "Uva")) # Trocando os valores do indice, vai exibir pela ordem na declaração das vareaveis


# Operador (estilo antigo)
nome = "Jhonnata"
idade = 12
altura = 1.90
formatacao_antiga = "Eu sou %s tenho %d anos e tenho %f de altura"%(nome, idade, altura)
print(formatacao_antiga)


# Formatador casa decimais
pi = 3.1415
print(f"{pi:.3f}")

