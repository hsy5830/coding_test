id = [int(input()) for _ in range(28)]
id = set(id)
classes = set(list(range(1,31)))

print(min(classes-id))
print(max(classes-id))