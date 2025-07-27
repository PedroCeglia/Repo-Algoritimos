listaNumeros = [7, 10, 3, 9, 1, 6, 2, 8, 4, 5]
listaNomes = ["Pedro", "Joao", "Ana Paula", "Ana Carolina", "José", "Ricardo"]

## Verifica se o numero que antecede "i" é menor do que i
## Ordena deslocando o menor numero para a esquerda
def insertionSort(listaTeste):
    for i in range(1, len(listaTeste)):
        chaveInicial = listaTeste[i]
        deslocamento = i - 1
        for j in range(i - 1, -1, -1):
            if listaTeste[j] > chaveInicial:
                listaTeste[j + 1] = listaTeste[j]
                j -= 1
                deslocamento -= 1
        listaTeste[deslocamento + 1] = chaveInicial
            
    print(listaTeste)

insertionSort(listaNumeros)
insertionSort(listaNomes)


