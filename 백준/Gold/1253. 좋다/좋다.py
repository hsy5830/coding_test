'''
좋다 - https://www.acmicpc.net/problem/1253


'''
N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

now = numbers[-1]
now_idx = N-1

count = 0
while now_idx >= 0:
    s, e = 0, N-1
    while s < e:
        if s == now_idx:
            s += 1
            continue
        elif e == now_idx:
            e -= 1
            continue

        num_sum = numbers[s] + numbers[e]
        if num_sum > now:
            e -= 1
        elif num_sum < now:
            s += 1
        else:
            count += 1
            break
    now_idx -= 1
    now = numbers[now_idx]

print(count)
