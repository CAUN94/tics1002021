def comp(p1,p2):
    if len(p1)!=len(p2):
        return -1
    respuesta = [0,0,0]

    for i in range(len(p1)):
        if p1[i] < p2[i]:
            respuesta[0] += 1
        if p1[i] == p2[i]:
            respuesta[1] += 1
        if p1[i] > p2[i]:
            respuesta[2] += 1
    return respuesta


P1 = [0,0,2,4,1,2]
P2 = [1,1,3,4,0,2]

print(comp(P1,P2))