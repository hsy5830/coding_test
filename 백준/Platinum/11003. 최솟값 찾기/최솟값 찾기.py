'''
최솟값 찾기 - https://www.acmicpc.net/problem/11003


'''
from collections import deque

N, L = map(int, input().split())
l = list(map(int, input().split()))

# 답지
window = deque()

for i in range(N):
    while window and window[-1][1] > l[i]:
        window.pop()
    
    window.append((i, l[i]))
    if i - window[0][0] >= L:
        window.popleft()

    print(window[0][1], end = ' ')

# # 내 풀이
# window = deque([(0, l[0])])
# result = [l[0]]

# for i in range(1, N):
    
#     while len(window) > 0:
#         if l[i] <= window[-1][1]:
#             window.pop()
#             if len(window) == 0:
#                 window.append((i, l[i]))
#                 break
#         else:
#             window.append((i, l[i]))
#             break

#     # 윈도우 길이 체크
#     if i - window[0][0] >= L:
#         window.popleft()

#     result.append(window[0][1])




# # ##### 내 방법 (실패) #####
# # m1, m2 = l[0], l[1]

# # # window size under L
# # for i in range(L):
# #     if l[i] < m1:
# #         result.append(l[i])
# #         m2 = m1
# #         m1 = l[i]
# #     else:
# #         if m1 < l[i] < m2:
# #             m2 = l[i]
# #         result.append(m1)

# # # window size == L
# # for i in range(L, N):
# #     s, e = i-L+1, i
# #     if m1 == l[s-1]:
# #         if m2 < l[s]:
# #             m1 = m2; m2 = l[s]
# #         else:
# #             m1 = l[s]
# #     if l[e] < m1:
# #         m1 = l[e]
# #     elif l[e] < m2:
# #         m2 = l[e]
# #     result.append(m1)

# # print
# for n in result:
#     print(n, end=" ")