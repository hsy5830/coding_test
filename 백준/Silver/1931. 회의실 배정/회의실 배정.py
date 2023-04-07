from collections import deque

N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]

meetings.sort(key = lambda x: (x[1], x[0]))
meetings = deque(meetings)

ans = deque([meetings.popleft()])
while len(meetings):
    s, e = meetings.popleft()
    if ans[-1][1] > e:
        ans.pop()
        ans.append((s,e))
    elif ans[-1][1] <= s:
        ans.append((s,e))

print(len(ans))