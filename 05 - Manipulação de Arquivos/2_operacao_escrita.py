arquivo = open("C:/Users/pc/PycharmProjects/Projetos_DIO/05 - Manipulação de Arquivos/teste.txt", "w")
arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])
arquivo.close()