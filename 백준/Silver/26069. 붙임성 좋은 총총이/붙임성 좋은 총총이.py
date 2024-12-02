import sys
input = sys.stdin.readline

N = int(input())
dance = set(['ChongChong'])

for _ in range(N):
    A, B = input().split()
    if A in dance or B in dance:
        dance.update([A, B])

print(len((dance)))