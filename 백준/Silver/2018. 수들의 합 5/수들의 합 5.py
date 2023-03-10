'''
수들의 합 5 : https://www.acmicpc.net/problem/2018

N = kc + (1 + 2 + ... + k-1)
'''

N = int(input())

count = 0
for k in range(1, N+1):
    r = k*(k-1)//2
    if r > N: break
    # if (N-r) % k == 0: count += 1
    if (N-r) // k >= 1 and (N-r) % k == 0:
        count += 1

print(count)