'''
잃어버린 괄호 : https://www.acmicpc.net/problem/1541
'''

# ## [1]
# s = input()
# numbers = []
# opers = []

# tmp = ''
# for i in range(len(s)):
#     if s[i].isdigit():
#         tmp += s[i]
#     else:
#         numbers.append(int(tmp))
#         tmp = ''
#         opers.append(s[i])
# numbers.append(int(tmp))

# if '-' not in opers:
#     print(sum(numbers))
# else:
#     idx = opers.index('-')
#     print(sum(numbers[:idx+1]) - sum(numbers[idx+1:]))


## [2]
A = list(map(str, input().split('-')))

ans = sum(list(map(int, A[0].split('+'))))
for i in range(1, len(A)):
    ans -= sum(list(map(int, A[i].split('+'))))

print(ans)
