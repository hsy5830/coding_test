'''
잃어버린 괄호 : https://www.acmicpc.net/problem/1541
'''
s = input()
numbers = []
opers = []

tmp = ''
for i in range(len(s)):
    if s[i].isdigit():
        tmp += s[i]
    else:
        numbers.append(int(tmp))
        tmp = ''
        opers.append(s[i])
numbers.append(int(tmp))

if '-' not in opers:
    print(sum(numbers))
else:
    idx = opers.index('-')
    print(sum(numbers[:idx+1]) - sum(numbers[idx+1:]))

