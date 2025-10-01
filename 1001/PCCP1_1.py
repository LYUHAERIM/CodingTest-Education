from collections import defaultdict
def solution(input_string):
    # 외톨이 알파벳을 알파벳순으로 이어붙여서 return해라.
    # 없으면 'N' 리턴해라

    # => 외톨이 알파벳을 구한다.
    # => sort해라.

    # => 외톨이? 
    # 소문자로만 이루어진 어떤 문자열에서, 
    # 2회 이상 나타난 알파벳이 
    # 2개 이상의 부분으로 나뉘어 있으면 외톨이 알파벳이라고 정의합니다.

    # => 알파벳의 개수를 구해라! 단, 알파벳이 연속으로 존재하면 1개로 칩니다.
    # 즉, 우리는 문자열에서 알파벳의 덩어리의 개수를 구한다.
    # -> 그것의 개수가 2개 이상인지를 확인.
    
    # 알파벳 덩어리의 개수
    counter = defaultdict(int)

    before = ''
    for char in input_string:
        # aaaa와 같이 연속된 것은 1번만 세야 한다.
        # 이전값과 비교해서 같으면 세지 않는다.
        if before == char:
            continue # 다음 반복으로 넘어가자.
        counter[char] += 1
        before = char

    # answer = []
    # for key, value in counter.items():
    #     if value > 1:
    #         answer.append(key)
    answer = [key for key, value in counter.items() if value > 1]

    if answer:
        answer.sort()
        answer = "".join(answer)
    else:
        answer = 'N'
    return answer