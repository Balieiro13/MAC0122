import numpy as np

class Point3D:
	def __init__(self, coords=[0,0,0]):
		self.array = np.array(coords)
		self.coords=list(self.array)

	def __str__(self):
		s = f'({str(self.coords)[1:-1]})'
		return s

	def __add__(self, other):
		soma = [0,0,0]
		if type(other) == int or type(other)==float:
			soma = self.array + other
			return Point3D(soma)
		soma = self.array + other.array
		return Point3D(list(soma))

	def __radd__(self, other):
		return self+other

	def coord(self):
		coord = self.coords[:]
		return coord

	def media(self):
		return self.array.mean()


p0 = Point3D([3,3,3])

print(p0+1)