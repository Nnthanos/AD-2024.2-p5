import heapq

def heapSort(lista):
    heapq.heapify(lista)  # Converte a lista em uma heap
    return [heapq.heappop(lista) for _ in range(len(lista))]  # Extrai os elementos em ordem