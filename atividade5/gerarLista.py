import random

def gerarLista(quantidade, nome_arquivo="numeros.txt"):
    with open(nome_arquivo, "w") as arquivo:
        numeros = [str(random.randint(0, 10000)) for _ in range(quantidade)]
        arquivo.write("\n".join(numeros))