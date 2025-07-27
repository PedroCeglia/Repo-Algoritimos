# 2606
# SPOJ

def teste(a, g, rA, rG ):
    kmGas = rG / g
    kmAlc = rA / a
    if kmAlc < kmGas:
        return "A" 
    else:
        return "G"

a = teste(1.2 , 2.3 ,10.0, 15.0)
b = teste(1.00, 1.00, 9.00, 9.01)
c = teste(1.00, 1.00, 10.00, 10.00)

#print(a)
#print(b)   
#print(c)

def algoritimoProfessor(A, G, Ra, Rg):
    #A, G, Ra, Rg = map(float, input().split())
    Va = A / Ra
    Vg = G/Rg
    if(Vg <= Va):
        print("G")
    else:
        print("A")

aP = algoritimoProfessor(1.2 , 2.3 ,10.0, 15.0)
bP = algoritimoProfessor(1.00, 1.00, 9.00, 9.01)
cP = algoritimoProfessor(1.00, 1.00, 10.00, 10.00)

