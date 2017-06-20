# Project Euler
# Problem 14
# Longest Collatz sequence

def collatz_sequence_iterative(number):
	chain = 1

	while (number != 1):

		if number % 2 == 0:
			number /= 2
		else:
			number = number * 3 + 1

		chain += 1

	return chain


def longest_chain(max_number):
	largest = - float("inf")
	largestNumber = 0

	for i in range(1, max_number):
		curr = collatz_sequence_iterative(i)
		
		if curr > largest:
			largest = curr
			largestNumber = i

	return largestNumber

print longest_chain(10**6)