'''
수 묶기 : https://www.acmicpc.net/problem/1744

>1 : 큰 것 부터 2개씩 곱해서 더해준다
    하나 남으면? 그냥 더해줌
1 : 1은 그냥 더해주는게 최대값 만드는 방법
0 : 0은 음수가 1개 남았을 때 없애는 용도
<0 : 작은 것 부터(절대값이 큰 것 부터) 2개씩 곱해서 더해준다
    하나남으면?
        0이 있다면 0
        없다면 그냥 더해

위 규칙대로 구현하면 된다.
'''
from collections import deque

N = int(input())
l = deque(sorted([int(input()) for _ in range(N)]))

# >1, 1, 0, 0> : 네 파트로 나누기
# 내림차순으로 들어감
morethanone = deque([])
one = 0
zero = 0
negative = deque([])
while len(l):
    v = l.pop()
    if v > 1:
        morethanone.append(v)
    elif v == 1:
        one += 1
    elif v == 0:
        zero += 1
    else:
        negative.append(v)

# 정답 구하기
ans = 0
# [1]
while len(morethanone) > 1:
    ans += (morethanone.popleft() * morethanone.popleft())
if len(morethanone) == 1:
    ans += morethanone.popleft()

# [2]
ans += one

# [3]
while len(negative) > 1:
    ans += (negative.pop() * negative.pop())

if len(negative) == 1:
    # [4]
    if zero == 0:
        ans += negative.popleft()

print(ans)