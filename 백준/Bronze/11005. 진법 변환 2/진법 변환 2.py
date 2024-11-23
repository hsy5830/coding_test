s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = map(int, input().split())
ans = ''

while n:
    ans += s[n%b]
    n //= b

print(ans[::-1])