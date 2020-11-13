import sys

pri = int(sys.argv[-1])

def primo(max):
	eras={}
	p = 2
	while p < max:
		if p not in eras:
			yield p
			eras[p*p] = [p]
		else:
			for q in eras[p]:
				eras.setdefault(q + p, []).append(q)
			del eras[p]
		p += 1

print(primo(pri))
