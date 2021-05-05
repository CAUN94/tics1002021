i = 1
while i < 5:
    j = 1
    while j <= i//2+1:
        print(f'{i},{j}')
        j = j+1
    i = i+1

# i = 1, j = 1 // Primera Iteracion
# 1,1
# i = 2, j = 1 // Segunda Iteracion
# 2,1
# 2,2
# i = 3, j = 1 // Tercera Iteración
# 3,1
# 3,2
# i = 4, j = 1 // Cuarta Iteración
# 4,1
# 4,2
# 4,3
