# 문제 설명
# 1 x 1 크기의 칸들로 이루어진 직사각형 격자 형태의 미로에서 탈출하려고 합니다.
# 각 칸은 통로 또는 벽으로 구성되어 있으며, 벽으로 된 칸은 지나갈 수 없고
# 통로로 된 칸으로만 이동할 수 있습니다.
# 통로들 중 한 칸에는 미로를 빠져나가는 문이 있는데, 이 문은 레버를 당겨서만 열 수 있습니다.
# 레버 또한 통로들 중 한 칸에 있습니다.
# 따라서, 출발 지점에서 먼저 레버가 있는 칸으로 이동하여 레버를 당긴 후
# 미로를 빠져나가는 문이 있는 칸으로 이동하면 됩니다.
# 이때 아직 레버를 당기지 않았더라도 출구가 있는 칸을 지나갈 수 있습니다.
# 미로에서 한 칸을 이동하는데 1초가 걸린다고 할 때,
# 최대한 빠르게 미로를 빠져나가는데 걸리는 시간을 구하려 합니다.

# 미로를 나타낸 문자열 배열 maps가 매개변수로 주어질 때,
# 미로를 탈출하는데 필요한 최소 시간을 return 하는 solution 함수를 완성해주세요.
# 만약, 탈출할 수 없다면 -1을 return 해주세요.

# 입출력 예
# maps	                                        result
# ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]	    16
# ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]	    -1

# https://campus.programmers.co.kr/tryouts/196833/challenges

from collections import deque


def solution(maps):
    # 시작 / 도착 / 레버
    n = len(maps)
    m = len(maps[0])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                start = (i, j)
            elif maps[i][j] == "E":
                end = (i, j)
            elif maps[i][j] == "L":
                lever = (i, j)
    # 1. start -> lever로 이동.
    # 최단거리 -> queue를 써야겠다! (bfs)

    # s -> e로 가는 거리
    def bfs(s, e):
        queue = deque()
        # (x, y, distance)

        # 출발 distance가 0 : 한칸을 이동하는데 1이 걸리기 때문         / 다른 문제는 "몇칸 걸리니?" -> 기본값 1
        # queue.append((*s, 0))
        x, y = s
        queue.append((x, y, 0))

        visited = set()
        visited.add(s)

        while queue:
            x, y, distance = queue.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                #                         길을 갈수 있다 가 아니라 -> 길, 출구, 레버, 입구
                #                         벽을 갈 수 없다.-> 벽이 아닐때만 가겠다.
                if (
                    0 <= nx < n
                    and 0 <= ny < m
                    and maps[nx][ny] != "X"
                    and (nx, ny) not in visited
                ):
                    queue.append((nx, ny, distance + 1))
                    visited.add((nx, ny))

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


# start -> lever로 갈 때는 갔던 길을 또 가지 않아야 합니다.
# lever -> end로 갈때도 마찬가지로 갔던 길을 또 가지 않아야 합니다.
# 단, lever -> end로 갈 때 start -> lever로 이동할 때 지나쳤던 칸은 또 가도 됩니다.
# visited를 공유 or maps를 덮어씌운다 는 동작은 하면 안됩니다.


# 참고
# * : packing / unpacking
# 여러 개를 하나의 변수로 / 하나의 변수를 여러 개로
def func(*args):
    print(args)


func(1, 2, 3, 4, 5, 6, 7)
