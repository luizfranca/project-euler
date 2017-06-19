# Summation of primes

# def primers(n):
# 	primers_list = [2]
# 	sum_numbers = 2
# 	number = 2
# 	while number < n:
# 		number += 1

# 		for i in primers_list:
# 			if number % i == 0:
# 				break
# 		else:
# 			primers_list.append(number)
# 			sum_numbers += number
	
# 	return sum_numbers - number

import math

def isPrime(n):
	if n == 1:
		return False
	elif n < 4:
		return True #2 and 3 are prime
	elif n % 2 == 0:
		return False
	elif n < 9:
		return True #we have already excluded 4,6 and 8.
	elif n % 3 == 0:
		return False
	else:
		r = int(math.sqrt(n)) # n rounded to the greatest integer r so that r*r<=n
		f = 5
		while f <= r:
			if n % f == 0:
				return False #(and step out of the function)
			if n % (f + 2) == 0:
				return False #(and step out of the function)

			f += 6

		return True #(in all other cases)

def primers(limit):
	sum_primers = 5 #// we know that 2 and 3 are prime
	n = 5
	while n <= limit:
		if isPrime(n):
			sum_primers += n

		n += 2

		if n <= limit and isPrime(n):
			sum_primers += n

		n += 4
		
	return sum_primers
print isPrime(531)
print primers(2000000)




# 142913828922