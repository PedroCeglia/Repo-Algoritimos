listaNumeros = [7, 10, 3, 9, 1, 6, 2, 8, 4, 5]
listaNomes = ["Pedro", "Joao", "Ana Paula", "Ana Carolina", "José", "Ricardo"]

def mergeSort(listaTeste):
    if len(listaTeste) <= 1:
        return listaTeste
    
    divisorVetor = len(listaTeste) // 2
    arr1 = mergeSort(listaTeste[:divisorVetor])
    arr2 = mergeSort(listaTeste[divisorVetor:])
    
    return merge(arr1, arr2)

def merge(arr1, arr2):
    resultado = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            resultado.append(arr1[i])
            i += 1
        else:
            resultado.append(arr2[j])
            j += 1
    
    ## Quando finalizar uma das pilhas, adicionar todos os itens da outra pilha
    resultado.extend(arr1[i:])
    resultado.extend(arr2[j:])
    return resultado

resultado = mergeSort(listaNumeros)
print(resultado)

resultado2 = mergeSort(listaNomes)
print(resultado2)