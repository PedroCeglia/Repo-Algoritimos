
listaTesteNumeros = [ 
    1, 2, 3, 4, 5, 6, 7, 8, 9, 
    10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
    20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 
    30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 
    40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 
    50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 
    60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 
    70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 
    80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 
    90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100
]

listaTesteNomes = [
    "Adriana", "Afonso", "Alan", "Alberto", "Alexandre", "Alice", "Aline", "Amanda",
    "Ana Beatriz", "Ana Clara", "Ana Júlia", "André", "Antônio", "Arthur", "Bárbara",
    "Beatriz", "Bianca", "Bruno", "Caio", "Camila", "Carla", "Carlos", "Carolina",
    "Cecília", "Clara", "Cláudio", "Cristina", "Daniel", "Daniela", "Danilo", "Davi",
    "Diego", "Eduardo", "Elaine", "Elias", "Elisa", "Emanuel", "Emerson", "Enzo",
    "Estela", "Fabiana", "Fabrício", "Felipe", "Fernanda", "Fernando", "Flávia",
    "Francisco", "Gabriel", "Gabriela", "Giovana", "Gilberto", "Gustavo", "Helena",
    "Henrique", "Hugo", "Igor", "Ingrid", "Isabela", "Isadora", "Iuri", "João Gabriel",
    "João Miguel", "João Pedro", "Joaquim", "Jorge", "José", "Júlia", "Juliana", "Karina",
    "Kauã", "Lara", "Larissa", "Laura", "Leonardo", "Letícia", "Lívia", "Lorena",
    "Lucca", "Lucas", "Luciana", "Luciano", "Luísa", "Luís Fernando", "Manuella",
    "Marcelo", "Mariana", "Marina", "Mateus", "Matheus", "Melissa", "Miguel", "Murilo",
    "Natália", "Nicole", "Otávio", "Patrícia", "Paula", "Paulo", "Pedro", "Priscila"
]

def buscaBinaria(listaTeste, chaveBusca, activeLogs=False):
    contadorDeRepeticoes = 0
    inicioSubVetor = 0
    finalSubVetor = len(listaTeste) - 1

    while True:
        contadorDeRepeticoes += 1
        if activeLogs:
            print("COUNTER", contadorDeRepeticoes)
            print("INICIO SUB VETOR", inicioSubVetor)
            print("FINAL SUB VETOR", finalSubVetor)
            print("----------------------------------------")

        if inicioSubVetor > finalSubVetor:
            return "NÃO ENCONTRADO"
        
        divisorVetor = int((inicioSubVetor + finalSubVetor) / 2)


        if  listaTeste[divisorVetor] == chaveBusca:
            if not activeLogs:
                print(f"COUNTER: {contadorDeRepeticoes}")
            return divisorVetor
        
        if listaTeste[divisorVetor] > chaveBusca:
            finalSubVetor = divisorVetor - 1
        
        if listaTeste[divisorVetor] < chaveBusca:
            inicioSubVetor = divisorVetor + 1


def buscaBinariaRecursiva(listaTeste, chaveBusca, inicioSubVetor, finalSubVetor):

    if inicioSubVetor > finalSubVetor:
        return "NÃO ENCONTRADO"
    
    divisorVetor = int((inicioSubVetor + finalSubVetor) / 2)


    if  listaTeste[divisorVetor] == chaveBusca:
        return divisorVetor
    
    if listaTeste[divisorVetor] > chaveBusca:
        return buscaBinariaRecursiva(listaTeste , chaveBusca, inicioSubVetor, divisorVetor - 1)
    
    if listaTeste[divisorVetor] < chaveBusca:
        return buscaBinariaRecursiva(listaTeste , chaveBusca, divisorVetor + 1, finalSubVetor)

    
    

    
# Duvida em relação ao arredondamento.
# 5.4 = 5 && 5.5 == 6 
# Isso pode gerar algum erro para a busca binaria?

resultado = buscaBinariaRecursiva(listaTesteNomes, "Pedro", 0, len(listaTesteNomes) - 1)
print(resultado, listaTesteNomes[resultado])
resultado2 = buscaBinariaRecursiva(listaTesteNomes, "Felipe", 0, len(listaTesteNomes) - 1)
print(resultado2, listaTesteNomes[resultado2])
resultado3 = buscaBinariaRecursiva(listaTesteNomes, "João", 0, len(listaTesteNomes) - 1)
print(resultado3)
resultado4 = buscaBinariaRecursiva(listaTesteNomes, "Ana Clara", 0, len(listaTesteNomes) - 1)
print(resultado4, listaTesteNomes[resultado4])
resultado5 = buscaBinariaRecursiva(listaTesteNomes, "Nicole", 0, len(listaTesteNomes) - 1)
print(resultado5, listaTesteNomes[resultado5])
resultado6 = buscaBinariaRecursiva(listaTesteNomes, "Nicoli", 0, len(listaTesteNomes) - 1)
print(resultado6)


