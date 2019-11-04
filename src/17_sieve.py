# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

# from codingame.com
def sieve(num: int) -> list:
	primes = 2*[False] + (num-1)*[True]
	# more effecient to max out at sqrt of num
	sqr = int(num**0.5+1.5)
	for i in range(2, sqr):
		if primes[i]:
			for j in range(i*i, num+1, i):
				primes[j] = False
	return [n for n, isPrime in enumerate(primes) if isPrime]

# # myImplementation based on wikipedia pseudocode
# def sieve(num):
# 	# find all prime integers <= num
# 	# offset range to account for 0 index
# 	lst = [True for n in range(0, num+1)]
# 	lst[0] = False # 0 is not prime
# 	lst[1] = False # 1 is not prime
# 	for num, _ in enumerate(lst, start=0):
# 		if lst[num] == True:
# 			sq = num*num
# 			if sq >= len(lst): break
# 			else:
# 				lst[sq] = False
# 				max = len(lst)
# 				i = 1
# 				j = num
# 				while i < max:
# 					target = sq+(i*j)
# 					if target >= len(lst): break 
# 					lst[target] = False
# 					i += 1
# 	# return a list containing only prime numbers <= num
# 	result = [n for n, isPrime in enumerate(lst, start=0) if isPrime == True]
# 	return result
