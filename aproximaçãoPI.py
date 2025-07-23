# DEU RUIM

def acharValorPI():
    valorBase = 4
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
            isPlus = False
        else:
            valor -= valorSequencia
            isPlus = True

        denominandor += 2
    
        valorAproximado = acharValorMaisProximo(valor, valorMaisProximo, 3.14159)
        if valorAproximado["id"] == "antigo":
            print(f"O algoritimo finalizou em {counter} iterações")
            print(f"O valor mais proximo de PI foi {valorAproximado}")
            break
        else:
            print(f"O novo numero é mais proximo de pi")
            print(f"O valor mais proximo de PI foi {valorAproximado}")


def acharValorMaisProximo(valorNovo, valorAntigo, valorComparacao):
    diferencaValor1 = 0
    diferencaValor2 = 0
    
    if valorNovo > valorComparacao:
        diferencaValor1 = valorNovo - valorComparacao
    else:
        diferencaValor1 = valorComparacao - valorNovo

    if valorAntigo > valorComparacao:
        diferencaValor2 = valorAntigo - valorComparacao
    else:
        diferencaValor2 = valorComparacao - valorAntigo

    if diferencaValor1 > diferencaValor2:
        return {"id":"novo", "valorNovo":valorNovo,  "valorAntigo":valorAntigo, "diferencaAntiga": diferencaValor2, "diferencaNova": diferencaValor1}
    else:
        return {"id":"antigo", "valorNovo":valorNovo, "valorAntigo":valorAntigo, "diferencaAntiga": diferencaValor2, "diferencaNova": diferencaValor1}


acharValorPI()
