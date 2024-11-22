l = []
while 1:
    try:
        l.append(input())
    except:
        break

print(*l, sep = '\n')