'''
구간합 구하기 lv.2
행렬에서

matrix 만들 때 (ex 3x3)
    1. [[0] * 3] * 3
        이렇게 만들면 3개 행의 [0, 0, 0] 들이 각각 다른 주소를 갖는 3개의 리스트가 아니라
        같은 포인터를 갖는 리스트이다.
        하나의 리스트를 3개로 복사해라! 라는 느낌인 듯
    
    2. [[0] * 3 for _ in range(3)]
        이런식으로 만들면 [0, 0, 0]을 3번 생성하기 때문에 각기 다른 포인터를 갖는 서로 다른 리스트
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mat = [ list(map(int, input().split())) for _ in range(N)]

### 잘못된 풀이
### sum_mat을 아래와 같이 (0,0) 부터 (i,j) 순서대로 더한 것으로 구성하면
### 풀어야하는 문제에는 맞지 않는 합 행렬임
# s = 0
# sum_mat = []
# for i in range(N):
#     l = []
#     for j in range(N):
#         s += mat[i][j]
#         l.append(s)
#     sum_mat.append(l)

sum_mat = [[0] * (N+1) for _ in range(N+1)]
for i in range(1,N+1):
    s = 0
    for j in range(1, N+1):
        s += mat[i-1][j-1]
        sum_mat[i][j] += sum_mat[i-1][j]
        sum_mat[i][j] += s

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(sum_mat[x2][y2] - sum_mat[x1-1][y2] - sum_mat[x2][y1-1] + sum_mat[x1-1][y1-1])