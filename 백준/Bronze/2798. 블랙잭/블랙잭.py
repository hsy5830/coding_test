from itertools import combinations
N, M = map(int, input().split())
l = list(map(int, input().split()))

Max = 0
for s in combinations(l, 3):
    score = sum(s)
    if score > Max and score <= M: Max = score
        
print(Max)