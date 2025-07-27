def acharValorPI():
    valorBase = 4
    listaValores = [3.14, 4.141, 3.1415, 3.14159, 3.141592, 3.1415926, 3.14159265, 3.141592653, 3.1415926535, 3.14159265358, 3.141592653589, 3.1415926535897, 3.14159265358979, 3.141592653589793, 3.1415926535897932, 3.14159265358979323, 3.141592653589793238, 3.1415926535897932384]
    
    for valorAproximadoPI in listaValores:
        denominandor = 3
        isPlus = False
        valor = 4
        valorMaisProximo = valorBase
        counter = 0
        while True:
            counter += 1
            
            valorSequencia = valorBase / denominandor

            if isPlus:
                valor += valorSequencia
            else:
                valor -= valorSequencia
                
            isPlus = not isPlus
            denominandor += 2
        
            valorAproximado = acharValorMaisProximo(valor, valorMaisProximo, valorAproximadoPI)
            if valorAproximado["id"] == "antigo":
                print(f"O algoritimo finalizou em {counter} iterações")
                print(f"O valor mais proximo de PI foi {valorAproximado["valorAntigo"]}")
                break
            else:
                valorMaisProximo = valor


def acharValorMaisProximo(valorNovo, valorAntigo, valorComparacao):
    diferencaValorNovo = 0
    diferencaValorAntigo = 0
    
    if valorNovo > valorComparacao:
        diferencaValorNovo = valorNovo - valorComparacao
    else:
        diferencaValorNovo = valorComparacao - valorNovo

    if valorAntigo > valorComparacao:
        diferencaValorAntigo = valorAntigo - valorComparacao
    else:
        diferencaValorAntigo = valorComparacao - valorAntigo

    if diferencaValorNovo < diferencaValorAntigo:
        return {"id":"novo", "valorNovo":valorNovo,  "valorAntigo":valorAntigo, "diferencaAntiga": diferencaValorAntigo, "diferencaNova": diferencaValorNovo}
    else:
        return {"id":"antigo", "valorNovo":valorNovo, "valorAntigo":valorAntigo, "diferencaAntiga": diferencaValorAntigo, "diferencaNova": diferencaValorNovo}


#acharValorPI()

def codigoProfessor():
    pi = 0
    s = -1
    i = j = 0
    l = [3.14, 3.141, 3.1415, 3.14159, 141592, 1415926]

    while j < len(l):
        s = s * -1
        pi = pi + (4 * s) / (2*i +1)
        i = i + 1
        if(round(pi, j+2) == l[j]):
            print(l[j], "encontrou com", i, "passos")
            j = j + 1

codigoProfessor()