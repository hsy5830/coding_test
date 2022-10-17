'''
끝나는 시간을 오름차순으로 정렬
끝나는 시간에 맞춰서 greedy하게 추가하면 됨
'''

N = int(input())
session = [list(map(int, input().split())) for _ in range(N)]
session.sort(key = lambda x: (x[1], x[0]))


ans = [[0,0]]
for S, E in session:
    if ans[-1][1] > S: continue
    ans.append([S, E])

print(len(ans) - 1)