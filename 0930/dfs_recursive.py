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

visited = [[0] * m for _ in range(n)]


# while stack:
# x, y -> nx, ny로 한발자국 나아가는 함수.
def dfs(x, y):
    # x, y = stack[-1]
    visited[x][y] = 1

    if (x, y) == (end_x, end_y):
        print(True)
        return

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if (
            (0 <= nx < n and 0 <= ny < m)
            and (mat[nx][ny] == 1)
            and (visited[nx][ny] == 0)
        ):
            # stack.append((nx, ny))
            dfs(nx, ny)
            # break
    # else:
    #     stack.pop()
    # return
