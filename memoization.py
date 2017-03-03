
factorialCache = {}

def factorial(a):
	if a in factorialCache:
		return factorialCache[a]
	else:
		out = 1 if a<=1 else a*factorial(a-1)
		factorialCache[a] = out
		return out

for i in range(0, 100000):
	print(factorial(i//1000))
