# Smallest multiple
def problem(n):
	number = n
	while True:
		for i in range(n, 0, -1):
			if number % i != 0:
				break
		else:
			print number
			return
		number += n
problem(20)