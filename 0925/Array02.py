# 문제 설명
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

# 입출력 예
# n	    return
# 12345	[5,4,3,2,1]

# n = int(input())
n = 12345


def solution(n):
    result = []
    while n > 0:
        result.append(n % 10)
        n //= 10
    return result


# def solution(n):
#     result = [int(ch) for ch in str(n)][::-1]
#     result = list(map(int, str(n)[::-1]))
#     return result

print(solution(n))
