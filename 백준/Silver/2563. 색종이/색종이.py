'''
색종이 (100 x 100)

한변 10 정사각형
3 7 -> 왼쪽아래의 좌표
'''

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
area = [[0 for _ in range(100)] for _ in range(100)]

for i in range(len(paper)):
    left, bottom = paper[i]
    for l in range(10):
        for b in range(10):
            if left+l < 100 and bottom+b < 100:
                area[left+l][bottom+b] = 1
            else:
                break

ans = sum(list(map(lambda x: sum(x), area)))
print(ans)
