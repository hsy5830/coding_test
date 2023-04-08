'''
거의 소수 : https://www.acmicpc.net/problem/1456

A ~ B**0.5 까지의 소수 구해놓고,
'''

A, B = map(int, input().split())

# [1] Sieve of Eratosthenes
lim = max(A, int(B**0.5))
lim = int(B**0.5)
# primes = [True] * (lim + 1) # 1, 2, ..., 루트B
primes = [True] * 10000001 # 1, 2, ..., 루트B
primes[1] = False

for i in range(2, lim + 1): # 여기도 제곱근 까지만 수행
    if primes[i] == False:
        continue
    for j in range(2*i, lim + 1, i):
        primes[j] = False


count = 0
for prime in range(2, lim + 1):
    # # 이렇게하면 prime ** order가 너무 커져서 에러 발생
    # order = 2
    # if primes[prime]:
    #     while prime ** order <= B:
    #         if A <= prime ** order:
    #             count += 1
#             order += 1

    # # 얘도 마찬가지
    # if primes[prime]:
    #     now = prime
    #     while now * prime <= B:
    #         if A <= now * prime:
    #             count += 1
#             now *= prime

    # 조건식을 나누기로 바꿔주면 큰 숫자까지 도달하지 않는다.
    if primes[prime]:
        now = prime
        while prime <= B / now:
            if A / now <= prime:
                count += 1
            now *= prime

print(count)