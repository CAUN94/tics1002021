import numpy

a = [1,2,3]
b = numpy.array([1,2,3])

print(a)
print(b)

a.append(4)
b = numpy.append(b,[4])

print(a)
print(b)

a.append(5)
a.append(6)
b = numpy.append(b,[5,6])

print(a)
print(b)

print(f"{len(b)} vs {b.size}")