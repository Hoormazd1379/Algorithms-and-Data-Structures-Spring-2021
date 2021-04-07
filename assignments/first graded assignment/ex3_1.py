def powerset(A):
	if len(A) <= 0:
		yield []
	else:
		for a in powerset(A[1:]):
			yield [A[0]]+a
			yield a

def sum_of_set(A):
	sum = 0
	for a in A:
		sum += a

	return sum

def equal_sum_seq(A):
	check_equal_sum_seq([x for x in powerset(A)])

def check_equal_sum_seq(A):

	try:
		sub = sum(A.pop())

		for a in A:
			if sum(a) == sub:
				print ('True')
				return True
				break
			
		check_equal_sum_seq(A)
	except:
		print('False')
		return False

