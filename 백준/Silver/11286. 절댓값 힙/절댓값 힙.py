'''
절댓값 힙 : https://www.acmicpc.net/problem/11286
'''
import sys
# print = sys.stdout.write
input = sys.stdin.readline
import heapq

N = int(input())
heap = []

for i in range(N):
    x = int(input())
    if x != 0:
        if x>0: heapq.heappush(heap, (x, 1))
        else: heapq.heappush(heap, (-x, -1))
    else:
        if len(heap) == 0:
            print(0)
            continue

        r = heapq.heappop(heap)
        print(r[0] * r[1])
