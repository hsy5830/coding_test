'''
행렬 덧셈
'''

N, M = map(int, input().split())
mat1 = [list(map(int, input().split())) for _ in range(N)]
mat2 = [list(map(int, input().split())) for _ in range(N)]

mat = map(lambda x, y: list(map(lambda a, b: str(a+b), x, y)), mat1, mat2)

for e in mat:
    print(" ".join(e))
