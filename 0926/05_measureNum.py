# 문제 설명
# 두 정수 left와 right가 매개변수로 주어집니다.
# left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고,
# 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

# 입출력 예
# left  right	result
# 13	17	    43
# 24	27	    52

left = 13
right = 17


def solution(left: int, right: int) -> int:
    total = 0
    for x in range(left, right + 1):
        r = int(x**0.5)
        if r * r == x:  # 완전제곱수 → 약수 개수 홀수 → 뺀다
            total -= x
        else:  # 그 외 → 약수 개수 짝수 → 더한다
            total += x
    return total


print(solution(left, right))
