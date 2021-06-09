import numpy

a = numpy.random.randint(1,10,size=10)
print(a)

a = numpy.append(a,[7,8,9])
print(a)

for i in range(3):
    nr = int(input('Dame un nr: '))
    a = numpy.append(a,[nr])
print(a)