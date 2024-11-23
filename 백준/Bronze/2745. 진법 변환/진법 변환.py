D = {}
for i in range(26):
    D[chr(65+i)] = i+10
for i in range(10):
    D[f"{i}"] = i

N, B = input().split()
B = int(B)

ans = 0
for i in range(len(N)-1, -1, -1):
    ans += D[N[i]] * (B**(len(N)-1-i))

print(ans)