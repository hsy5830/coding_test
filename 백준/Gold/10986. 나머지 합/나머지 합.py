'''
나머지 합

합배열 구한 뒤 (i, j) 돌아가며 구하기엔 10^6 C 2 의 경우가 있어 시간초과

'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
l = map(int, input().split())
count = 0

sum_list = []
s = 0
for num in l:
    s += num
    sum_list.append(s)

### 시간초과
# for i in range(0, N):
#     for j in range(i+1, N+1):
#         if (sum_list[j] - sum_list[i]) % M == 0: count += 1

dividedM = [num % M for num in sum_list]
remainders = [0] * M
for r in dividedM:
    remainders[r] += 1

count += remainders[0]
for i in range(M):
    n = remainders[i]
    if n < 2: continue
    count += (n * (n-1)) // 2

print(count)