def first_unique(A):

	for a in A:
		n = 0 # Number of occurances
		for b in A:
			if a == b:
				n+=1
		if n == 1:
			return(a)
			break
