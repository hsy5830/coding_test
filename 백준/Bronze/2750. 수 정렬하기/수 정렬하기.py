N = int(input())
arr = [int(input()) for _ in range(N)]

# 버블정렬
for i in range(N-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

for n in arr:
    print(n)