# Verifique se a estação é outono, inverno, primavera ou verão. Se a entrada do usuário for: setembro, outubro ou novembro, a estação é outono. Dezembro, janeiro ou fevereiro, a estação é o inverno. Março, abril ou maio, a temporada é primavera Junho, julho ou agosto, a temporada é verão

mes = str(input("Informe o mês atual: "))

if mes in ["setembro", "outubro", "novembro"]:
    print("Estação: Outuno")
elif mes in ["dezembro", "janeiro", "fevereiro"]:
    print("Estação: Inverno")
elif mes in ["março", "abril", "maio"]:
    print("Estação: primavera")
elif mes in ["junho", "julho", "agosto"]:
    print("Estação: verão")
else:
    print("[ERRO] mês informado incorretamente, tente novamente")