class Primo:
	def __init__(self, lim):
		self.lim=lim
		self.eras = {}

	def __iter__(self):
		self.p = 2
		self.q = 3
		return self

	def __next__(self):
		p = self.p
		if p > self.lim:
			raise StopIteration

		if p not in self.eras:
			self.eras[p*p] = [p]
			self.p = self.q
			self.q += 1
			return p
		else:
			for q in self.eras[p]:
				self.eras.setdefault(q+ p, []).append(q)
			del self.eras[p]
		self.p = self.q
		self.q += 1
		return p


print(list(Primo(100)))