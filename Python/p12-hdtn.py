# Project Euler
# Problem 12
# Highly divisible triangular number

def getNextPrimer(primers):
	return 0

def numberDivisors(number): # re do
	count = 0
	for i in range(1, (number / 2) + 1):
		if (number % i == 0):
			count += 1
	if number > 0:
		count += 1
	return count

def hdtn(n):
	i = 0
	triangle = 0
	divisors = 0

	while (divisors < n):
		divisors = numberDivisors(triangle)
		if divisors > n:
			break

		i += 1
		triangle += i

	print "Divisors: " + str(divisors) + " triangles: " + str(triangle) + " n: " + str(n) + " i: " + str(i)

# hdtn(150)
print numberDivisors(28)

