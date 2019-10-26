import sys

num = int(sys.argv[1])

def isPrime(num):
	if num < 2:
		return False
	elif num > 1 and num < 4:
		return True
	elif num % 2 == 0:
		return False
	elif num % 2 != 0:
		res = True
		for n in range(3, num):
			if num % n == 0:
				res = False
		return res

output = isPrime(num)
print(f'{num} isPrime ? {output}')