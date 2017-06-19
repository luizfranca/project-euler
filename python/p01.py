# Multiples of 3 and 5
def problem(number):	
	print sum([i for i in range(1, number) if i % 3 == 0 or i % 5 == 0])

problem(1000)