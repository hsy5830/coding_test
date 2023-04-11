'''
GCD(n, k) = 1 : https://www.acmicpc.net/problem/11689

'''

N = int(input())
result = N

# # 내 방법 -> 시간 초과
# k = 2
# while k <= N:
#     if result % k == 0: # 소수
#         N = N - N // k
#         while result % k == 0:
#             result /= k
#     k += 1

for p in range(2, int(N**0.5) + 1):
    if N % p == 0: # 소인수(소수) 확인
        result -= result / p # 오일러 피
        while N % p == 0:
            N /= p

if N > 1: # 누락된 소수 (root N 보다 큰 소인수)
    result -= result / N

print(int(result))