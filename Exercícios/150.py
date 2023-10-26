# Escreva um loop que faça sete chamadas para print(), então obtemos na saída o seguinte triângulo:
  #
  ##
  ###
  ####
  #####
  ######
  #######


numero = 0

exibicao = ""
while numero <= 10:
    exibicao += str(numero)
    print(exibicao)
    
    numero += 1
