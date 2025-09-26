# 문제 설명
# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

# 입출력 예
# n	    return
# 12	28
# 5	    6

n = 12


def solution(n):
    result = []
    result = [num for num in range(1, n + 1) if n % num == 0]
    return sum(result)


print(solution(n))
