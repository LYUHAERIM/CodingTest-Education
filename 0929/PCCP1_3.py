# 문제 설명
# 멘델은 완두콩을 이용하여 7년간 실험한 결과, 다음과 같은 특별한 법칙을 발견하였습니다.

# 둥근 완두 순종(RR)을 자가 수분, 즉 같은 유전자끼리 교배할 경우, 다음 세대에 둥근 완두 순종 형질만 나타난다.
# 주름진 완두 순종(rr)을 자가 수분할 경우, 다음 세대에 주름진 완두 순종 형질만 나타난다.
# 두 순종을 교배한 잡종(Rr)을 자가 수분할 경우, 다음 세대의 형질은 RR:Rr:rr=1:2:1의 비율로 나타난다.

# 멘델의 법칙을 공부한 진송이는, 직접 완두콩의 자가 수분 실험을 진행했습니다.
# 진송이의 실험에서 완두콩 한 개를 자가 수분한 결과는 다음과 같습니다.

# 1. 각 완두콩은 자가 수분해서 정확히 4개의 완두콩 후손을 남긴다.
# 2. 잡종 완두콩(Rr)은 자가 수분해서 첫째는 RR, 둘째와 셋째는 Rr, 넷째는 rr 형질의 후손을 남긴다.
# 3. 순종 완두콩(RR, rr)은 자가 수분해서 자신과 같은 형질의 후손을 남긴다.

# 진송이는 이러한 완두콩의 자가 수분 실험 결과를 정리하고 싶어합니다.
# 하지만, 세대를 거듭할수록, 완두콩의 수가 너무 많아져 모든 가계도를 기록하기 어려워졌습니다.
# 진송이는 가계도를 전부 기록하는 것 대신, 완두콩의 세대와 해당 세대에서
# 몇 번째 개체인지를 알면 형질을 바로 계산하는 프로그램을 만들려 합니다.

# 각 세대에서 맨 왼쪽 개체부터 첫 번째, 두 번째, 세 번째, ...개체로 나타냅니다.

# 형질을 알고 싶은 완두콩의 세대를 나타내는 정수 n과,
# 해당 완두콩이 세대 내에서 몇 번째 개체인지를 나타내는 정수 p가
# 2차원 정수 배열 queries의 원소로 주어집니다.
# queries에 담긴 순서대로 n세대의 p 번째 개체의 형질을 문자열 배열에 담아서 return 하도록 solution 함수를 완성해주세요.

# 입출력 예
# queries	                    result
# [[3, 5]]	                    ["RR"]
# [[3, 8], [2, 2]]	            ["rr", "Rr"]
# [[3, 1], [2, 3], [3, 9]]	    ["RR", "Rr", "RR"]
# [[4, 26]]	                    ["Rr"]


# 1
def solution(queries):
    def get_gene(n, p):
        state = "Rr"  # 세대 1은 항상 Rr
        while n > 1:
            child = (p - 1) % 4  # 이번 단계에서 고른 자식(0~3)
            # Rr의 자식: [RR, Rr, Rr, rr]
            if child == 0:
                state = "RR"
            elif child == 3:
                state = "rr"
            # 한 세대 위로
            p = (p - 1) // 4 + 1
            n -= 1
        return state  # RR/rr이면 중간에 확정, 아니면 끝까지 갔을 때 Rr

    return [get_gene(n, p) for n, p in queries]


# 2
def solution(queries):
    def kth_genotype(n, p):
        # 세대 1의 개체는 항상 Rr (문제 전개상 기본 가정)
        state = "Rr"
        if n == 1:
            return state

        # p-1의 4진수 자릿수를 위(상위 세대)부터 차례로 읽어가며 이동
        # k번째 단계에서 사용할 자릿수: ((p-1) // 4**(n-1-k)) % 4
        x = p - 1
        for level in range(2, n + 1):
            if state == "RR":
                # 순종은 이후로도 변함없음
                return "RR"
            if state == "rr":
                return "rr"

            # 현재 단계에서 선택된 자식 인덱스(0~3)
            digit = (x // (4 ** (n - level))) % 4

            # 부모가 Rr일 때의 자식 매핑: [RR, Rr, Rr, rr]
            if digit == 0:
                state = "RR"
            elif digit in (1, 2):
                state = "Rr"
            else:  # digit == 3
                state = "rr"

        return state

    # 쿼리별로 계산
    return [kth_genotype(n, p) for n, p in queries]


print(solution([[3, 6]]))
