'''
수 정렬하기 2 : https://www.acmicpc.net/problem/2751

'''
# ### 시간 초과 ###
# # tmp 만들고 -> 하나씩 다시 대입 이라서 그런듯?
# def merge(A, start, end):
#     # stop rule
#     if end - start < 1: return

#     # middle index
#     m = (start + end) // 2
    
#     # recursion
#     merge(A, start, m)
#     merge(A, m+1, end)

#     # merge sort
#     tmp = []
#     i1, i2 = start, m+1
#     while i1 <= m and i2 <= end:
#         if A[i1] < A[i2]:
#             tmp.append(A[i1])
#             i1 += 1
#         else:
#             tmp.append(A[i2])
#             i2 += 1
    
#     while i1 <= m:
#         tmp.append(A[i1])
#         i1 += 1

#     while i2 <= end:
#         tmp.append(A[i2])
#         i2 += 1

#     for i in range(len(tmp)): # 시간 초과 원인인듯
#         A[start+i] = tmp[i]

import sys
input = sys.stdin.readline

def merge(A):
    # print("start : ", A, start, end)
    # stop rule
    if len(A) <= 1: return A

    # mid point
    m = len(A)//2

    # recursion
    A_left = merge(A[:m])
    A_right = merge(A[m:])

    ## merge sort
    left, right, now = 0, 0, 0

    while left < len(A_left) and right < len(A_right):
        if A_left[left] < A_right[right]:
            A[now] = A_left[left]
            left += 1
            now += 1
        else:
            A[now] = A_right[right]
            right += 1
            now += 1
        
    # one side remains
    while left < len(A_left):
        A[now] = A_left[left]
        left += 1
        now += 1

    while right < len(A_right):
        A[now] = A_right[right]
        right += 1
        now += 1

    return A

    
##### main #####
N = int(input())
l = [int(input()) for _ in range(N)]

l = merge(l)

for n in l:
    print(n)