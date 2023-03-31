'''
수 정렬하기 3 : https://www.acmicpc.net/problem/10989

책에서 radix 정렬 문제로 소개 -> counting sort
'''
import sys
input = sys.stdin.readline

N = int(input())
# l = [int(input()) for _ in range(N)] # 이렇게 하면 메모리초과!

### counting sort
count_list = [0] * (10001) # index == 답 으로 하기 위해 1개 더 추가

# for number in l:
#     count_list[number] += 1

for i in range(N):
    count_list[int(input())] += 1

for i in range(len(count_list)):
    for _ in range(count_list[i]):
        print(i)