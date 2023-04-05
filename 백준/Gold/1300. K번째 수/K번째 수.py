'''
K번째 수 : https://www.acmicpc.net/problem/1300
'''

N = int(input())
k = int(input())
# A = [[i*j for i in range(1, N+1)] for j in range(1, N+1)] # 필요없네;;

start, end = 1, k
while start <= end:
    count = 0
    mid = (start + end) // 2

    # mid 보다 같거나 작은 것의 개수 세기
    for i in range(1, N+1):
        if mid//i == 0: break
        count += min(mid // i, N)

    # 이진 탐색 조건
    if count < k:
        start = mid + 1
    else:
        end = mid - 1

print(start)