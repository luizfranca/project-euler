# Largest prime factor
import math

def problem(number):
	for i in xrange(int(math.ceil(math.sqrt(number))), 5, -1):
		for j in xrange(2, int(math.ceil(math.sqrt(i)))):
			if i % j == 0:
				break
		else:
			if number % i == 0:
				print i
				break

problem(600851475143)