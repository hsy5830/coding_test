from collections import deque

def solution(number, k):
    answer = ''
    stack = deque([])
    
    throw = 0
    for i in range(len(number)):
        now = number[i]
        while stack and throw < k and stack[-1] < now:
            stack.pop()
            throw += 1
        
        stack.append(now)
    
    if throw < k:
        stack = deque(list(stack)[:-k+throw])
    
    return ''.join(stack)