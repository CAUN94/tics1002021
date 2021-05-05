import math

z = int(input("z: "))
numiter = int(input("numiter: "))

suma = 0
for k in range(0,numiter+1):
    suma += math.pow(z,k)/math.factorial(k)

print(f"La suma es {suma}")
