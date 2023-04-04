'''
기타 레슨 : https://www.acmicpc.net/problem/2343
'''

def can_record(lectures, playtime_limit, num_cd):
    count = 1
    now = 0 # 현재 cd 시간
    for time in lectures:
        if now + time > playtime_limit: # 새 cd
            now = 0
            count += 1
            if count > num_cd: return False
        now += time
    if count <= num_cd:
        return True


N, M = map(int, input().split())
lec = list(map(int, input().split()))

# 블루레이 하나의 크기 기준으로 binary search
start, end = max(lec), sum(lec) # index가 아니라 시간!!
while start <= end:
    playtime = (start + end) // 2
    if not can_record(lec, playtime, M):
        start = playtime + 1
    else:
        end = playtime - 1

print(start)