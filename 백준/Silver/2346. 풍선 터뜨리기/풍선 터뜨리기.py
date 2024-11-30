from collections import deque

N = int(input())
l = list(map(int, input().split()))
ld = deque([(i+1, l[i]) for i in range(N)])

ans = []
while ld:
    idx, k = ld.popleft()
    ans.append(idx)
    # 음수 이동도 양수 기준 동일 보정
    if k > 0: 
        ld.rotate(-(k-1))
    else: 
        ld.rotate(-k)

print(*ans)
