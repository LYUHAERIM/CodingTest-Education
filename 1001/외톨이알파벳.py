# 문제 설명
# 알파벳 소문자로만 이루어진 어떤 문자열에서,
# 2회 이상 나타난 알파벳이 2개 이상의 부분으로 나뉘어 있으면 외톨이 알파벳이라고 정의합니다.

# 문자열 "edeaaabbccd"를 예시로 들어보면,

# a는 2회 이상 나타나지만, 하나의 덩어리로 뭉쳐있으므로 외톨이 알파벳이 아닙니다.
# "ede(aaa)bbccd"
# b, c도 a와 같은 이유로 외톨이 알파벳이 아닙니다.
# d는 2회 나타나면서, 2개의 부분으로 나뉘어 있으므로 외톨이 알파벳입니다.
# "e(d)eaaabbcc(d)"
# e도 d와 같은 이유로 외톨이 알파벳입니다.
# 문자열 "eeddee"를 예시로 들어보면,

# e는 4회 나타나면서, 2개의 부분으로 나뉘어 있으므로 외톨이 알파벳입니다.
# "(ee)dd(ee)"
# d는 2회 나타나지만, 하나의 덩어리로 뭉쳐있으므로 외톨이 알파벳이 아닙니다.
# "ee(dd)ee"
# 문자열 input_string이 주어졌을 때, 외톨이 알파벳들을 알파벳순으로 이어 붙인
# 문자열을 return 하도록 solution 함수를 완성해주세요.
# 만약, 외톨이 알파벳이 없다면 문자열 "N"을 return 합니다.

# 입출력 예
# input_string      result
# "edeaaabbccd"	    "de"
# "eeddee"	        "e"
# "string"	        "N"
# "zbzbz"	        "bz"


from collections import defaultdict


def solution(input_string: str) -> str:
    if not input_string:
        return "N"

    # 각 알파벳의 '덩어리(연속 구간)' 개수 세기
    seg = defaultdict(int)  # segments(덩어리·구간)
    prev = None
    for ch in input_string:
        if ch != prev:  # 새로운 구간이 시작될 때만 +
            seg[ch] += 1
            prev = ch
    print(seg)

    # 구간 수가 2 이상인 알파벳만 사전순으로 이어붙이기
    lonely = "".join(sorted(ch for ch, cnt in seg.items() if cnt >= 2))
    return lonely if lonely else "N"


print(solution("edeaaabbccd"))
