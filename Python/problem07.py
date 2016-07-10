#10001st prime

def primers(n):
	primers_List = [2]
	number = 3
	while True:
		for i in primers_List:
			if number % i == 0:
				break
		else:
			primers_List.append(number)

		if len(primers_List) == n:
			return primers_List[-1]
			
		number += 1

print primers(10001)
