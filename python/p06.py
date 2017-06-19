#Sum square difference

def sum_square(n):
	return sum([i**2 for i in range(1, n + 1)])

def square_sum(n):
	return sum(range(1, n + 1)) ** 2

def difference(n):
	return square_sum(n) - sum_square(n)

print difference(100)