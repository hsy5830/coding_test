'''
최대공약수 : https://www.acmicpc.net/problem/1850
'''
def GCD(A, B): # A > B
    if B == 0:
        return A
    else:
        return GCD(B, A % B)

A, B = map(int, input().split())

G = GCD(B, A)

for _ in range(G):
    print(1, end = '')