# Special Pythagorean triplet
import math

def pythagorean_Triplet(n):
	number = 0

	for a in range(1, n):
		for b in range(1, n):
			c = math.sqrt(a ** 2 + b ** 2)
			if c % 1 == 0:
				number = a + b + int(c)

			c = int(c)
			
			if number == n:
				return a * b * c

print pythagorean_Triplet(1000)