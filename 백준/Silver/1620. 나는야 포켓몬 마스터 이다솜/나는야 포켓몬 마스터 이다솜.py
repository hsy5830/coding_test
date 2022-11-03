N, M = map(int, input().split())
poke = [input() for _ in range(N)]
Q = [input() for _ in range(M)]
Q = [int(q) if q.isdigit() else q for q in Q]

poke_dict = {name:id for id, name in enumerate(poke)} # 나중에 id + 1 해줘야 함

for q in Q:
    if type(q) == type('s'):
        print(poke_dict[q]+1)
    else:
        print(poke[q-1])