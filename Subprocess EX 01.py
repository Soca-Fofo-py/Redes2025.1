import subprocess
saida_simples = subprocess.run(["ipconfig"],capture_output=True,text=True).stdout
saida_completa = subprocess.run(["ipconfig","/all"],capture_output=True,text=True).stdout

saida = subprocess.run(["ipconfig"],capture_output=True,text=True).stdout
print(saida)

linhas = saida.split("\n")
print(linhas)

for linha in linhas:
    if "IPv4" in linha:
        print(linha)

