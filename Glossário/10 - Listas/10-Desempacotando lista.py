lista = ["item1", "item2", "item3", "item4"]
primeiro_item, segundo_item, terceiro_item, quarto_item = lista

print(primeiro_item)
print(segundo_item)
print(terceiro_item)
print(quarto_item)



paises = ["Brasil", "França", "Alemanha", "Italia", "Reino Unido", "Russia"]
br, fr, gr, *resto = paises

print(br, fr, gr)
print(resto)