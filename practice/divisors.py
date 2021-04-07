def Div(n):
	A = []
	for a in range(n):
		a += 1
		if (n % a == 0):
			A.append(a)
	return A

def IsPrime(n):
	if Div(n) == [1] or Div(n) == [1,n]:
		return True
	else:
		return False

def PrimeDiv(n):
	P = []
	for i in Div(n):
		if IsPrime(i):
			P.append(i)
	return P

def PrimesUpTo(n):
	P = []
	for i in range(n):
		if IsPrime(i):
			P.append(i)
	return P

