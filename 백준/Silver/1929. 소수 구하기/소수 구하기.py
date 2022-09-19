def is_prime(N):
    if N == 1: return False
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0: return False
    return True

a, b = map(int, input().split())
for num in range(a, b+1):
    if is_prime(num): print(num)