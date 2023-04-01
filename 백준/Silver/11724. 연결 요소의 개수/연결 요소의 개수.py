'''
연결 요소의 개수 : https://www.acmicpc.net/problem/11724

DFS로 구현
'''
from collections import deque

def DFS(graph, visited, start):
    if visited[start - 1] == 1: return

    # stack에 start node 삽입
    stack = [start]
    visited[start - 1] = 1

    # # 인접노드 visted
    # while len(stack) >= 1:
    #     node = stack.pop()
    #     while len(graph[node]) != 0:
    #         next = graph[node].pop()
    #         if visited[next - 1] == 0:
    #             stack.append(next)
    #             visited[next - 1] = 1

    # 인접노드 visted
    while len(stack) >= 1:
        node = stack.pop()
        for next in graph[node]:
            if visited[next-1] == 0:
                stack.append(next)
                visited[next - 1] = 1
        
    return graph, visited

##### main #####
N, M = map(int, input().split())

# 연결 리스트 구현 with Dictionary
graph = {i:deque([]) for i in range(1, N+1)}
for i in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# DFS
visited = deque([0] * N)

count = 0
for i in range(1, N+1):
    if not visited[i-1]:
        count += 1
        graph, visited = DFS(graph, visited, i)

print(count)