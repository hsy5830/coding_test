'''
제곱 ㄴㄴ수 : https://www.acmicpc.net/problem/1016
'''

m, M = map(int, input().split())
# nono = [True] * (M+1) # 이렇게 시작하면 메모리 초과
nono = [i for i in range(m, M+1)]

for i in range(2, M+1):
    if i > M / i: break
    k = max(int((m / i) // i), 1)
    while k * i <= M / i:
        if k * i >= m / i:
            nono[k * i * i - m] = 0
        k += 1

print(sum([True if i != 0 else False for i in nono]))