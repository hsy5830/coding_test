'''
버블 소트 : https://www.acmicpc.net/problem/1377
'''
import sys
input = sys.stdin.readline

N = int(input())
l = [(int(input()), i) for i in range(N)] # (숫자, 처음 index)
l.sort() # sort() 함수는 O(n*logn)

moved = []
for i in range(N):
    moved.append(l[i][1] - i)

M = max(moved)

print(M+1)