import sys
from sieve import sieve

num = int(sys.argv[1])
if num < 1: sys.exit('ERROR: input must be integer > 0')

sifted = sieve(num)
# print('16_isprime sifted',sifted)

if num in sifted:
	isPrime = True
else: isPrime = False
print(f'{num} isPrime ? {isPrime}')


# myNaive implementation
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
