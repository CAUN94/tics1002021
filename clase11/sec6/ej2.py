import math

def dist(P1,P2):
    if len(P1) != len(P2):
        return -1
    suma = 0
    for i in range(len(P1)):
        resta = (P2[i]-P1[i])**2
        suma += resta
    return math.sqrt(suma)
P1 = [0,0,1,2]
P2 = [1,1,2,2]
print(dist(P1,P2))