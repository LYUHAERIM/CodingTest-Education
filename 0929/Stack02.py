# 문제 설명
# 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

# "()()" 또는 "(())()" 는 올바른 괄호입니다.
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

# 입출력 예
# s	        nswer
# "()()"	true
# "(())()"	true
# ")()("	false
# "(()("	false


def solution1(s):
    stack = []
    for ch in s:
        if ch == "(":
            stack.append(ch)
        else:  # ch == ')'
            if not stack:  # 닫는 괄호가 나왔는데 앞에 열린 게 없음
                return False
            stack.pop()  # 짝 맞음 → 하나 제거
    return len(stack) == 0  # 모두 짝지었으면 True, 남아있으면 False


def solution2(s):
    bal = 0
    for ch in s:
        if ch == "(":
            bal += 1
        else:  # ch == ')'
            bal -= 1
            if bal < 0:  # 닫는 괄호가 더 많아짐 → 즉시 실패
                return False
    return bal == 0  # 0이면 정확히 짝 맞음
