import random

listaNumeros = [7, 10, 3, 9, 1, 6, 2, 8, 4, 5]
listaNomes = ["Pedro", "Joao", "Ana Paula", "Ana Carolina", "José", "Ricardo"]

def quickSort(listaTeste):
    if len(listaTeste) <= 1:
        return listaTeste

    pivo = random.choice(listaTeste)
    arr1 = [x for x in listaTeste if x < pivo]
    arr2 = [x for x in listaTeste if x > pivo]
    arrPivo = [x for x in listaTeste if x == pivo]
    return quickSort(arr1) + arrPivo + quickSort(arr2)

resultado = quickSort(listaNumeros)
print(resultado)

resultado2 = quickSort(listaNomes)
print(resultado2)