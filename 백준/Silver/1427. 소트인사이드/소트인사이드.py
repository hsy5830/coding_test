'''
소트인사이드 : https://www.acmicpc.net/problem/1427

'''

N = input()
l = list(N)

answer = ''
for i in range(len(N)):
    M, idx = l[i], i
    for j in range(i, len(N)):
        if l[j] > l[idx]:
            M = l[j]
            idx = j
    tmp = l[i]
    l[i] = M
    l[idx] = tmp

for n in l:
    print(n, end='')