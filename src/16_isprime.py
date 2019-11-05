import sys
from decorators import timer

@timer
def sieve(num: int) -> list:
	primes = 2*[False] + (num-1)*[True]
	sqr = int(num**0.5+1.5) # max out at sqrt of num
	for i in range(2, sqr):
		if primes[i]:
			for j in range(i*i, num+1, i):
				primes[j] = False
	return [n for n, isPrime in enumerate(primes) if isPrime]

num = int(sys.argv[1])
if num < 1: sys.exit('ERROR: input must be integer > 0')

sifted = sieve(num)
if num in sifted:
	isPrime = True
else: 
	isPrime = False
print(f'{num} isPrime ? {isPrime}')

# # myNaive implementation
# @timer
# def isPrime(num):
# 	if num < 2:
# 		return False
# 	elif num > 1 and num < 4:
# 		return True
# 	elif num % 2 == 0:
# 		return False
# 	elif num % 2 != 0:
# 		res = True
# 		for n in range(3, num):
# 			if num % n == 0:
# 				res = False
# 		return res

# output = isPrime(num)
# print(f'{num} isPrime ? {output}')
