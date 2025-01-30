from heapSort import heapSort
from quickSort import quickSort
from mergeSort import mergeSort
from gerarLista import gerarLista
import tracemalloc
import time

# gerarLista(100000, "atividade5/lista100000.txt")

def medir_tempo_memoria(algoritmo, lista):
    tempos = []
    memorias = []
    for _ in range(2):  # Executa duas vezes e tira a média
        tracemalloc.start()
        inicio = time.time()
        algoritmo(lista[:])  # Executa o algoritmo de sorting
        fim = time.time()
        memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        tempos.append((fim - inicio) * 1000)  # Tempo em milissegundos
        memorias.append(memoria_pico / 1024)  # Memória em KB

    return sum(tempos) / len(tempos), sum(memorias) / len(memorias)

if __name__ == '__main__':
    # Abrir os arquivos e transformar em listas
    listas = {}
    for tamanho in [10000, 50000, 100000]:
        with open(f"atividade5/lista{tamanho}.txt", "r") as file:
            listas[tamanho] = list(map(int, file.read().splitlines()))

    # Medir tempos de execução e uso de memória
    resultados = {}
    for tamanho, lista in listas.items():
        resultados[f"quickSort_{tamanho}"] = medir_tempo_memoria(quickSort, lista)
        resultados[f"heapSort_{tamanho}"] = medir_tempo_memoria(heapSort, lista)
        resultados[f"mergeSort_{tamanho}"] = medir_tempo_memoria(mergeSort, lista)

    # Exibir os resultados
    for chave, (tempo, memoria) in resultados.items():
        print(f"{chave}: {tempo:.2f} ms, {memoria:.2f} KB")
