# Project Euler
# Problem 12
# Highly divisible triangular number
import sys, math

primes = [2, 3, 7]

def isPrime(number):
	if number == 1 or (number % 2 == 0 and number != 2):
		return False

	start = number / 2
	start = start if start % 2 != 0 else start + 1

	for i in range(start, 2, -2) :
		if number % i == 0:
			return False
	return True

def nextPrime(curr):
	number = curr + 1
	while not isPrime(number):
		number += 2

	primes.insert(number)

def numberDivisors(number): # re do
	count = 0
	curr = number
	for i in primes:
		curr = number / i

	# count, factor = 0, 1
	# if number % 2 != 0:
	# 	factor = 2

	# for i in range(1, (number / 2) + 1, factor):
	# 	if (number % i == 0):
	# 		count += 1
	# if number > 0:
	# 	count += 1
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

# hdtn(int(sys.argv[1]))
print numberDivisors(24)
# print isPrime(int(sys.argv[1]))