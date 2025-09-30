# 문제 설명
# n개의 음이 아닌 정수들이 있습니다.
# 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때
# 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

# 입출력 예
# numbers	        target	return
# [1, 1, 1, 1, 1]	3	    5
# [4, 1, 2, 1]	4	2

# https://campus.programmers.co.kr/tryouts/196832/challenges


def solution(numbers, target):
    n = len(numbers)

    def dfs(i, cur):
        # i번째까지 고려했을 때 합이 cur인 경우의 수
        if i == n:
            return 1 if cur == target else 0
        # i번째 수를 + 또는 -로 선택
        return dfs(i + 1, cur + numbers[i]) + dfs(i + 1, cur - numbers[i])

    return dfs(0, 0)


def solution(numbers, target):
    count = 0

    # 지금까지는 x, y가 필요햇지만,
    # 이제는 index만 필요합니다.
    def dfs(i, value):
        # global count
        # 이 함수 scope 바로 밖에 있는 변수에 접근 가능.
        nonlocal count

        # 원래의 dfs에서는 basecase, 즉 멈추는 조건이 존재하지 않음
        # -> if 조건부로 함수가 실행되기 때문.
        if i == len(numbers):
            # 끝까지 닿은 것.
            if value == target:
                count += 1
            return

        # 다음 부분 방문
        # for d in range(): 이 아래로 대체됨
        # for k in [-1, 1]:
        #     dfs(i+1, value + k * numbers[i])
        dfs(i + 1, value + numbers[i])
        dfs(i + 1, value - numbers[i])

    dfs(0, 0)
    return count


# count를 아예 밖에 두고
count = 0


def solution(numbers, target):

    def dfs(i, value):
        # 밖에 있는 count 사용
        global count

        if i == len(numbers):
            if value == target:
                count += 1
            return

        dfs(i + 1, value + numbers[i])
        dfs(i + 1, value - numbers[i])

    dfs(0, 0)
    return count


# '개발'로써는 정석적인 방법 -> global, nonlocal을 개발할 때 쓰면 어디서 에러가 나는지 확인하기 너무 힘듦.
# 단, 알고리즘 풀때는 재귀함수를 이쁘게 만들기 힘듦. -> 그냥 global 쓰자.
# 프로그래머스의 경우에는 solution함수로 묶여 있기 때문에 nonlocal의 존재도 알면 좋다.
def solution(numbers, target):

    # 너는 target이랑 같은 '개수'를 return하는 녀석이야.
    def dfs(i, value):

        if i == len(numbers):
            if value == target:
                return 1

            return 0

        x = dfs(i + 1, value + numbers[i])
        y = dfs(i + 1, value - numbers[i])
        return x + y

    result = dfs(0, 0)
    return result
