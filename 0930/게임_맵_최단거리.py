from collections import deque


# 기본적인 dfs만 구현
def solution(maps):
    # start -> end까지 가는데 얼마나 걸리니?
    # bfs를 써서 해보자!
    n = len(maps)
    m = len(maps[0])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    start_x, start_y = 0, 0
    end_x, end_y = n - 1, m - 1

    queue = deque()
    queue.append((start_x, start_y))

    visited = set()
    visited.add((start_x, start_y))

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if (
                0 <= nx < n
                and 0 <= ny < m
                and maps[nx][ny] == 1
                and (nx, ny) not in visited
            ):
                queue.append((nx, ny))
                visited.add((nx, ny))
                if (nx, ny) == (end_x, end_y):
                    # 도착!
                    pass

    answer = 0
    return answer


from collections import deque


# 좌표에 거리를 넣고 다니자
def solution(maps):
    # start -> end까지 가는데 얼마나 걸리니?
    # bfs를 써서 해보자!
    n = len(maps)
    m = len(maps[0])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    start_x, start_y = 0, 0
    end_x, end_y = n - 1, m - 1

    queue = deque()
    #              x 좌표  / y좌표   / 거리 : 기본값 : 1 / 칸의 개수를 세는 것.
    queue.append((start_x, start_y, 1))

    visited = set()
    visited.add((start_x, start_y))

    while queue:
        x, y, distance = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if (
                0 <= nx < n
                and 0 <= ny < m
                and maps[nx][ny] == 1
                and (nx, ny) not in visited
            ):
                queue.append((nx, ny, distance + 1))
                visited.add((nx, ny))
                if (nx, ny) == (end_x, end_y):
                    # 도착!
                    return distance + 1
                    pass
    # 도착 실패!
    return -1


# visited 배열에 거리를 함께 넣는다.
def solution(maps):

    n = len(maps)
    m = len(maps[0])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    start_x, start_y = 0, 0
    end_x, end_y = n - 1, m - 1

    queue = deque()
    queue.append((start_x, start_y))

    visited = [[0] * m for _ in range(n)]
    visited[start_x][start_y] = 1

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if (
                0 <= nx < n
                and 0 <= ny < m
                and maps[nx][ny] == 1
                and visited[nx][ny] == 0
            ):
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                if (nx, ny) == (end_x, end_y):
                    # 도착!
                    return visited[nx][ny]

    return -1


# dfs를 하면 queue에 다음과 같이 자료가 들어가게 된다.
# 원점으로부터의 거리가 (0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3) 스럽게 들어간다.
# 즉, 우리는 거리 0 따로 / 거리 1 따로 / 거리 2 따로 묶어서 생각할 수 있다.


def solution(maps):
    # start -> end까지 가는데 얼마나 걸리니?
    # bfs를 써서 해보자!
    n = len(maps)
    m = len(maps[0])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    start_x, start_y = 0, 0
    end_x, end_y = n - 1, m - 1

    queue = deque()
    queue.append((start_x, start_y))

    visited = set()
    visited.add((start_x, start_y))

    distance = 1

    # 전체에 대해서.
    while queue:
        # 지금 queue에는 같은 거리를 가지고 있는 값들만 들어있습니다.
        count = len(queue)  # 같은 거리를 가지고 있는 값들의 개수.
        distance += 1
        # count번 popleft해버림.
        for _ in range(count):
            x, y = queue.popleft()

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if (
                    0 <= nx < n
                    and 0 <= ny < m
                    and maps[nx][ny] == 1
                    and (nx, ny) not in visited
                ):
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    if (nx, ny) == (end_x, end_y):
                        return distance

    return -1


# visited 배열에 거리를 함께 넣는다.
def solution(maps):

    n = len(maps)
    m = len(maps[0])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    start_x, start_y = 0, 0
    end_x, end_y = n - 1, m - 1

    queue = deque()
    queue.append((start_x, start_y))

    flag = 100
    # maps[start_x][start_y] = 거리
    maps[start_x][start_y] = flag + 1  # 마지막 정답에서 flag를 빼줌.

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 이미 방문한 곳은 maps가 flag보다 큰 값으로 덮어씌워졌기 때문에 maps가 1인 부분만 안간게 맞다.
            if (
                0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1
            ):  # and visited[nx][ny] == 0:
                queue.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1
                if (nx, ny) == (end_x, end_y):
                    # 도착!
                    return maps[nx][ny] - flag

    return -1
