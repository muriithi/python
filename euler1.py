def  euler1():
	""" Add all the natural numbers below 
	one thousand that are multiples of 3 or 5."""
	sum = 0
	for i in range (1 ,1000):
		if (i %3) ==0 or (i% 5) == 0:
			sum = sum + i
	return sum
			
			
		