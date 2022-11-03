def decomp(N):
    s = sum(map(int, list(str(N))))
    return s + N

N = int(input())
for i in range(1, N):
    if decomp(i) == N:
        print(i)
        break
else:
    print(0)