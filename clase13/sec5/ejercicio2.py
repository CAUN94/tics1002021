import numpy

notas = numpy.array([2,2.2,7,6.5,6.2])

min = notas.min()
max = notas.max()
mean = round(notas.mean(),1)

print(f"min: {min}")
print(f"max: {max}")
print(f"mean: {mean}")
