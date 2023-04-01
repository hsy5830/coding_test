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
    # 방문하면 visited, depth 업데이트
    visited[v] = True
    depth += 1
    
    # 만약 depth == 5 가 되면 끝. 종료
    if depth == 5:
        exist[0] = 1
        return

    # p를 시작점으로 탐색한 뒤, 다시 p를 False로 돌려놓는다
    # 다른 시작점에서 p를 방문할 수 있도록 하기 위함
    # 1 -> 0 -> 3 방문하다가 끊겼다면, 3, 0, 1 순서로 다시 visited[p] = False가 적용될 것.
    for p in friends[v]:
        if not visited[p]:
            DFS(p, depth)
            visited[p] = False

    visited[v] = False # DFS에서 시작점에 대해 False로 초기화해주진 않는다. (1)

# 모든 시작점에서 탐색하기
for i in range(N):
    if not visited[i]:
        DFS(i, 0)
        # visited[i] = False # DFS에서 시작점에 대해 False로 초기화해주진 않는다. (2)
        if exist[0] == 1: break

## (1) or (2) 둘 중 하나는 해줘야 함

print(exist[0])