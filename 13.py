from functools import reduce
def prod(L):
	def mul(x,y):
		return x*y
	return reduce(mul,L)
print('3*5*7*9=',prod([3,5,7,9]))