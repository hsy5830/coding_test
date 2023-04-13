def solution(people, limit):
    people.sort() # 사람들의 몸무게를 오름차순으로 정렬
    i, j = 0, len(people) - 1 # 가장 가벼운 사람과 가장 무거운 사람의 인덱스를 지정
    count = 0 # 필요한 구명보트의 개수를 저장할 변수
    while i <= j:
        if people[i] + people[j] <= limit: # 가장 가벼운 사람과 가장 무거운 사람이 함께 탈 수 있는 경우
            i += 1 # 가장 가벼운 사람의 인덱스를 증가시키고
            j -= 1 # 가장 무거운 사람의 인덱스를 감소시킴
        else: # 함께 탈 수 없는 경우
            j -= 1 # 가장 무거운 사람만 구명보트를 타고 떠남
        count += 1 # 구명보트의 수를 증가시킴
    return count # 필요한 구명보트의 수를 반환
