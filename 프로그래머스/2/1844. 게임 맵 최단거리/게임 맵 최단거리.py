from collections import deque

def solution(maps):
    answer = 1
    n, m = len(maps), len(maps[0])
    
    # visited = [[0] * m for _ in range(n)]
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    queue = deque([(0,0)])
    
    while 1:
        is_moved = 0
        for i in range(len(queue)):
            x, y = queue.popleft()
            
            for j in range(4):
                new_x, new_y = x + dx[j], y + dy[j]
                if (new_x >= 0 and new_x <= n-1) and (new_y <= m-1 and new_y >=0) and maps[new_x][new_y]:
                    maps[new_x][new_y] = 0
                    queue.append((new_x, new_y))
                    is_moved = 1
        if is_moved:
            answer += 1
        
        if (n-1, m-1) in queue:
            return answer 
        elif len(queue) == 0:
            return -1
        

    return 0