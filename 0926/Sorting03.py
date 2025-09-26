# 문제 설명
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.

# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.

# 입출력 예
# numbers	        return
# [6, 10, 2]	    "6210"
# [3, 30, 34, 5, 9]	"9534330"


from functools import cmp_to_key

# numbers = list(map(int, input().split()))
numbers = [6, 10, 2]


def compare(a: str, b: str) -> int:
    # a+b 가 b+a 보다 크면 a가 앞
    if a + b > b + a:
        return -1
    if a + b < b + a:
        return 1
    return 0


def solution(numbers):
    strs = list(map(str, numbers))
    strs.sort(key=cmp_to_key(compare))
    ans = "".join(strs)
    return "0" if ans[0] == "0" else ans


print(solution(numbers))
