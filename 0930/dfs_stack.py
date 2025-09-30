# 1은 길 / 0은 벽.
# 우리는 1로만 갈 수 있고, 왼쪽 위 -> 오른쪽 아래로 이동할 수 있니?

# n, m = map(int,input().split())
# mat = [list(map(int,input().split())) for _ in range(n)]
# 4 6
# 1 0 1 1 1 1
# 1 1 1 0 1 0
# 1 0 1 0 1 1
# 1 1 1 0 1 1


from collections import deque

n, m = 4, 6
# 성공 mat
mat = [[1, 0, 1, 1, 1, 1], [1, 1, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]

# 실패 mat
# mat = [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 1, 1, 0, 0, 1]]

# 왼쪽 위에서 출발해서 모든 점들을 방문하며 오른쪽 아래로 이동하겠어.

# 1에서 출발해.
# 1에서 갈 수 있는 점 중 하나만 방문.
# 해당 점에서 다시 갈 수 있는 점 중 하나만 방문
# 더이상 갈 수 없으면 해당 점 pop
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

stack = deque()
start_x, start_y = 0, 0
end_x, end_y = n - 1, m - 1

stack.append((start_x, start_y))
visited = [[0] * m for _ in range(n)]
while stack:
    # stack의 가장 마지막 값을 '사용'하는 것이지, 삭제하는 것이 아님.
    x, y = stack[-1]
    visited[x][y] = 1

    if (x, y) == (end_x, end_y):
        print(True)
        break

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if (
            (0 <= nx < n and 0 <= ny < m)
            and (mat[nx][ny] == 1)
            and (visited[nx][ny] == 0)
        ):
            stack.append((nx, ny))
            # bfs 같은 경우에는 모든 nx, ny를 한번에 queue에 넣습니다
            # dfs 같은 경우에는 하나의 nx, ny만 stack에 넣습니다.
            break
    else:
        stack.pop()
