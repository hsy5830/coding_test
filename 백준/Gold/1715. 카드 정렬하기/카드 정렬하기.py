'''
https://www.acmicpc.net/problem/1715

Gold : 카드 정렬하기
'''

import heapq

# ##### [1] #####
# N = int(input())
# l = sorted([int(input()) for _ in range(N)])

# if N == 1: print(0)
# else:
#     ans = 0
#     for _ in range(N-1):
#         tmp  = heapq.heappop(l) + heapq.heappop(l)
#         ans += tmp
#         heapq.heappush(l, tmp)
#     print(ans)


##### [2] #####
N = int(input())
cards = [int(input()) for _ in range(N)]

heapq.heapify(cards)

ans = 0
while len(cards) > 1:
    c1 = heapq.heappop(cards)
    c2 = heapq.heappop(cards)

    ans += (c1 + c2)
    heapq.heappush(cards, c1 + c2)

print(ans)