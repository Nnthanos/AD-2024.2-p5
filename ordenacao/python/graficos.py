import pandas as pd
import matplotlib.pyplot as plt

def criar_graficos():
    # Ler o arquivo Excel
    array = []
    try:
        dados_xlsx = pd.read_excel("resultados.xlsx")
    except Exception as e:
        print(f"Erro ao ler o arquivo Excel: {e}")
        return

    # Ler o arquivo CSV
    try:
        dados_csv = pd.read_csv("resultadosJava.csv")
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")
        return

    dados_xlsx_mergeSortPy = dados_xlsx[dados_xlsx["Metodo"] == "mergeSortPy"]
    dados_xlsx_bubbleSortPy = dados_xlsx[dados_xlsx["Metodo"] == "bubbleSortPy"]
    dados_csv_mergeSort = dados_csv[dados_csv["Metodo"] == "mergeSort"]
    dados_csv_bubbleSort = dados_csv[dados_csv["Metodo"] == "bubbleSort"]

    # Gráfico 1: Média do Tempo de Execução
    try:
        media_tempo_xlsx_mergeSortPy = dados_xlsx_mergeSortPy["Tempo de Execucao (ms)"].mean()
        media_tempo_xlsx_bubbleSortPy = dados_xlsx_bubbleSortPy["Tempo de Execucao (ms)"].mean()
        media_tempo_csv_mergeSort = dados_csv_mergeSort["Tempo de Execucao (ms)"].mean()
        media_tempo_csv_bubbleSort = dados_csv_bubbleSort["Tempo de Execucao (ms)"].mean()

        plt.figure(figsize=(10, 6))
        bar_width = 0.2
        x = range(2)
        plt.bar(x, [media_tempo_xlsx_mergeSortPy, media_tempo_xlsx_bubbleSortPy], width=bar_width, label="Python (Excel)", alpha=0.6, color='blue')
        plt.bar([i + bar_width for i in x], [media_tempo_csv_mergeSort, media_tempo_csv_bubbleSort], width=bar_width, label="Java (CSV)", alpha=0.6, color='green')
        plt.xticks([i + bar_width/2 for i in x], ['mergeSort', 'bubbleSort'])
        plt.xlabel("Método")
        plt.ylabel("Média do Tempo de Execução (ms)")
        plt.title("Média do Tempo de Execução")
        plt.legend()
        plt.grid(axis='y')
        plt.tight_layout()
        plt.savefig("media_tempo.png")
        plt.show()

    except KeyError as e:
        print(f"Erro ao calcular média do tempo de execução: {e}")

    # Gráfico 2: Mediana do Tempo de Execução
    try:
        mediana_tempo_xlsx_mergeSortPy = dados_xlsx_mergeSortPy["Tempo de Execucao (ms)"].median()
        mediana_tempo_xlsx_bubbleSortPy = dados_xlsx_bubbleSortPy["Tempo de Execucao (ms)"].median()
        mediana_tempo_csv_mergeSort = dados_csv_mergeSort["Tempo de Execucao (ms)"].median()
        mediana_tempo_csv_bubbleSort = dados_csv_bubbleSort["Tempo de Execucao (ms)"].median()

        plt.figure(figsize=(10, 6))
        plt.bar(x, [mediana_tempo_xlsx_mergeSortPy, mediana_tempo_xlsx_bubbleSortPy], width=bar_width, label="Python (Excel)", alpha=0.6, color='blue')
        plt.bar([i + bar_width for i in x], [mediana_tempo_csv_mergeSort, mediana_tempo_csv_bubbleSort], width=bar_width, label="Java (CSV)", alpha=0.6, color='green')
        plt.xticks([i + bar_width/2 for i in x], ['mergeSort', 'bubbleSort'])
        plt.xlabel("Método")
        plt.ylabel("Mediana do Tempo de Execução (ms)")
        plt.title("Mediana do Tempo de Execução")
        plt.legend()
        plt.grid(axis='y')
        plt.tight_layout()
        plt.savefig("mediana_tempo.png")
        plt.show()

    except KeyError as e:
        print(f"Erro ao calcular mediana do tempo de execução: {e}")

    # Gráfico 3: Média do Consumo de Memória
    try:
        media_memoria_xlsx_mergeSortPy = dados_xlsx_mergeSortPy["Consumo de Memoria (KB)"].mean()
        media_memoria_xlsx_bubbleSortPy = dados_xlsx_bubbleSortPy["Consumo de Memoria (KB)"].mean()
        media_memoria_csv_mergeSort = dados_csv_mergeSort["Consumo de Memoria (KB)"].mean()
        media_memoria_csv_bubbleSort = dados_csv_bubbleSort["Consumo de Memoria (KB)"].mean()

        plt.figure(figsize=(10, 6))
        plt.bar(x, [media_memoria_xlsx_mergeSortPy, media_memoria_xlsx_bubbleSortPy], width=bar_width, label="Python (Excel)", alpha=0.6, color='blue')
        plt.bar([i + bar_width for i in x], [media_memoria_csv_mergeSort, media_memoria_csv_bubbleSort], width=bar_width, label="Java (CSV)", alpha=0.6, color='green')
        plt.xticks([i + bar_width/2 for i in x], ['mergeSort', 'bubbleSort'])
        plt.xlabel("Método")
        plt.ylabel("Média do Consumo de Memória (KB)")
        plt.title("Média do Consumo de Memória")
        plt.legend()
        plt.grid(axis='y')
        plt.tight_layout()
        plt.savefig("media_memoria.png")
        plt.show()

    except KeyError as e:
        print(f"Erro ao calcular média do consumo de memória: {e}")

    # Gráfico 4: Mediana do Consumo de Memória
    try:
        mediana_memoria_xlsx_mergeSortPy = dados_xlsx_mergeSortPy["Consumo de Memoria (KB)"].median()
        mediana_memoria_xlsx_bubbleSortPy = dados_xlsx_bubbleSortPy["Consumo de Memoria (KB)"].median()
        mediana_memoria_csv_mergeSort = dados_csv_mergeSort["Consumo de Memoria (KB)"].median()
        mediana_memoria_csv_bubbleSort = dados_csv_bubbleSort["Consumo de Memoria (KB)"].median()

        plt.figure(figsize=(10, 6))
        plt.bar(x, [mediana_memoria_xlsx_mergeSortPy, mediana_memoria_xlsx_bubbleSortPy], width=bar_width, label="Python (Excel)", alpha=0.6, color='blue')
        plt.bar([i + bar_width for i in x], [mediana_memoria_csv_mergeSort, mediana_memoria_csv_bubbleSort], width=bar_width, label="Java (CSV)", alpha=0.6, color='green')
        plt.xticks([i + bar_width/2 for i in x], ['mergeSort', 'bubbleSort'])
        plt.xlabel("Método")
        plt.ylabel("Mediana do Consumo de Memória (KB)")
        plt.title("Mediana do Consumo de Memória")
        plt.legend()
        plt.grid(axis='y')
        plt.tight_layout()
        plt.savefig("mediana_memoria.png")
        plt.show()

    except KeyError as e:
        print(f"Erro ao calcular mediana do consumo de memória: {e}")

if __name__ == "__main__":
    criar_graficos()
