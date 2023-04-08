'''
소수 & 팰린드롬 : https://www.acmicpc.net/problem/1747
'''

def is_pelindrome(s : str):
    return s == s[::-1]

N = int(input())
prime = [True] * 1005000

# 소수 구하기
prime[1] = False
for i in range(2, int(len(prime) ** 0.5)):
    if not prime[i]: # 소수가 아니면 이후 숫자 확인할 필요 없음
        continue
    for j in range(i + i, len(prime), i):
        prime[j] = False

# 펠린드롬
for i in range(N, len(prime)):
    if prime[i]:    
        s = str(i)
        if is_pelindrome(s):
            print(s)
            break