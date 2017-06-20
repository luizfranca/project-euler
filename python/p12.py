# Project Euler
# Problem 12
# Highly divisible triangular number
primes = [2, 3, 5, 7]

def isPrime(number):
	if number == 1 or (number % 2 == 0 and number != 2):
		return False

	start = number / 2
	start = start if start % 2 != 0 else start + 1

	for i in range(start, 2, -2) :
		if number % i == 0:
			return False
	return True

def nextPrime():
	number = primes[-1] + 2
	
	while not isPrime(number):
		number += 2

	primes.append(number)

def numberDivisors(number):
	if number == 0:
		return 0
	elif number == 1:
		return 1

	index = 0
	count, currCount = 1, 1
	
	curr = number

	while curr != 1:
		prime = primes[index]

		if (curr % prime == 0):
			curr /= prime

			currCount += 1
		else:
			count *= currCount
			currCount = 1
			index +=1
			if len(primes) <= index:
				nextPrime()

	count *= currCount

	return count

def hdtn(n):
	i = 0
	triangle = 0
	divisors = 0

	while (divisors <= n):
		divisors = numberDivisors(triangle)
		if divisors >= n:
			break

		i += 1
		triangle += i

	print "Divisors: " + str(divisors) + " triangle: " + str(triangle) + " n: " + str(n) + " i: " + str(i)

hdtn(500)