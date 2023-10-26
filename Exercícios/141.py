# A lista a seguir contém algumas frutas:

# fruits = ['banana', 'orange', 'mango', 'lemon']

# Se uma fruta não existir na lista, adicione a fruta à lista e imprima a lista modificada. Se a fruta existir print('Essa fruta já existe na lista')


frutas = ["banana", "laranja", "morango", "manga", "uva"]

nova_fruta = str(input("Adicione uma nova fruta: "))

if nova_fruta in frutas:
    print("Essa fruta já esxite na lista")
else:
    nova_frutas = frutas
    nova_frutas.append(nova_fruta)
    print(nova_frutas)