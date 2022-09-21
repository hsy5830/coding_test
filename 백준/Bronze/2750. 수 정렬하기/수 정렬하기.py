N = int(input())
arr = [int(input()) for _ in range(N)]

# 선택 정렬
for i in range(N):
    idx = i; m = arr[i]
    for j in range(i,N):
        if arr[j] < m:
            idx = j; m = arr[j]
    if idx > i:
        arr[idx], arr[i] = arr[i], arr[idx]

for n in arr:
    print(n)