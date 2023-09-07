import sys
input = sys.stdin.readline

M, N = map(int, input().split())
S = list(map(int, input().split()))
# sum_S = S
# for i in range(1, len(S)):
#     sum_S[i] += sum_S[i-1]
# sum_S = [0] + sum_S

# for _ in range(N):
#     a, b = map(int, input().split())
#     print(sum_S[b] - sum_S[a-1])


for i in range(1, len(S)):
    S[i] += S[i-1]
S = [0] + S

for _ in range(N):
    a, b = map(int, input().split())
    print(S[b] - S[a-1])