import time
import os
from memory_profiler import memory_usage
from bubbleSort import *;
from mergeSort import *;
import os
import pandas as pd


def ler(arquivo):
    lista = []
    with open(arquivo, "r") as f:
        for linha in f:
            lista.append(int(linha))
    print("Arquivo lido com sucesso!")
    return lista

def salvar_lista_em_arquivo(lista, nome_arquivo):
    
    if os.path.exists(nome_arquivo):
        base, ext = os.path.splitext(nome_arquivo)
        counter = 1
        while os.path.exists(f"{base}_{counter}{ext}"):
            counter += 1
        nome_arquivo = f"{base}_{counter}{ext}"
    with open(nome_arquivo, "w") as f:
        for numero in lista:
            f.write(f"{numero}\n")
    print(f"Lista ordenada salva em '{nome_arquivo}'")



def salvar_dados_em_planilha(tempo, memoria, metodo, arquivo_saida):
    # Dados a serem salvos
    versao_python = "3.11.1"

    # Cria o DataFrame com os dados
    novo_dado = {
        "Metodo": [metodo],
        "Tempo de Execucao (ms)": [tempo],
        "Consumo de Memoria (KB)": [memoria],
        "Versao Python": [versao_python]
    }

    df_novo = pd.DataFrame(novo_dado)

    # Se o arquivo já existir, lê os dados e adiciona a nova linha
    if os.path.exists(arquivo_saida):
        df_existente = pd.read_csv(arquivo_saida)
        df_final = pd.concat([df_existente, df_novo], ignore_index=True)
    else:
        df_final = df_novo

    # Salva os dados no arquivo CSV
    df_final.to_csv(arquivo_saida, index=False)
    print(f"Dados salvos no arquivo CSV '{arquivo_saida}'")


def medirDesempenho(arquivo):
    lista = ler(arquivo)


    inicio = time.time()
    print("Ordenando lista...")
    # metodo = "bubbleSortPy"
    # memory = memory_usage((bubbleSort, (lista,)))
    metodo = "mergeSortPy"
    memory = memory_usage((mergeSort, (lista,)))
    memoria = max(memory) * 1024
    fim = time.time()
    
    tempoms = (fim - inicio) * 1000
    print(f"Tempo de execução: {tempoms:.2f} ms")
    print(f"Consumo de memória: {memoria} KB")
    

    # salvar_lista_em_arquivo(lista, "arq_saida.txt")
    salvar_dados_em_planilha(tempoms, memoria, metodo, "resultadosPythonVM.csv")


if __name__ == '__main__':
    for i in range(10):
        medirDesempenho("ordenacao/python/arq_saida.txt")
        print(f"Execução {i+1} concluída!")