from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    start_x, start_y = 0, 0
    distance = 1
    end_x, end_y = n - 1, m - 1

    q = deque()
    q.append((start_x, start_y, distance))

    visited = set()
    visited.add((start_x, start_y))

    while q:
        x, y, distance = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if (
                (0 <= nx < n and 0 <= ny < m)
                and (maps[nx][ny] == 1)
                and ((nx, ny) not in visited)
            ):
                q.append((nx, ny, distance + 1))
                visited.add((nx, ny))

                if (nx, ny) == (end_x, end_y):
                    return distance + 1
    return -1


print(
    solution(
        [
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 1],
        ]
    )
)
