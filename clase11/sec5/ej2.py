import math

def dist(p1,p2):
    if len(p1) != len(p2):
        return -1
    suma = 0
    for i in range(len(p1)):
        temp = (p2[i]-p1[i])**2
        suma += temp
    return math.sqrt(suma)

P1 = [0,0,0,0]
P2 = [1,1,1,1]

print(dist(P1,P2))