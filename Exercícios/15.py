# Use a função de entrada integrada para obter o nome, sobrenome, país e idade de um usuário e armazenar o valor em seus nomes de variáveis ​​correspondentes

nome = input("Informe seu nome: ")
sobrenome = input("Informe seu sobrenome: ")
pais = input("Informe seu páis: ")
idade = int(input("Informe sua idade: "))
print(
    "\n"
    f"Seu nome é {nome}"
    f"\nSeu sobrenome é {sobrenome}"
    f"\nSeu país é {pais}"
    f"\nSua idade é {idade}"
)