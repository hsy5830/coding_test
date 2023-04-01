'''
DFS와 BFS : https://www.acmicpc.net/problem/1260

'''
from collections import deque

N, M, V = map(int, input().split())

# # 이렇게하면 작은 노드부터 방문하는데 문제가 생기는 거 같음
# # 3 7 / 4 3 -> 3 : [7, 4] 가 들어가게 된다.
# l = [tuple(map(int, input().split())) for _ in range(M)]
# l.sort(key = lambda x: (x[1], x[0]))

graph = {i:[] for i in range(1, N+1)}
for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for node in list(graph.keys()):
    graph[node].sort()

# DFS
visited_dfs = [False] * (N+1)
ans_dfs = []
def DFS(V):
    visited_dfs[V] = True
    ans_dfs.append(V)
    for node in graph[V]:
        if not visited_dfs[node]:
            DFS(node)

# BFS
visited_bfs = [False] * (N+1)
ans_bfs = []
def BFS(V):
    # V 방문 표시
    visited_bfs[V] = True
    ans_bfs.append(V)

    queue = deque([V])
    while len(queue):
        now = queue.popleft()
        # now에 인접한 노드 차례대로 방문
        for n in graph[now]:
            if not visited_bfs[n]:
                queue.append(n)
                visited_bfs[n] = True
                ans_bfs.append(n)


##### main ####
DFS(V)
for node in ans_dfs:
    print(node, end=' ')

print()

BFS(V)
for node in ans_bfs:
    print(node, end=' ')