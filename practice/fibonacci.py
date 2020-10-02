class Fibo:
	def __init__(self, final):
		self.final = final

	def __iter__(self):
		self.a = 0
		self.b = 1
		return self

	def __next__(self):
		fib = self.a
		if fib > self.final:
			raise StopIteration
		self.a, self.b = self.b, self.a + self.b
		return fib
