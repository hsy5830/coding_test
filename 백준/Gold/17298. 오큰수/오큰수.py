'''
오큰수 : https://www.acmicpc.net/problem/17298


'''
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
stack = []
answer = [-1] * N

for i in range(N): # i : push 대상 인덱스
    while len(stack) > 0 and A[i] > A[stack[-1]]: # top 보다 크면 pop하고 오큰수 answer에 업데이트
        j = stack.pop()
        answer[j] = A[i]
    stack.append(i)

for ans in answer:
    print(ans, end = ' ')  