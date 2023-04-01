'''
연결 요소의 개수 : https://www.acmicpc.net/problem/11724

DFS로 구현
'''
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M = map(int, input().split())

# 연결 리스트 구현 with Dictionary
graph = {i:[] for i in range(1, N+1)}
for i in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# visited 초기화
visited = [0] * N

# DFS 함수
def DFS(v): # 입력으론 1,2,...,N
    visited[v-1] = 1
    for node in graph[v]:
        if visited[node - 1] == 0: # visited가 모두 1이라면 재귀 종료
            DFS(node)

### main
count = 0
for i in range(1, N+1):
    if visited[i-1] == 0:
        count += 1
        DFS(i)

print(count)




# ############################## 비재귀 방식 ##############################
# def DFS(graph, visited, start):
#     if visited[start - 1] == 1: return

#     # stack에 start node 삽입
#     stack = [start]
#     visited[start - 1] = 1

#     # 인접노드 visted
#     while len(stack) >= 1:
#         node = stack.pop()
#         for next in graph[node]:
#             if visited[next-1] == 0:
#                 stack.append(next)
#                 visited[next - 1] = 1
        
#     return graph, visited

# ##### main #####
# N, M = map(int, input().split())

# # 연결 리스트 구현 with Dictionary
# graph = {i:deque([]) for i in range(1, N+1)}
# for i in range(M):
#     n1, n2 = map(int, input().split())
#     graph[n1].append(n2)
#     graph[n2].append(n1)

# # DFS
# visited = deque([0] * N)

# count = 0
# for i in range(1, N+1):
#     if not visited[i-1]:
#         count += 1
#         graph, visited = DFS(graph, visited, i)

# print(count)