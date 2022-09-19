def is_prime(n):
    if n == 1: return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        else:
             return True

N = int(input())
l = list(map(int, input().split()))

ans = 0
for num in l:
    if is_prime(num): ans += 1
print(ans)