'''
주몽

(내 풀이)
고유 번호를 n 이라고 할 때, M-n이 재료 중에 있어야 갑옷 하나를 만들 수 있다.
    materials의 번호들을 M에서 뺀 새로운 리스트 만들고
    새로운 리스트의 번호가 materials에 있다면 갑옷을 만들 수 있는 것

(투 포인터)
1. materials 오름차순 정렬
2. 좌우 끝에서 부터 좁혀가며 찾는다
    O(N) -> O(N/2)

'''

N = int(input())
M = int(input())
materials = list(map(int, input().split()))

# # 내 방법
# set_materials = set(materials)

# materials_minus_M = [M - n for n in materials]

# count = 0
# for k in materials_minus_M:
#     if k in set_materials: count += 1

# print(count//2)


# 투 포인터
materials.sort()

count = 0
s, e = 0, N-1
while s < e:
    added = materials[s] + materials[e]
    if added > M:
        e -= 1
    elif added < M:
        s += 1
    else:
        s += 1
        e -= 1
        count += 1

print(count)