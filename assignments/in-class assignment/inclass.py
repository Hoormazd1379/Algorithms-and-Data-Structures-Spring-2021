def like_or_dislike(A):

	likes = 0
	dislikes = 0
	for a in A:
		if a == 'like':
			likes += 1
		elif a == 'dislike':
			dislikes += 1
	if likes > dislikes:
		return 'like'
	elif likes < dislikes:
		return 'dislike'
	else:
		return 'undecided'


def stops_and_inversions(P):

	direction = None
	pp = None
	stops = 0
	inversions = 0
	stopped = 1

	for p in P:

		if pp == None:
			pp = p
		else:
			if p > pp and direction == 'neg':
				direction = 'pos'
				inversions += 1
			elif p > pp and direction == None:
				direction = 'pos'

			elif p < pp and direction == 'pos':
				direction = 'neg'
				inversions += 1
			elif p < pp and direction == None:
				direction = 'neg'

		if stopped == 1 and p != pp:
			stopped = 0
		elif stopped == 0 and p == pp:
			stops += 1
			stopped  = 1

		pp = p


	print('stops: ', stops)
	if inversions > 0:
		print('inversions: ', inversions)
