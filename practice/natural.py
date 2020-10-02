class Natural:
	def __init__(self, N):
		self.max = N

	def __iter__(self):
		self.n1 = 0
		self.n2 = 1
		return self

	def __next__(self):
		natural = self.n1
		if natural > self.max:
			raise StopIteration
		self.n1 = self.n2
		self.n2 +=1
		return natural


