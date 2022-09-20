limit = 123456
prime = [True] * (2 * limit + 1)
prime[0:2] = [False, False]

for i in range(2, int(len(prime)**0.5)+1):
    if prime[i]:
        for j in range(2*i, len(prime), i):
            prime[j] = False

N = int(input())
while N != 0:
    print(sum(prime[N+1:2*N+1]))
    N = int(input())