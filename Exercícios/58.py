# Corte a frase 'porque porque porque' na seguinte frase: 'Você não pode terminar uma frase com porque porque porque porque é uma conjunção'

texto = "Você não pode terminar uma frase com porque porque porque porque é uma conjunção"

inicio = texto.find("porque")
fim = texto.rfind("porque")
ultimo = len(texto)
print(inicio, fim)

novo = texto[0:inicio] + texto[fim:ultimo]
print(novo)