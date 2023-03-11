'''
DNA 비밀번호 : https://www.acmicpc.net/problem/12891


'''
# import sys
# input = sys.stdin.readline

N, P = map(int, input().split())
DNA = input()
c = list(map(int, input().split()))
condition = {'A':c[0], 'C':c[1], 'G':c[2], 'T':c[3]}
count_DNA = {'A':0, 'C':0, 'G':0, 'T':0}

s, e = 0, P-1
part = DNA[s:e]
for r in part:
    count_DNA[r] += 1

count = 0
while e < N:
    count_DNA[DNA[e]] += 1
    
    if count_DNA['A'] >= condition['A'] and count_DNA['C'] >= condition['C'] and count_DNA['G'] >= condition['G'] and count_DNA['T'] >= condition['T']:
        count += 1

    count_DNA[DNA[s]] -= 1

    s += 1
    e += 1
    
print(count)