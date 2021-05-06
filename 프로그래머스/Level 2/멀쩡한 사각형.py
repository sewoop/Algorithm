from math import gcd
def solution(w, h):
	common = gcd(w, h)
	
	# common * ((w // common) + (h // common) - 1)
	# >> (w + h - common)
	return w * h - (w + h - common)