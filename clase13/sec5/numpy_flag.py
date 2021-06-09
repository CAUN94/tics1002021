import numpy

x = numpy.array([True,True,True])
y = numpy.array([True,False,False,False,False,False,False,False,False,False,False,False,False])
print(f"x: {x}")
print(f"y: {y}")
print()
print(f"x.all(): {x.all()}")
print(f"y.all(): {y.all()}")
print(f"x.any(): {x.any()}")
print(f"y.any(): {y.any()}")