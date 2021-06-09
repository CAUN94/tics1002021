import numpy

a = numpy.array([True,True,True,True,True])
b = numpy.array([True,False,False,False,False,False,False,False,False,False,False,False,False])

print(a.all())
print(a.any())

print(b.all())
print(b.any())