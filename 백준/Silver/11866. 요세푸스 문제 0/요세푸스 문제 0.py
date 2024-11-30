from collections import deque

def josephus(N, K):
    # 1부터 N까지 사람 번호를 리스트로 생성
    people = list(range(1, N + 1))
    result = []
    index = 0  # 현재 제거할 사람의 인덱스

    while people:
        # 다음 제거할 사람의 인덱스를 계산
        index = (index + K - 1) % len(people)
        # 해당 사람을 결과에 추가하고 리스트에서 제거
        result.append(people.pop(index))

    return result

# 예시 실행
N, K = map(int, input().split())

print('<', end='')
print(*josephus(N, K), end = '', sep = ', ')
print('>')