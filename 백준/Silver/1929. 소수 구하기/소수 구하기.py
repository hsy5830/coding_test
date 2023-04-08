'''
소수 구하기 : https://www.acmicpc.net/problem/1929
'''

M, N = map(int, input().split())

# Sieve of Eratosthenes
primes = [True] * (N+1)
primes[1] = False

for i in range(2, N):
    for j in range(2*i, N+1, i):
        primes[j] = False

for prime in range(M, N+1):
    if primes[prime]:
        print(prime)