# Modifique a tupla de irmãos e adicione o nome de seu pai e sua mãe e atribua-o a family_members

irmoes = ('Jhonnata', 'Daniel', 'Natanael', 'Guilerme', 'Jhannyele', 'Ellem', 'Eduarda')

family_members = list(irmoes)
family_members.insert(0, "Jorgival")
family_members.insert(5, "Lucilene")

tuple_novamente = tuple(family_members)

print(tuple_novamente)