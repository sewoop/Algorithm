from collections import Counter
def solution(s):
	a = b = 0
	while s != "1":
		a += 1
		
		# Counter is faster than list.count()
		# Counter is dictionary : O(1) -> O(N)
		# list.count()'s time complexity : O(N) -> O(N^2)
		one = Counter(s)['1']
		b += len(s) - one
		s = bin(one)[2:]
	return [a, b]