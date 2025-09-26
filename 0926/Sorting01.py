# 문제 설명
# 문자열 before와 after가 매개변수로 주어질 때,
# before의 순서를 바꾸어 after를 만들 수 있으면 1을,
# 만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.

# 입출력 예
# before	after	result
# "olleh"	"hello"	1
# "allpe"	"apple"	0

# before, after = map(str, input().split())

before = "olleh"
after = "hello"


def solution(before: str, after: str) -> int:
    return 1 if sorted(before) == sorted(after) else 0


print(solution(before, after))
