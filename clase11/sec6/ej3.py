def comp(p1,p2):
    if(len(p1) != len(p1)):
        return -1
    resp = [0,0,0]

    for i in range(len(p1)):
        if(p1[i] < p2[i]):
            resp[0] += 1 
        if(p1[i] == p2[i]):
            resp[1] += 1 
        if(p1[i] > p2[i]):
            resp[2] += 1 
    
    return resp
p1 = [0,0,2,4,1,2]
p2 = [1,1,3,4,0,2]

print(comp(p1,p2))