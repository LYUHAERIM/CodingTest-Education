#         1
#        / \
#       2   3
#      / \   \
#     4   5   8
#    / \  /
#   7    6
#
# BFS: [1, 2, 3, 4, 5, 8, 7, 6]


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
# 1에서 갈 수 있는 점들을 다 방문할 예정이야 => 기록해.
# 1은 끝났으니, (1에서 갈 수 있는 점)에서 다시 출발해

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

start_x, start_y = 0, 0
end_x, end_y = n - 1, m - 1

queue = deque()
queue.append((start_x, start_y))

visited = [[0] * m for _ in range(n)]
visited[start_x][start_y] = 1

answer = False


# queue에 원소가 존재할 때 반복해라.
def bfs():
    while queue:
        # queue에서 점을 pop하고, 그 점에서 출발하는 다른 점을 append
        x, y = queue.popleft()
        print(x, y)
        # visited[x][y] = 1 # 방문처리를 여기서 하게 되면, 중복 방문이 발생할 수 있다
        for d in range(4):
            # x, y로 부터 갈 수 있는 점들을 확인해야 함.
            nx = x + dx[d]
            ny = y + dy[d]

            # 그리드 안에 있고 / 1인 점 : 갈 수 있는 점    / visited하지 않은 점
            if (
                (0 <= nx < n and 0 <= ny < m)
                and (mat[nx][ny] == 1)
                and (visited[nx][ny] == 0)
            ):
                # 내가 (미래에) 방문할 곳.
                queue.append((nx, ny))
                visited[nx][ny] = 1  # 방문처리는 요기서!

                if (nx, ny) == (end_x, end_y):
                    # 성공!
                    return True
    return False


answer = bfs()
print(answer)
