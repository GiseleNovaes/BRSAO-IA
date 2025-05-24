with open("minhas_notas.txt", "w") as arquivos:
    arquivos.write("Seja Bem Vindo(a)!\n")
    arquivos.write("Como posso te ajudar hoje?\n")
    arquivos.write("Até breve!\n")

with open("minhas_notas.txt", "a") as arquivos:
    arquivos.write("Estou evoluindo a cada exercício que faço.\n")
    arquivos.write("Python está se tornando cada vez mais familiar para mim.\n")

with open("minhas_notas.txt", "r") as arquivos:
    conteudo = arquivos.read()
    print(conteudo)



