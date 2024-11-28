def mergeSort(lista):
    if len(lista) > 1:
        # Dividir a lista no meio
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        # Recursivamente ordenar as duas metades
        mergeSort(esquerda)
        mergeSort(direita)

        # Mesclar as duas metades ordenadas
        i = j = k = 0

        # Combinar os valores de 'esquerda' e 'direita' na lista original
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        # Adicionar os elementos restantes da esquerda (se houver)
        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        # Adicionar os elementos restantes da direita (se houver)
        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1
    
    return lista