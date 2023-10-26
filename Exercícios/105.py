# Altere a tupla about food_stuff_tp para uma lista food_stuff_lt

food_stuff_tp = ('maça', 'uva', 'banana', 'tomate', 'cebola', 'alho', 'bovino', 'ave')

food_stuff_lt = list(food_stuff_tp)
food_stuff_lt.insert(0, "pitomba")
food_stuff_lt = tuple(food_stuff_lt)

print(food_stuff_lt)