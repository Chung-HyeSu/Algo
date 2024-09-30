from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    def make_board():
        board = [[0] * 102 for _ in range(102)]
        for x1, y1, x2, y2 in rectangle:
            for i in range(2*x1, 2*x2+1):
                for j in range(2*y1, 2*y2+1):
                    board[i][j] = 1
        for x1, y1, x2, y2 in rectangle:
            for i in range(2*x1+1, 2*x2):
                for j in range(2*y1+1, 2*y2):
                    board[i][j] = 0
        return board

    def bfs(board, start_x, start_y, end_x, end_y):
        queue = deque([(start_x, start_y, 0)])
        visited = [[False] * 102 for _ in range(102)]
        visited[start_x][start_y] = True
        
        while queue:
            x, y, dist = queue.popleft()
            if x == end_x and y == end_y:
                return dist // 2
            
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 102 and 0 <= ny < 102 and board[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx, ny, dist + 1))
                    visited[nx][ny] = True
        
        return -1

    board = make_board()
    return bfs(board, 2*characterX, 2*characterY, 2*itemX, 2*itemY)