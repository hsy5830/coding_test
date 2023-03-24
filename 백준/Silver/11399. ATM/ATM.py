'''
ATM : https://www.acmicpc.net/problem/11399

그냥 오름차순 정렬하면 됨
'''

N = int(input())
l = list(map(int, input().split()))

for i in range(1,N):
    val, idx = l[i], i
    for j in range(i+1):
        if l[i] < l[j]:
            val = l[i]
            idx = j
            break

    for k in range(i, idx, -1):
        l[k] = l[k-1]
    l[idx] = val

time = 0
for i in range(N):
    time += l[i] * (N - i)
print(time)