'''
카드2 : https://www.acmicpc.net/problem/2164


'''
from collections import deque

N = int(input())
cards = deque([i+1 for i in range(N)])

while len(cards) > 1:
    cards.popleft()
    tmp = cards.popleft()
    cards.append(tmp)

print(cards[0])