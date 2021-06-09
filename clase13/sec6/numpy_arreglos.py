import numpy

a = numpy.zeros(5,)
print(a)
print(a[2])

b = numpy.ones(5,)
print(b)
print(b[2])

c = numpy.full(5,7)
print(c)
print(c[2])

# d = numpy.random.random(5,)
# print(d)
# print(d[2])

e = numpy.random.randint(5,size=5)
print(e)
print(e[2])