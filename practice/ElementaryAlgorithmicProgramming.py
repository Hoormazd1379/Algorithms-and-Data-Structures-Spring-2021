def minimum(A):
	min = None
	for a in A:
		if min == None or min > a:
			min = a
	return min

def position_in_sequence(A,x):
	for a in range (len(A)):
		if A[a] == x:
			return a
	return -1

def count_lower(A,x):
	count = 0
	for a in A:
		if a < x:
			count += 1
	return count

def check_sorted(A):
	for a in range(len(A)):
		if a > 0 and A[a] < A[a-1]:
			return False
	return True

def log_base_two(n):
	log = 0
	for a in range((n//2)+1):
		if (2**a) <= n:
			log = a
	return log

def maximum(A):
	max = None
	for a in A:
		if max == None or max < a:
			max = a
	return max

def maximal_difference(A):
	return maximum(A)-minimum(A)


