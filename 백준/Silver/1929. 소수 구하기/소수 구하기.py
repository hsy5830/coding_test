'''
소수 구하기 : https://www.acmicpc.net/problem/1929
'''

M, N = map(int, input().split())

# [1] Sieve of Eratosthenes
primes = [True] * (N+1)
primes[1] = False

# for i in range(2, N):
for i in range(2, int(N**0.5) + 1): # 여기도 제곱근 까지만 수행
    for j in range(2*i, N+1, i):
        primes[j] = False

for prime in range(M, N+1):
    if primes[prime]:
        print(prime)

# # [2] 일반적인 소수 찾는 방법
# # range에 유의!
# def is_prime(N):
#     if N == 1: return False
#     for i in range(2, int(N**0.5) + 1):
#         if N % i == 0: return False
#     return True

# for num in range(M, N+1):
#     if is_prime(num): print(num)