'''
수 찾기 : https://www.acmicpc.net/problem/1920

재귀로 이진탐색 시,
    def binary_search(A, target, left, right) 
로 많이 구현하는 듯
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())
l = list(map(int, input().split()))

M = int(input())
targets = list(map(int, input().split()))

def bin_sc(A, target): # A : 정렬된 리스트
    # stop condition
    if len(A) == 0:
        return 0

    # binary search
    S, E = 0, len(A)-1
    mid = (S + E) // 2

    if A[mid] == target: return 1
    elif A[mid] > target:
        return bin_sc(A[:mid], target)
    else:
        return bin_sc(A[mid+1:], target)
    
def binary_search(A, target, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2
    if A[mid] == target: return 1
    elif A[mid] > target:
        return binary_search(A, target, start, mid-1)
    else:
        return binary_search(A, target, mid+1, end)
    

l.sort()
for i in targets:
    # print(bin_sc(l, i))
    print(binary_search(l, i, 0, N-1))