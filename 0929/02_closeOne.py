n, m = 5, 5
lst = [
    [1, 0, 1, 0, 2],
    [0, 0, 1, 2, 1],
    [0, 1, 0, 1, 2],
    [1, 1, 0, 2, 1],
    [2, 0, 1, 0, 2],
]

# 문제
# 2와 근접한 1의 개수 찾기


# 1단계 : 한글로 적기

# lst에 들어있는 전체 원소들에 대해서.
# 1의 개수를 찾고 싶다.
# 2와 근접한
# 2의 상하좌우에 1이 존재하면 개수를 세면 됨.
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count = 0
for x in range(n):
    for y in range(m):
        if lst[x][y] == 2:
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if lst[nx][ny] == 1:
                        count += 1
print(count)
# 1. 방문처리
# 2. 아예 없애버림(다른 값으로 덮어씌움)
# 0 : 의미없음 / 1, 2라는 의미있음.
count = 0
for x in range(n):
    for y in range(m):
        if lst[x][y] == 2:
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if lst[nx][ny] == 1:
                        count += 1
                        # 방문한곳을 다시 방문하지 않도록.
                        lst[nx][ny] = 0
print(count)


# 방문처리
# visited 라는 "방문 했음"을 처리하는 data(원본 사이즈와 같게.)
visited = [[0] * m for _ in range(n)]  # 0 : 방문안함 / 1 : 방문함.
lst = [
    [1, 0, 1, 0, 2],
    [0, 0, 1, 2, 1],
    [0, 1, 0, 1, 2],
    [1, 1, 0, 2, 1],
    [2, 0, 1, 0, 2],
]

count = 0
for x in range(n):
    for y in range(m):
        if lst[x][y] == 2:
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                # (그리드 안에 있거나) 또는 (방문하지 않았을 때) 확인.
                if (0 <= nx < n and 0 <= ny < m) and (visited[nx][ny] == 0):
                    if lst[nx][ny] == 1:
                        count += 1
                        # 방문한곳을 다시 방문하지 않도록.
                        visited[nx][ny] = 1
print(count)

# 방문처리
# visited 라는 "방문 했음"을 처리하는 data(원본 사이즈와 같게.)\
visited = set()  # set은 존재성을 나타내기 좋은 자료구조.
# 성능은 2차원 배열이 더 좋을 가능성이 높음.
# 단, set은 hashable만 들어갈 수 있어서 []리스트는 안되고, ()튜플만 가능하다.
lst = [
    [1, 0, 1, 0, 2],
    [0, 0, 1, 2, 1],
    [0, 1, 0, 1, 2],
    [1, 1, 0, 2, 1],
    [2, 0, 1, 0, 2],
]

count = 0
for x in range(n):
    for y in range(m):
        if lst[x][y] == 2:
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                # (그리드 안에 있거나) 또는 (방문하지 않았을 때) 확인.
                if (0 <= nx < n and 0 <= ny < m) and ((nx, ny) not in visited):
                    if lst[nx][ny] == 1:
                        count += 1
                        # 방문한곳을 다시 방문하지 않도록.
                        visited.add((nx, ny))
print(count)
