N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

given = set(nums) & set(cards) # 가지고 있는 카드 집합

ans = [1 if num in given else 0 for num in nums]
ans = list(map(str, ans))
print(" ".join(ans))