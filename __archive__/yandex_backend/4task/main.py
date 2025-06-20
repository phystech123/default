import sys
from collections import deque

def main():
    n, m, d = map(int, sys.stdin.readline().split())
    grid = []
    for _ in range(n):
        grid.append(sys.stdin.readline().strip())
    
    # Инициализация матрицы расстояний
    dist = [[-1] * m for _ in range(n)]
    q = deque()
    
    # Заполнение очереди начальными точками (все 'X')
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'X':
                dist[i][j] = 0
                q.append((i, j))
    
    # Направления для BFS (вверх, вниз, влево, вправо)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS для заполнения матрицы расстояний
    while q:
        i, j = q.popleft()
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and dist[ni][nj] == -1:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))
    
    # Функция проверки наличия квадрата k x k с минимумом >= d
    def is_possible(k):
        if k == 0:
            return any(dist[i][j] >= d for i in range(n) for j in range(m))
        if k > min(n, m):
            return False
        
        # Проверка горизонтальных окон
        row_min = []
        for i in range(n):
            current_row = []
            dq = deque()
            for j in range(m):
                # Удаляем элементы вне текущего окна
                while dq and dq[0] < j - k + 1:
                    dq.popleft()
                # Удаляем элементы, которые больше текущего
                while dq and dist[i][dq[-1]] >= dist[i][j]:
                    dq.pop()
                dq.append(j)
                if j >= k - 1:
                    current_row.append(dist[i][dq[0]])
            row_min.append(current_row)
        
        # Проверка вертикальных окон
        for j in range(len(row_min[0])):
            dq = deque()
            for i in range(n):
                # Удаляем элементы вне текущего окна
                while dq and dq[0] < i - k + 1:
                    dq.popleft()
                # Удаляем элементы, которые больше текущего
                while dq and (row_min[dq[-1]][j] >= row_min[i][j] if dq else False):
                    dq.pop()
                dq.append(i)
                if i >= k - 1:
                    min_val = row_min[dq[0]][j]
                    if min_val >= d:
                        return True
        return False
    
    # Бинарный поиск максимального k
    low = 1
    high = min(n, m)
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if is_possible(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    
    print(ans)

if __name__ == "__main__":
    main()