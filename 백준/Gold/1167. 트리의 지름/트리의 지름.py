'''
트리의 지름 : https://www.acmicpc.net/problem/1167
'''
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

# tree 생성
tree = {i:deque([]) for i in range(1, N+1)}
for _ in range(N):
    l = list(map(int, input().split()))
    node = l[0]
    idx = 1
    while idx < len(l) - 1:
        n = l[idx]
        dist = l[idx+1]
        tree[node].append((n, dist))
        idx += 2


# distance (거리 정보)
random_start = 1
M, M_node = 0, random_start

queue = tree[random_start].copy() # already deque
visited = [False] * (N+1)
visited[random_start] = True

for n ,d in queue:
    if not visited[n]:
        visited[n] = True
        if M <= d:
            M = d
            M_node = n

while len(queue):
    now, dist = queue.popleft()
    
    next = tree[now]
    for n, d in next:
        if not visited[n]:
            queue.append((n, d + dist))
            visited[n] = True
            if M <= d + dist:
                M = d + dist
                M_node = n



queue = tree[M_node].copy() # already deque
visited = [False] * (N+1)
visited[M_node] = True

M2 = 0
for n ,d in queue:
    if not visited[n]:
        visited[n] = True
        if M2 <= d:
            M2 = d
            M_node = n
        

while len(queue):
    now, dist = queue.popleft()
    
    next = tree[now]
    for n, d in next:
        if not visited[n]:
            queue.append((n, d + dist))
            visited[n] = True
            if M2 <= d + dist:
                M2 = d + dist
                M_node = n

print(M2)