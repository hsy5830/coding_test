'''
칵테일 : https://www.acmicpc.net/problem/1033
'''
def GCD(a, b): # a > b
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

def DFS(v):
    visited[v] = True
    
    for node in nodes[v]:
        b, p, q = node
        if not visited[b]:
            ans[b] = ans[v] * q // p
            DFS(b)


##### main #####
N = int(input())
nodes = {i:[] for i in range(N)}

lcm = 1
for _ in range(N-1):
    a, b, p, q = map(int, input().split())
    nodes[a].append((b, p, q)) # a : b = p : q
    nodes[b].append((a, q, p)) # b : a = q : p

    # 최소공배수 구하기
    lcm *= (p * q // GCD(p, q))

visited = [False] * N
LCM = [1] * N

ans = [lcm] * N
for i in range(N):
    DFS(i)
gcd = lcm

for i in range(1, N):
    gcd = GCD(gcd, ans[i])

for i in range(N):
    print(int(ans[i] // gcd), end = ' ')