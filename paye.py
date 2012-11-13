def paye(salary):
	"""
		calculates kenyan paye but excludes relief.
		todo: floating point, edge cases, -ve salary, error handling
	"""	
	if salary>0 and salary<10165:
		paye = salary* 0.1
		return paye
		
	elif salary>10165 and salary<19741:
		paye = 1016 +((salary-10165)*0.15)
		return paye
	
	elif salary>19741 and salary<29317:
		paye = 2452 + ((salary-19741)* 0.2)
		return paye
		
	elif salary >29317 and salary < 38893 :
		paye = 4367 + ((salary-29317)*0.25)
		return paye
		
	elif salary>38893:
		paye = 6761+ ((salary - 38892)*0.3)
		return paye
		
	else:
		print "Mind blown"
		
		
	
		
		