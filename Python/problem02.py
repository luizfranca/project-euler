# Even Fibonacci numbers
def problem(number):
	x1, x2, value = 0, 1, 0
	while x2 < number:
		x1, x2 = x2, x1 + x2 
		if x2 % 2 != 0: continue
		value += x2
	print value

problem(4000000)