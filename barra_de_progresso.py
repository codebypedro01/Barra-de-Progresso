"""
BARRA DE PROGRESSO
"""
import time

total = 50

print("Aguarde o carregamento!")

for i in range(total + 1):
    porcentagem = int((i / total) * 100)
    barra = "#" * (porcentagem // 5)
    espacos = " " * ((100 - porcentagem) // 5)
    print(f"\rProgresso: [{barra}{espacos}] {porcentagem}%", end="")
    time.sleep(0.1)