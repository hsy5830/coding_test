'''
ABCDE : https://www.acmicpc.net/problem/13023

DFS로 구현
'''
N, M = map(int, input().split())
friends = {p:[] for p in range(N)}
for _ in range(M):
    p1, p2 = map(int, input().split())
    friends[p1].append(p2)
    friends[p2].append(p1)

visited = [False] * N
exist = [0]

def DFS(v, depth):
    visited[v] = True
    depth += 1
    # print(visited, depth)
    if depth == 5:
        exist[0] = 1
        return
    
    # 원래는 인접한 노드를 다 접근하고 visited 체크한다. 하지만,
    # 여기선 한 줄기에 대한 DFS의 깊이를 찾아야하기 때문에 인접한 노드 한 개만 먼저 접근.
    # 1 -> 2, 3 일 때 DFS(1) 에서 2, 3을 visited 하지 않고, 2(or 3) 먼저 접근한다.
    # if len(friends[v]) != 0:
    #     p = friends[v].pop()
    #     if not visited[p]:
    #         DFS(p, depth)
    #         visited[p] = False

    # for p in friends[v]:
    #     if not visited[p]:
    #         DFS(p, depth)
    #         visited[p] = False

    for p in friends[v]:
        if not visited[p]:
            DFS(p, depth)
            visited[p] = False


# for i in range(N):
#     for j in friends[i]:
#         if not visited[j]:
#             DFS(i, 0)
#             visited[j] = False
#             if exist[0] == 1: break

for i in range(N):
    if not visited[i]:
        DFS(i, 0)
        visited[i] = False
        if exist[0] == 1: break


print(exist[0])