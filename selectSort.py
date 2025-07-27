listaNumeros = [7, 10, 3, 9, 1, 6, 2, 8, 4, 5]
listaNomes = ["Pedro", "Joao", "Ana Paula", "Ana Carolina", "José", "Ricardo"]
def selectSort(listaTeste, reverse=False):
    ## lembrando que não percorremos os itens da lista mas sim os index
    ## Não precisamos percorrer o Array inteiro. Na ultima iteração, os valores ja vão estar todos organizados. 
    for i in range(len(listaTeste) - 1):
        ## Definimos o primeiro valor que encontramos como o menor valor atual.
        menorValorAtual = i
        ## Vamos percorrer todos os itens que estão a cima de i
        for j in range(i + 1, len(listaTeste)):
            if not reverse:
                if listaTeste[menorValorAtual] > listaTeste[j]:
                    menorValorAtual = j
            else:
                if listaTeste[menorValorAtual] < listaTeste[j]:
                    menorValorAtual = j
        ## Se encontrou algum numero menor que i       
        ## Substituimos o item da posição de i para a posicao do menor valor atual e vice  e versa. 
        if menorValorAtual != i:
            menorValorAntigo = listaTeste[i]
            menorValorNovo = listaTeste[menorValorAtual]
            listaTeste[i] = menorValorNovo
            listaTeste[menorValorAtual] = menorValorAntigo

    print(listaTeste)

    

selectSort(listaNumeros, True)
selectSort(listaNomes, False)


