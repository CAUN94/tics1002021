i = 1
while i < 5:
    j = 1
    while j <= i//2+1:
        print(f"{i},{j}")
        j = j+1
    i = i+1


# i:1 , j:1 // Primera iteracion
# 1,1 j:1
# i:2 , j:1 // Segunda iteracion
# 2,1 j: 1
# 2,2 j: 2
# i:3 , j:1 // Tercera iteracion
# 3,1 j: 1
# 3,2 j: 2
# i: 4, j:1 // Cuarta iteraciom
# 4,1 j: 1
# 4,2 j: 2
# 4,3 j: 3

