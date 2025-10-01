from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                start = (i, j)
            if maps[i][j] == "E":
                end = (i, j)
            if maps[i][j] == "L":
                lever = (i, j)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def bfs(s, e):
        #print("s", s)
        q = deque()

        x, y = s
        distance = 0

        q.append((x, y, distance))

        visited = set()
        visited.add((x, y, distance))

        while q:
            x, y, distance = q.popleft()
            #print(x, y)
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if (
                    (0 <= nx < n and 0 <= ny < m)
                    and (maps[nx][ny] != "X")
                    and (nx, ny) not in visited
                ):
                    q.append((nx, ny, distance + 1))
                    visited.add((nx, ny))
                    #print(q)
                    if (nx, ny) == e:
                        return distance + 1
        return -1

    start_to_lever = bfs(start, lever)
    if start_to_lever == -1:
        return -1
    lever_to_end = bfs(lever, end)
    if lever_to_end == -1:
        return -1

    return start_to_lever + lever_to_end


print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))
