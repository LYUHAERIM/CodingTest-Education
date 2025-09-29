from pprint import pprint
# 1  2  3  4
# 12 13 14 5
# 11 16 15 6
# 10 9  8  7
n = 5

# 이렇게 생긴 n짜리 list를 만드시오.

# 직접 만들어보니까, 빈 그리드가 필요함.
snail = [[0]*n for _ in range(n)]

# 숫자를 키우면서 한방향으로 이동함.
# 방향? 이동? -> delta 이동

# 한방향으로 이동하다가 특정 순간에 방향을 바꿈
# d 를 바꾸면 되겠구나!

# 방향이 시계방향으로 순서대로 이동 -> dx, dy를 만들때 조심!
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d = 0
x, y = 0, 0
for num in range(1, n*n + 1):
    snail[x][y] = num

    # x, y를 이동!
    # x = x + dx[d]
    # y = y + dy[d]

    # 이동을 지금하는게 아니라, 방향을 바꿀지 정하자!
    # nx, ny 즉 next_dot은 dot이 갈 수 있는 곳들의 후보.
    nx = x + dx[d]
    ny = y + dy[d]

    # (0,5)를 만남. 즉 grid에서 벗어나면 안됨!
        # 방향을 바꿔줘야 함!

    # 그리드에서 벗어나면                또는 이미 값이 있을 때
    if 0>nx or n<=nx or 0>ny or n<=ny or snail[nx][ny]!=0:
        # 방향을 바꿔줘!
        d = (d+1)%4
        nx = x + dx[d]
        ny = y + dy[d]
    
    # 진짜 이동
    x = nx
    y = ny
    print(x, y)
    # 디버거를 사용해도 괜찮지만,
    pprint(snail)
    print()