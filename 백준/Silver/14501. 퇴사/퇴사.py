N = int(input())

# input
T, P = [], []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t); P.append(p)


# i + t_i 일 부터 마지막 날까지 
# i일의 일을 한다고 할 때 / 안할 때 를 비교하여 큰 값을 업데이트
money = [0 for _ in range(N+1)]
for i in range(N):
    for j in range(i + T[i], N+1):
        if money[j] < money[i] + P[i]:    # i일의 일을 (안할 때 < 할 때)
            money[j] = money[i] + P[i]

# 퇴사일의 금액 리턴
print(money[-1])