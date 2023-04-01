'''
신기한 소수 : https://www.acmicpc.net/problem/2023

DFS로 구현

에라토스테네스의 체? -> 시간초과
'''
def is_prime(n):
    if n == 1: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def DFS(n):
    if len(str(n)) == N:
        print(n)
    else:
        for k in [1,3,5,7,9]:
            if is_prime(10*n + k):
                DFS(10*n + k)

N = int(input())

for num in [2,3,5,7]:
    DFS(num)

