'''
미로 탐색 : https://www.acmicpc.net/problem/2178

BFS 구현
'''
from collections import deque

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

def BFS(x, y):
    visited[x][y] = True

    queue = deque([(x, y, 1)])
    while len(queue):
        w, z, c = queue.popleft()
        if w+1 < N and z < M and maze[w+1][z] == '1' and visited[w+1][z] == False:
            queue.append((w+1, z, c+1))
            visited[w+1][z] = True
            if (w+1, z) == (N-1, M-1):
                print(c+1)
                break
        if w < N and z+1 < M and maze[w][z+1] == '1' and visited[w][z+1] == False:
            queue.append((w, z+1, c+1))
            visited[w][z+1] = True  
            if (w, z+1) == (N-1, M-1):
                print(c+1)
                break  
        if w > 0 and z > 0 and maze[w-1][z] == '1' and visited[w-1][z] == False:
            queue.append((w-1, z, c+1))
            visited[w-1][z] = True
            if (w-1, z) == (N-1, M-1):
                print(c+1)
                break
        if w > 0 and z > 0 and maze[w][z-1] == '1' and visited[w][z-1] == False:
            queue.append((w, z-1, c+1))
            visited[w][z-1] = True
            if (w, z-1) == (N-1, M-1):
                print(c+1)
                break


BFS(0, 0)
