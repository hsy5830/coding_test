a, b = int(input()), int(input())
if a == 1: a = 2
l = []

for num in range(a, b+1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        l.append(num)

if len(l) == 0:
    print(-1)
else:
    print(sum(l))
    print(min(l))