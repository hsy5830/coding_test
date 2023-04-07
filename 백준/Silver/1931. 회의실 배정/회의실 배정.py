'''
끝나는 시간을 오름차순으로 정렬
끝나는 시간에 맞춰서 greedy하게 추가하면 됨
'''

# input / (끝나는 시간, 시작 시간) 순서로 오름차순 정렬
N = int(input())
session = [list(map(int, input().split())) for _ in range(N)]
# session.sort(key = lambda x: x[1]) # 이렇게 하면 [3, 3] 같은 애들이 여러 개 있을 때 포함되지 않을 수 있음
session.sort(key = lambda x: (x[1], x[0])) # [3, 3] [2, 3] 순서로 있을 때 는 [2, 3]이 적용되지 않음

## 같은 결과를 갖는 정렬법
# room.sort(key = lambda x: x[0]) 
# room.sort(key = lambda x: x[1])

# ### 리스트 append
# # [0, 0] 에서 부터 시작,
# ans = [[0,0]]
# for S, E in session:
#     if ans[-1][1] > S: continue  # 새로운 회의가 열리려면, 시작 시간의 이전 회의의 끝나는 시간과 크거나 같아야 함
#     ans.append([S, E])

# # [0, 0]을 제외한 회의 수 print
# print(len(ans) - 1)

### 더 빠르게
count = 0
end = -1
for i in range(N):
    S, E = session[i]
    if S >= end: # 새로운 회의가 열리려면, 시작 시간의 이전 회의의 끝나는 시간과 크거나 같아야 함
        end = E
        count += 1

print(count)


# ##### 틀린 풀이 #####
# from collections import deque

# N = int(input())
# meetings = [tuple(map(int, input().split())) for _ in range(N)]

# meetings.sort(key = lambda x: (x[1], x[0]))
# meetings = deque(meetings)

# print(meetings)

# ans = deque([meetings.popleft()])
# while len(meetings):
#     s, e = meetings.popleft()
#     if ans[-1][1] > e:
#         ans.pop()
#         ans.append((s,e))
#     elif ans[-1][1] <= s:
#         ans.append((s,e))

# print(len(ans))