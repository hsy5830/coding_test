from collections import deque

# 입력 처리
N = int(input())
queuestack = map(int, input().split())  # 0: queue, 1: stack
data = list(map(int, input().split()))

# queuestack에서 0인 인덱스의 data 값만 deq에 추가
deq = deque(data[i] for i, q in enumerate(queuestack) if q == 0)

# 다음 입력: 추가할 값
_ = input()  # 빈 줄 무시
C = map(int, input().split())

# deque에 값을 추가하고 출력
for c in C:
    deq.appendleft(c)
    print(deq.pop(), end=' ')