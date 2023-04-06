'''
동전 0 : https://www.acmicpc.net/problem/11047
'''

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

price = 0
count = 0
for i in range(N-1, -1, -1):
    coin = coins[i]
    if K - price >= coin:
        count += ((K - price) // coin)
        price += coin * ((K - price) // coin)
        

print(count)