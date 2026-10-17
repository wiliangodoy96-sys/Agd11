# Programa para representação de nível de água com cores de indicação.
# Autor: Wilian Godoy Francisco
from colorama import Fore, Style
# Entrada de dados referentes ao nível de água do reservatório de água.
nivel = int(input("informar o nível de água do reservatório (1 a 5): "))

print (Fore. WHITE + "---NÍVEL DO RESERVATÓRIO DE ÁGUA---")

if nivel ==1:
    print (Fore. RED + "Muito baixo (crítico)")
elif nivel == 2:
    print(Fore. YELLOW + "Baixo")
elif nivel == 3:
    print(Fore. GREEN  + "Médio")
elif nivel == 4:
    print(Fore. CYAN  + "Alto")
elif nivel ==5:
    print(Fore. BLUE + "Muito Alto (Alerta)")
else:
    print("Nível inválido! Informe um valor de 1 a 5.")

Style.RESET_ALL