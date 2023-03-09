import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

sum_list = [0]
s = 0
for i in numbers:
    s += i
    sum_list.append(s)

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_list[j] - sum_list[i-1])