#Propriedade range(inicio, fim, passos)

intervalo = list(range(0, 10)) #De 0 a 10
print(intervalo)


intervalo = list(range(0, 10, 2)) #Pulando de 2 em 2
print(intervalo)


lista = list(range(5))
tupla = tuple(range(5))
conjunto = set(range(5))
# dicionario = dict(range(5)) #Não funciona em dicionário


print(lista)
print(tupla)
print(conjunto)
# print(dicionario)



pessoa = {
    'nome': 'Asabeneh',
    'sobrenome': 'Yetayeh',
    'idade': 250,
    'pais': 'Finland',
    'estado civil': True,
    'habilidade': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'endereco': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for chave in pessoa:
    if chave == "habilidade":
        for habilidade in pessoa['habilidade']:
            print(habilidade)