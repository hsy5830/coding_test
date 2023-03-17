'''
스택 수열 : https://www.acmicpc.net/problem/1874


'''

N = int(input())
l = [int(input()) for _ in range(N)] + [-100]

target_idx = 0
target = l[target_idx]
stack = [0]
action = []

for i in range(1, N+1):
    
    while stack[-1] == target:
        stack.pop()
        action.append('-')
        target_idx += 1
        target = l[target_idx]

    stack.append(i)
    action.append('+')

while len(stack) > 1:
    if stack.pop() != target:
        action.append('NO')
        break
    else:
        target_idx += 1
        target = l[target_idx]
        action.append('-')

if action[-1] == 'NO':
    print('NO')
else:
    for act in action:
        print(act)