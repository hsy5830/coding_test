'''
https://www.acmicpc.net/problem/2468

Silver : 안전 영역
'''

'''
check : true or false list
ans = 0

while sum(check) > 1:
    BFS로 바꾸고
    끝나면 ans += 1

return ans
'''

### Function
from collections import deque
def bfs(arr, x, y):
    q = deque([[x, y]])
    N = len(arr)

    while q:
        ix, iy = q.popleft()
        arr[ix][iy] = 0 # F

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1] 
        for i in range(4):
            nx, ny = ix + dx[i], iy + dy[i]
            if 0<= nx < N and 0 <= ny < N and arr[nx][ny]:    # 순서 바뀌면 안됨
                q.append([nx, ny])
                arr[nx][ny] = 0 # F

    return arr
        


### Main
N = int(input())
area = [ list(map(int, input().split())) for _ in range(N) ]
ans_l = []

# 0 ~ maximum rain - 1
for k in range(max(map(max, area))):
    check = [[0 if area[i][j] <= k else 1 for i in range(N)] for j in range(N)] # 강수량 미만의 지역 0, 안전영역 1
    ans = 0
    for i in range(N):
        for j in range(N):
            if check[i][j]:
                check = bfs(check, i, j)
                ans += 1
    ans_l.append(ans)

if len(ans_l) == 0: ans_l = [1]
print(max(ans_l))
