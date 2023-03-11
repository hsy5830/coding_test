'''
주몽


'''

N = int(input())
M = int(input())
materials = list(map(int, input().split()))
set_materials = set(materials)

materials_minus_M = [M - n for n in materials]

count = 0
for k in materials_minus_M:
    if k in set_materials: count += 1

print(count//2)