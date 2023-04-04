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


## 아래 두 과정을 BFS(v) 함수로 만들어서 좀 더 간단히 만들 수 있을 듯
## 책에 있는 distance 리스트도 필요없다!

# BFS 1 - random node 기준
random_start = 1
M, M_node = 1, random_start

queue = deque([(random_start, 0)]) # already deque
visited = [False] * (N+1)
visited[random_start] = True

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


# BFS 2 - MAX node 기준
queue = deque([(M_node, 0)]) # already deque
visited = [False] * (N+1)
visited[M_node] = True

M2 = 1
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