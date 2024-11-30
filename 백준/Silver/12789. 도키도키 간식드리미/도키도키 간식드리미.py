from collections import deque

N = int(input())
students = deque(list(map(int, input().split())))
stack = [1001]

prev = 0
while students:
    if students[0] < stack[-1]:
        next = students.popleft()
        if next == prev + 1: prev = next
        else: stack.append(next)
    else:
        if stack[-1] == prev + 1:
            prev = stack.pop()
        else: break

while len(stack) > 1:
    if stack[-1] != prev + 1: break
    prev += 1
    stack.pop()

if stack[-1] == 1001: print('Nice')
else: print('Sad')
