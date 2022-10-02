import heapq

N = int(input())
l = sorted([int(input()) for _ in range(N)])

if N == 1: print(0)
else:
    ans = 0
    for _ in range(N-1):
        tmp  = heapq.heappop(l) + heapq.heappop(l)
        ans += tmp
        heapq.heappush(l, tmp)
    print(ans)