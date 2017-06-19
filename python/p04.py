# Largest palindrome product
def isPalindrome(number):
	number = str(number)
	lenght = len(number)
	if lenght % 2 == 0 and number[:lenght / 2] == number[:(lenght / 2) - 1:-1]:
		return True
	elif number[:lenght / 2] == number[:(lenght / 2): -1]:
		return True
	return False

def problem(number):
	numberRange = range((number - 1) * 10, int(number * "9") + 1)
	palindromes = []
	for i in numberRange:
		for j in numberRange:
			if isPalindrome(i * j):
				palindromes.append(i * j)
	print max(palindromes)

problem(3)