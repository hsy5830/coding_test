limit = 10001
prime = [True] * limit
prime[0], prime[1] = False, False

for i in range(limit):
    if prime[i]:
        for j in range(i + i, limit, i):
            prime[j] = False

T = int(input())
for i in range(T):
    n = int(input())
    for k in range(int(n//2+0.5), 1, -1):
        if prime[k] and prime[n-k]:
            print(k, n-k)
            break