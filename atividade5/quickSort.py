def quickSort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[len(lista) // 2]  # Escolhe o pivô como o elemento do meio
        menores = [x for x in lista if x < pivo]  # Elementos menores que o pivô
        iguais = [x for x in lista if x == pivo]  # Elementos iguais ao pivô
        maiores = [x for x in lista if x > pivo]  # Elementos maiores que o pivô
        return quickSort(menores) + iguais + quickSort(maiores)