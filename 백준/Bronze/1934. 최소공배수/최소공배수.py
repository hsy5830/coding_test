'''
최소공배수 : https://www.acmicpc.net/problem/1934
'''

def GCM(A, B):
    M, N = max(A, B), min(A, B)
    while M % N != 0:
        M = M % N
        M, N = max(M, N), min(M, N)
    
    return N

N = int(input())

for _ in range(N):
    A, B = map(int, input().split())
    G = GCM(A, B)
    print(G * (A // G) * (B // G))
