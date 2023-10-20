from collections import deque
def solution(n, computers):
    ans = 0
    visited = [0] * n
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            queue = deque([i])
            while queue:
                now = queue.pop()
                for j in range(n):
                    if computers[now][j] and not visited[j]:
                        visited[j] = 1
                        queue.append(j)
            
            ans += 1
    
    return ans