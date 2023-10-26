# Compare os valores de my_age e your_age usando if … else. Quem é mais velho (eu ou você)? Use input(“Enter your age: ”) para obter a idade como entrada. Você pode usar uma condição aninhada para imprimir 'ano' para 1 ano de diferença de idade, 'anos' para diferenças maiores e um texto personalizado se minha_idade = sua_idade. Saída:
#     Enter your age: 30
#     You are 5 years older than me.

minha_idade = int(input("Informe sua idade: "))
dela_idade = int(input("Informe a idade dela: "))

if minha_idade > dela_idade:
    diferenca = minha_idade - dela_idade
    print(f"Você tem {diferenca} anos de diferença dela"
)
elif minha_idade == dela_idade:
    print("Ambos tem a mesma idade")
else:
    diferenca = dela_idade - minha_idade
    print(f"Ela tem {diferenca} anos de diferença da sua")