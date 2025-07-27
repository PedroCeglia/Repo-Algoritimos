# 3828
# Ache todos os numeros primos até um determinado numero inteiro positivo. Algoritmo de Eratóstenes.

## Forma Burra
def algoritmoEratostenesErrado(n):
    counter = 0
    if n < 2:
        return "nao"
    for i in range(2, n + 1):
        for j in range(2, n + 1):
            counter += 1
            if i * j == n:
                print(counter)
                return "nao"
    print(counter)
    return "sim"


def teste(n):
    counter = 0
    numeros = [True] * (n + 1)
    for i in range(2, n + 1):
        if numeros[i]:
            for j in range(2, n + 1):
                counter += 1
                if (i * j) <= n:
                    numeros[i * j] = False
    print(counter)
    for i, v in enumerate(numeros):
        if v:
            print(i, v)


def teste2(n):
    counter = 0
    numeros = [True] * (n + 1)
    for i in range(2, int(n**0.5) + 1):
        if numeros[i]:
            for j in range(2, n + 1):
                counter += 1
                if (i * j) <= n:
                    numeros[i * j] = False
    print(counter)

    for i, v in enumerate(numeros):
        if v:
            x = teste3(i)
            print(i, x)

def teste3(n):
    isPrimo = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            isPrimo = False
    return "sim" if isPrimo else "nao"
	
z = teste3(4294967291)	
#print(z)

def algoritimoProfessor():
    n = 101
    crivo = [True] * n
    
    crivo[0] = crivo[1] = False
    i = 2
    while (i < n/2):
        if (crivo[i] ==  1):
            for j in range(2 * i, n, i):
                crivo[j] = False
        i += 1
    for i in range(n):
        if crivo[i]:
            print(i, end=", ")

algoritimoProfessor()