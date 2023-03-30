'''
버블 소트 : https://www.acmicpc.net/problem/1517

버블 정렬 시 swap 횟수 계산
'''
import sys
input = sys.stdin.readline


def merge(A, count):
    # stop rule
    if len(A) <= 1:
        return A, 0

    # mid point
    m = len(A)//2

    # recursion
    A_left, c_l = merge(A[:m], count)
    A_right, c_r = merge(A[m:], count)

    # merge sort
    left, right, now = 0, 0, 0
    c0 = 0
    while left < len(A_left) and right < len(A_right):
        if A_left[left] <= A_right[right]:
            A[now] = A_left[left]
            left += 1
            now += 1
        else:
            c0 += (right + len(A_left) - now) # A_right 에서 먼저 뽑히는 것들은 왼쪽으로 이동한 것!
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

    return A, c_l + c_r + c0


##### main #####
N = int(input())
l = list(map(int, input().split()))

l, count = merge(l, 0)
print(count)